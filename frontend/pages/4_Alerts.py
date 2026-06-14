import streamlit as st

st.set_page_config(
    page_title="Alerts | AI-Powered Order Management System",
    page_icon="👓",
    layout="wide",
)
import requests
from ui_utils import show_header

show_header(active_page="alerts")

API_URL = "https://ai-powered-optical-lens-order-management.onrender.com"

st.title("⚠ AI Breach Alerts")

alerts = requests.get(f"{API_URL}/alerts").json()

if len(alerts) == 0:

    st.success("No High-Risk Orders Found")

else:

    for alert in alerts:

        risk = alert["risk"]
        confidence = alert["confidence"]

        if risk == "HIGH":
            st.error(f"""
                Order #{alert['order_id']}

                Customer: {alert['customer']}

                Status: {alert['status']}

                Confidence: {confidence:.2f}%
                """)

        else:

            st.warning(f"""
                Order #{alert['order_id']}

                Customer: {alert['customer']}

                Status: {alert['status']}

                Confidence: {confidence:.2f}%
                """)
