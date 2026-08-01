from flask import Flask, render_template, request, jsonify
from datetime import datetime
import pickle
import pandas as pd

# ---------------------------------------------------------------------------
# Load the deployment bundle produced at the end of capstone.ipynb (Section 10).
# It contains: the fitted preprocessing+model pipeline, plus the lookup tables
# needed to engineer route_frequency / dabbawala_workload / customer_feedback
# for a brand new order the same way they were engineered during training.
# ---------------------------------------------------------------------------
with open('model.pkl', 'rb') as f:
    artifacts = pickle.load(f)

model = artifacts['model']
encoder = artifacts['encoder']
scaler = artifacts['scaler']
cat_cols = artifacts['cat_cols']
num_cols = artifacts['num_cols']
route_freq_map = artifacts['route_freq_map']
route_freq_default = artifacts['route_freq_default']
dabbawala_freq_map = artifacts['dabbawala_freq_map']
dabbawala_freq_default = artifacts['dabbawala_freq_default']
feedback_map = artifacts['feedback_map']
options = artifacts['options']

app = Flask(__name__)

DAY_ORDER = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
FEEDBACK_OPTIONS = ['Not Available', 'Poor', 'Average', 'Good', 'Excellent']


def distance_bin(d):
    """Same binning rule used in capstone.ipynb Section 6.4."""
    if d <= 8:
        return 'Short'
    elif d <= 16:
        return 'Medium'
    else:
        return 'Long'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form')
def form_page():
    return render_template(
        'form.html',
        options=options,
        feedback_options=FEEDBACK_OPTIONS
    )


@app.route('/predict', methods=['POST'])
def predict():
    form = request.form

    try:
        order_date = form.get('order_date')
        pickup_area = form.get('pickup_area')
        delivery_area = form.get('delivery_area')
        dabbawala_id = form.get('dabbawala_id')
        distance_km = float(form.get('distance_km'))
        tiffin_weight_kg = float(form.get('tiffin_weight_kg'))
        charge_inr = float(form.get('charge_inr'))
        customer_type = form.get('customer_type')
        tiffin_type = form.get('tiffin_type')
        status = form.get('status')
        payment_mode = form.get('payment_mode')
        monthly_subscription = form.get('monthly_subscription')
        customer_feedback = form.get('customer_feedback')

        # --- Engineer features exactly the way capstone.ipynb Section 6 does ---
        date_obj = datetime.strptime(order_date, '%Y-%m-%d')
        day_of_week = DAY_ORDER[date_obj.weekday()]
        order_month = date_obj.month
        order_day = date_obj.day
        is_weekend = 1 if day_of_week in ['Saturday', 'Sunday'] else 0

        distance_category = distance_bin(distance_km)

        route_key = f"{pickup_area}_to_{delivery_area}"
        route_frequency = route_freq_map.get(route_key, route_freq_default)

        dabbawala_workload = dabbawala_freq_map.get(dabbawala_id, dabbawala_freq_default)

        customer_feedback_encoded = feedback_map.get(customer_feedback, 0)

        # --- One row, raw columns exactly as engineered in capstone.ipynb ---
        row = pd.DataFrame([{
            'day_of_week': day_of_week,
            'customer_type': customer_type,
            'tiffin_type': tiffin_type,
            'status': status,
            'payment_mode': payment_mode,
            'monthly_subscription': monthly_subscription,
            'distance_category': distance_category,
            'distance_km': distance_km,
            'tiffin_weight_kg': tiffin_weight_kg,
            'charge_inr': charge_inr,
            'order_month': order_month,
            'order_day': order_day,
            'is_weekend': is_weekend,
            'route_frequency': route_frequency,
            'dabbawala_workload': dabbawala_workload,
            'customer_feedback_encoded': customer_feedback_encoded,
        }])

        # --- Encode + scale exactly as Section 9.2 of the notebook does, then
        #     concatenate in the same column order the model was trained on ---
        row_cat = encoder.transform(row[cat_cols])
        row_cat = pd.DataFrame(row_cat, columns=encoder.get_feature_names_out(cat_cols), index=row.index)

        row_num = pd.DataFrame(scaler.transform(row[num_cols]), columns=num_cols, index=row.index)

        row_final = pd.concat([row_num, row_cat], axis=1)

        prediction = model.predict(row_final)[0]
        result = round(float(prediction), 1)

        return jsonify({'result': result})

    except Exception as exc:
        return jsonify({'error': str(exc)}), 400


if __name__ == '__main__':
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
