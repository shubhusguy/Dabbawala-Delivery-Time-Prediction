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
Raw Orders  →  Feature Engineering  →  Encoding & Scaling  →  Model Training  →  Deployment
```

**Engineered features** (the real secret sauce):
| Feature | What it captures |
|---|---|
| `route_frequency` | How often this pickup→delivery path is travelled |
| `dabbawala_workload` | How busy a specific dabbawala typically is |
| `distance_category` | Short / Medium / Long distance banding |
| `customer_feedback_encoded` | Historical service rating, numerically encoded |
| `is_weekend` | Whether the order falls on a weekend |

### The Model Bake-Off
Four contenders entered. One generalized best.

| Model | Train R² | Test R² | Test RMSE | Test MAE |
|---|---|---|---|---|
| **Linear Regression** 🏆 | 0.9267 | **0.9279** | 4.51 | 3.55 |
| Gradient Boosting | 0.9308 | 0.9192 | 4.77 | 3.81 |
| XGBoost | 0.9276 | 0.9166 | 4.85 | 3.87 |
| Random Forest (Tuned) | 0.9105 | 0.8842 | 5.71 | 4.54 |
| Random Forest | 0.8667 | 0.8454 | 6.60 | 5.17 |

The plot twist: the fanciest models *memorized* the training data harder but **generalized worse**. Plain old Linear Regression, with well-engineered features underneath it, quietly won. Sometimes the boring model is the right model.

---

## 🏗️ Project Structure

```
dabbawala-time-predictor/
├── app.py                  # Flask app — routes, feature engineering, prediction
├── model.pkl               # Trained pipeline + encoders + lookup tables
├── requirements.txt        # Python dependencies
├── Procfile                # Render/gunicorn entrypoint
└── templates/
    ├── index.html          # Landing page — the pitch
    └── form.html           # The actual prediction form
```

---

## ⚙️ Tech Stack

| Layer | Tools |
|---|---|
| **Modeling** | scikit-learn, pandas, numpy |
| **Backend** | Flask, gunicorn |
| **Frontend** | HTML, CSS, vanilla JS (no frameworks — just a dabba and a button) |
| **Deployment** | GitHub + Render (free tier) |

---

## 🚀 Running It Locally

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/dabbawala-time-predictor.git
cd dabbawala-time-predictor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py

# 4. Open in browser
http://localhost:8080
```

---

## 🔌 API Reference

### `POST /predict`

Send order details as form data, get back a delivery time estimate.

**Request** (`multipart/form-data`):
```
order_date, pickup_area, delivery_area, dabbawala_id,
distance_km, tiffin_weight_kg, charge_inr, customer_type,
tiffin_type, status, payment_mode, monthly_subscription,
customer_feedback
```

**Response:**
```json
{ "result": 38.4 }
```

**On error:**
```json
{ "error": "description of what went wrong" }
```

---

## 🎯 Why This Matters

- **For dispatchers** — flag orders at risk of running long, *before* they run long.
- **For customers** — know roughly when your lunch is arriving, without calling anyone.
- **For the network** — a small data-backed nudge on top of a century-old system that never really needed one, but might appreciate one anyway.

---

## ⚠️ Honest Limitations

- `route_frequency` and `dabbawala_workload` are computed on the full dataset before the train/test split — a mild source of information leakage worth knowing about if you're presenting these R² numbers as fully out-of-sample.
- The model is trained on a specific slice of Mumbai's dabbawala operations — it won't generalize to other cities or delivery networks out of the box.
- Free-tier hosting means the live demo may take ~30–50 seconds to wake up if it's been idle. That's Render being frugal, not the model being slow.

---

## 🙏 Credits

Built as a capstone project exploring end-to-end ML deployment — from raw logistics data to a live, publicly accessible prediction tool.

Inspired by the actual dabbawalas of Mumbai, whose real-world error rate is roughly **1 in 6 million deliveries** — a bar this model doesn't claim to clear, but was fun to chase.

---

<p align="center"><i>🍱 Made with pandas, patience, and a healthy respect for people who deliver lunch better than most logistics companies deliver anything.</i></p>

<p align="center"><b>Shubham Pote</b><br>Imarticus Learning</p>
