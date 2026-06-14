# 👓 AI-Powered Optical Lens Order Management System

<div align="center">

### 🚀 Smart Order Tracking • AI Risk Prediction • Inventory Intelligence • SLA Monitoring • Email Alerts

A Full-Stack AI-Powered Order Management Platform designed for Optical Lens Manufacturing & Retail Operations.

Built with **FastAPI**, **Streamlit**, **SQLite**, **Machine Learning**, and **Automated Monitoring** to streamline order processing, inventory management, SLA tracking, and proactive delay prediction.

---

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge\&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge\&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red?style=for-the-badge\&logo=streamlit)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge\&logo=sqlite)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge\&logo=scikitlearn)
![APScheduler](https://img.shields.io/badge/APScheduler-Automation-purple?style=for-the-badge)

</div>

---

# 📌 Project Overview

Managing optical lens orders involves multiple stages including inventory allocation, production, quality control, packaging, shipping, and delivery.

Traditional systems often react to delays after they occur.

This project introduces an **AI-Powered Predictive Monitoring System** that proactively identifies high-risk orders before SLA breaches occur, enabling operations teams to take preventive action.

The platform combines:

✅ Order Management

✅ Inventory Tracking

✅ SLA Monitoring

✅ AI-Based Delay Prediction

✅ Automated Risk Detection

✅ Email Notifications

✅ Interactive Analytics Dashboard

---

# 🎯 Business Problem

Optical stores and manufacturing units face challenges such as:

* Inventory shortages
* Production bottlenecks
* Quality control failures
* Missed delivery SLAs
* Lack of visibility into order progress
* Delayed identification of risky orders

These issues often result in:

❌ Customer dissatisfaction

❌ Revenue loss

❌ Operational inefficiencies

❌ Increased manual monitoring efforts

---

# 💡 Solution

The system continuously monitors order lifecycle data and uses AI-driven risk analysis to predict whether an order is likely to miss its SLA.

When a risky order is detected:

🚨 Alerts are automatically generated

📧 Email notifications are sent

📊 Dashboard metrics are updated

🤖 AI confidence scores are calculated

⚡ Operations teams can take preventive actions

---

# 🏗️ System Architecture

```text
                    ┌───────────────────┐
                    │     Streamlit     │
                    │    Frontend UI    │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │      FastAPI      │
                    │     Backend API   │
                    └─────────┬─────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼                               ▼
    ┌─────────────────┐          ┌─────────────────┐
    │     SQLite      │          │ Machine Learning│
    │    Database     │          │ Random Forest   │
    └─────────────────┘          └─────────────────┘
                                             │
                                             ▼
                                  ┌─────────────────┐
                                  │ APScheduler     │
                                  │ Auto Monitoring │
                                  └─────────────────┘
```

# ✨ Key Features

## 📦 Inventory Management

* Add and manage optical lens inventory
* Track stock quantities
* Support multiple lens specifications
* Real-time inventory verification

---

## 📝 Order Management

* Create customer orders
* Capture lens specifications
* Store customer and location information
* Quantity-based order processing

---

## 🔄 Intelligent Order Workflow

```text
Order Placed
    ↓
Production
    ↓
QC
   ↙   ↘
Pass   Fail
 ↓       ↓
Packed  Reorder
 ↓       ↓
Shipped Production
 ↓       ↓
Delivered QC
           ↓
        Packed
           ↓
        Shipped
           ↓
        Delivered
```

QC failures automatically trigger a reorder workflow, simulating real-world optical manufacturing processes.

---

## ⏱️ SLA Management

The platform dynamically assigns SLA targets based on lens complexity.

| Lens Type     | SLA      |
| ------------- | -------- |
| Single Vision | 24 Hours |
| Progressive   | 48 Hours |
| Bifocal       | 72 Hours |

The AI engine continuously monitors remaining SLA time and predicts potential breaches before they occur.

---

## 📊 Interactive Dashboard

Monitor:

* Total Orders
* Delivered Orders
* High-Risk Orders
* Inventory Items

Includes:

* Order Status Analytics
* Lens Type Distribution
* Inventory Overview
* AI Risk Monitoring
* Operational KPIs

---

## 🤖 AI-Powered Risk Prediction

Machine Learning model evaluates:

* Lens Type
* Order Status
* Store Location
* Inventory Availability
* Elapsed Processing Hours
* SLA Hours
* Workflow Progress

Output:

```text
Prediction:
    Breach / No Breach

Confidence Score:
    0 - 100%
```

---

## 🚨 Smart Alerts & Email Notifications

The system proactively identifies orders likely to breach their SLA.

Features:

* AI Risk Scoring
* High-Risk Order Detection
* SLA Breach Prediction
* Automated Email Notifications
* Operational Escalation Support

When a high-risk order is detected, email alerts are automatically sent to the operations team.

---

## ⚙️ Automated Monitoring

APScheduler continuously runs in the background and:

* Monitors active orders
* Calculates remaining SLA time
* Runs AI predictions
* Updates confidence scores
* Generates alerts
* Triggers automated email notifications

No manual monitoring required.

---

# 🧠 Machine Learning Pipeline

## Model

```python
RandomForestClassifier
```

## Features Used

```python
lens_type
stage
store_location
inventory_available
elapsed_hours
sla_hours
days_in_current_stage
```

## Output

```python
predicted_breach
predicted_confidence
```

---

# 🛠️ Technology Stack

## Frontend

* Streamlit
* Plotly

## Backend

* FastAPI
* SQLAlchemy
* Pydantic

## Database

* SQLite

## Machine Learning

* Scikit-Learn
* Random Forest Classifier
* Label Encoding

## Automation

* APScheduler

## Notifications

* SMTP Email Service
* Python Dotenv

## Deployment

* Render
* Streamlit Cloud

---

# 📁 Project Structure

```text
AI-Powered-Optical-Lens-Order-Management-System/

│
├── backend/
│   ├── app.py
│   ├── crud.py
│   ├── database.py
│   ├── email_service.py
│   ├── ml_service.py
│   ├── models.py
│   ├── scheduler.py
│   ├── schemas.py
│   └── .env
│
├── frontend/
│   ├── dashboard.py
│   ├── ui_utils.py
│   └── pages/
│
├── ml/
│   ├── train_model.py
│   ├── model.pkl
│   ├── lens_encoder.pkl
│   ├── stage_encoder.pkl
│   └── store_encoder.pkl
│
├── requirements.txt
├── .gitignore
└── README.md
```

# 🚀 Installation

## Clone Repository

```bash
git clone <repository-url>
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Backend

```bash
cd backend

uvicorn app:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Frontend

```bash
cd frontend

streamlit run dashboard.py
```

Frontend:

```text
http://localhost:8501
```

---

# 📈 Business Impact

The platform enables optical businesses to:

✅ Reduce SLA breaches through proactive monitoring

✅ Detect high-risk orders before delays occur

✅ Automate operational alerts using AI

✅ Improve inventory visibility

✅ Streamline lens manufacturing workflows

✅ Reduce manual tracking efforts

✅ Enhance customer satisfaction through timely deliveries

---

# 🌟 Future Enhancements

* User Authentication & Authorization
* Role-Based Access Control (Admin / Store Manager)
* WhatsApp Notifications
* Cloud Database Integration (PostgreSQL)
* Real-Time WebSocket Updates
* Advanced Predictive Analytics
* Demand Forecasting
* Multi-Store Performance Monitoring

---

# 👨‍💻 Author

### Sk Mahiduzzaman

**AI/ML Engineer | AI Developer**

Passionate about building intelligent systems that combine Machine Learning, Automation, and Modern Web Technologies to solve real-world business problems.

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

</div>
