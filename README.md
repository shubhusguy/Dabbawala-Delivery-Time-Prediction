# 🍱 Dabbawala Delivery Time Prediction

> *"A tiffin never lies about where it's going — only about when it'll get there."*
> This project teaches a machine to guess better than we do.

<p align="center">
  <img src="https://img.shields.io/badge/Model-Linear%20Regression-29B6F6?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Test%20R²-0.928-E3A008?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Deployed%20on-Render-8A3B2E?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Live-1B6B8C?style=for-the-badge" />
</p>

---

# 🚀 Live Demo

## 🌐 **Try the application here**

### **👉 https://dabbawala-delivery-time-prediction.onrender.com/**

> **Note:** Since the application is hosted on Render's free tier, the first request after inactivity may take **30–50 seconds** to wake up.

---

## 📖 The Story

Every morning, before Mumbai fully wakes up, an army of dabbawalas is already in motion — cycling, sorting, stacking, and hand-delivering over **100,000 home-cooked tiffins** across the city with a punctuality that Harvard Business School once studied as a case in operational excellence.

They do this with almost no technology. No app. No GPS. Just colour-coded lids, a century of tradition, and instinct sharpened by decades on the road.

This project doesn't try to replace that instinct — it tries to **quantify** it. Given a route, a distance, a dabbawala's workload, and a few details about the order, can a model estimate delivery time as reliably as a dabbawala's gut feeling?

Turns out — pretty close. **R² ≈ 0.93** on unseen data.

---

## 🗺️ What This Actually Does

You fill in an order — pickup area, delivery area, distance, tiffin weight, dabbawala ID, payment mode, and a few more details — and the model hands back an **estimated delivery time in minutes**, before the tiffin has even left the kitchen.

```
Input:  Andheri → Nariman Point, 14.2 km, Dabbawala #2231, Prepaid, Subscribed
Output: 🕒 Estimated delivery time: 38.4 minutes
```

---

## 🧠 Under the Hood

### The Data Journey

```
Raw Orders
      ↓
Feature Engineering
      ↓
Encoding & Scaling
      ↓
Model Training
      ↓
Deployment
```

### Engineered Features

| Feature | What it captures |
|----------|------------------|
| `route_frequency` | How often this pickup→delivery path is travelled |
| `dabbawala_workload` | How busy a specific dabbawala typically is |
| `distance_category` | Short / Medium / Long distance banding |
| `customer_feedback_encoded` | Historical service rating, numerically encoded |
| `is_weekend` | Whether the order falls on a weekend |

---

## 📊 Model Performance

Four contenders entered. One generalized best.

| Model | Train R² | Test R² | Test RMSE | Test MAE |
|------|---------:|---------:|----------:|---------:|
| 🏆 **Linear Regression** | **0.9267** | **0.9279** | **4.51** | **3.55** |
| Gradient Boosting | 0.9308 | 0.9192 | 4.77 | 3.81 |
| XGBoost | 0.9276 | 0.9166 | 4.85 | 3.87 |
| Random Forest (Tuned) | 0.9105 | 0.8842 | 5.71 | 4.54 |
| Random Forest | 0.8667 | 0.8454 | 6.60 | 5.17 |

The plot twist: the fanciest models memorized the training data harder but **generalized worse**.

**Linear Regression won because good feature engineering matters more than model complexity.**

---

## 🏗️ Project Structure

```
dabbawala-time-predictor/
├── app.py
├── model.pkl
├── requirements.txt
├── Procfile
└── templates/
    ├── index.html
    └── form.html
```

---

## ⚙️ Tech Stack

| Layer | Tools |
|-------|-------|
| Machine Learning | scikit-learn, pandas, numpy |
| Backend | Flask, Gunicorn |
| Frontend | HTML, CSS, JavaScript |
| Deployment | GitHub + Render |

---

# 🌍 Run the Live Application

### **🔗 https://dabbawala-delivery-time-prediction.onrender.com/**

No installation required—simply open the link above in your browser and start predicting delivery times.

---

## 💻 Running Locally

```bash
# Clone repository
git clone https://github.com/<your-username>/dabbawala-time-predictor.git

# Move into project
cd dabbawala-time-predictor

# Install dependencies
pip install -r requirements.txt

# Start Flask server
python app.py
```

Open:

```
http://localhost:8080
```

---

## 🔌 API Reference

### POST `/predict`

Accepts order information as form data and returns the estimated delivery time.

### Request Fields

```
order_date
pickup_area
delivery_area
dabbawala_id
distance_km
tiffin_weight_kg
charge_inr
customer_type
tiffin_type
status
payment_mode
monthly_subscription
customer_feedback
```

### Success Response

```json
{
    "result": 38.4
}
```

### Error Response

```json
{
    "error": "description of what went wrong"
}
```

---

## 🎯 Why This Matters

- Predict delivery time before dispatch.
- Improve customer expectations.
- Assist operational planning.
- Demonstrate end-to-end Machine Learning deployment.

---

## ⚠️ Limitations

- `route_frequency` and `dabbawala_workload` are computed before the train/test split, introducing mild information leakage.
- Model is trained specifically on Mumbai Dabbawala operations.
- Render free tier may require **30–50 seconds** for the first request after inactivity.

---

## 🙏 Credits

Built as a capstone Machine Learning project exploring the complete ML lifecycle—from data preprocessing and feature engineering to deployment.

Inspired by Mumbai's legendary Dabbawalas, whose real-world error rate is approximately **1 in 6 million deliveries**.

---

<p align="center">
<b>🌐 Live Demo</b><br><br>

👉 <b>https://dabbawala-delivery-time-prediction.onrender.com/</b>

</p>

---

<p align="center">
<i>🍱 Made with pandas, patience, and a healthy respect for the people who deliver lunch better than most logistics companies deliver anything.</i>
</p>

<p align="center">
<b>Shubham Pote</b><br>
Imarticus Learning
</p>
