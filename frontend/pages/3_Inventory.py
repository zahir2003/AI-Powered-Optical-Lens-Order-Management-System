import streamlit as st
st.set_page_config(
    page_title="Inventory | AI-Powered Order Management System",
    page_icon="👓",
    layout="wide",
    initial_sidebar_state="collapsed",
)
import requests
import pandas as pd
from ui_utils import show_header

show_header(active_page="inventory")

API_URL = "https://ai-powered-optical-lens-order-management.onrender.com"

st.title("🏭 Inventory Management")

inventory = requests.get(f"{API_URL}/inventory").json()

if inventory:

    st.dataframe(pd.DataFrame(inventory), use_container_width=True)

st.divider()

st.subheader("Add Inventory")

with st.form("inventory_form"):

    lens_type = st.selectbox("Lens Type", ["Single Vision", "Progressive", "Bifocal"])

    power = st.number_input("Power", value=-2.0)

    lens_index = st.selectbox("Lens Index", [1.50, 1.56, 1.60, 1.67, 1.74])

    coating = st.selectbox(
    "Coating",
    [
        "Blue Cut",
        "Anti Glare",
        "UV Protection",
        "Scratch Resistant",
        "Anti Reflective",
        "Photochromic"
    ]
    )

    quantity = st.number_input("Quantity", min_value=1)

    submit = st.form_submit_button("Add Inventory")

if submit:

    payload = {
        "lens_type": lens_type,
        "power": power,
        "lens_index": lens_index,
        "coating": coating,
        "quantity": quantity,
    }

    requests.post(f"{API_URL}/inventory", json=payload)

    st.success("Inventory Added")
