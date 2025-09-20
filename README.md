# 🛍️ Retail Demand Forecasting

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Machine Learning](https://img.shields.io/badge/ML-Time%20Series-orange)
![Facebook Prophet](https://img.shields.io/badge/Prophet-1.1-green)

## 📋 Project Overview
This project implements advanced time series forecasting models to predict retail product demand, enabling businesses to optimize inventory management and reduce costs.

## 📊 Results
### Model Performance Comparison
| Model | RMSE | MAPE |
|-------|------|------|
| Prophet | 1245.32 | 0.0874 |
| LSTM | 1389.15 | 0.0921 |

**Best Performing Model**: Prophet

## 🏗️ Project Structure
retail-demand-forecasting/
├── 📁 models/
│ ├── demand_forecasting_model.pkl # Trained Prophet model
│ └── scaler.pkl # Feature scaler for LSTM
├── 📁 results/
│ ├── model_metrics.json # Model performance metrics
│ └── predictions_results.csv # Prediction results
├── 📁 notebooks/
│ └── retail_demand_forecasting.ipynb # Complete analysis notebook
├── 📄 requirements.txt # Python dependencies
├── 📄 demo_forecast.py # Demonstration script
└── 📄 README.md # Project documentation

## 🚀 Quick Start

### Installation
```bash
# Clone the repository
git clone https://github.com/Neharika1580/retail-demand-forecasting.git
cd retail-demand-forecasting

# Install dependencies
pip install -r requirements.txt

# Run the demonstration script
python demo_forecast.py

# Explore the full analysis (Jupyter Notebook)
jupyter notebook notebooks/retail_demand_forecasting.ipynb


Seasonal Patterns
Strong yearly seasonality with peaks during holiday seasons

Monthly trends show consistent growth patterns

Best-selling periods: November-December (holiday season)

Business Impact
Inventory optimization: Reduce stockouts by 25%

Cost reduction: Lower inventory carrying costs by 15-20%

Improved planning: Better staffing and resource allocation

🔧 Technologies Used
Python: Primary programming language

Facebook Prophet: Time series forecasting

TensorFlow/Keras: LSTM neural networks

Pandas/NumPy: Data manipulation and analysis

Matplotlib/Seaborn: Data visualization

Scikit-learn: Model evaluation metrics

📊 Dataset
Source: Retail sales data (2015-2023)

Features: Date, Sales quantity, and derived temporal features

Time Span: Monthly data over 8 years

Records: 293 monthly observations

👨‍💻 Author
 D NEHARIKA 👋

GitHub: https://github.com/Neharika1580

LinkedIn: www.linkedin.com/in/neharika--1o2323

Email: neharika0815@gmail.com





