import streamlit as st
st.set_page_config(
    page_title="Update Status | AI-Powered Order Management System",
    page_icon="👓",
    layout="wide",
)
import requests
from ui_utils import show_header

show_header(active_page="update")


API_URL = "https://ai-powered-optical-lens-order-management.onrender.com"

st.title("🔄 Update Order Status")

orders = requests.get(f"{API_URL}/orders").json()

if orders:

    order_map = {f"{o['id']} - {o['customer_name']}": o["id"] for o in orders}

    selected = st.selectbox("Select Order", list(order_map.keys()))

    status = st.selectbox(
        "Status",
        [
            "Order Placed",
            "Prescription Verified",
            "Lens Allocated",
            "Production",
            "QC",
            "QC Failed",
            "Reorder",
            "Packed",
            "Shipped",
            "Delivered",
        ],
    )

    reason = st.text_input("Delay Reason (Optional)")

    if st.button("Update Status"):

        order_id = order_map[selected]

        requests.put(
            f"{API_URL}/orders/{order_id}",
            json={"status": status, "delay_reason": reason},
        )

        st.success("Status Updated")
