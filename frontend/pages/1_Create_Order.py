import streamlit as st
import requests
from ui_utils import show_header

show_header(active_page="create")

st.set_page_config(
    page_title="Create Order | AI-Powered Order Management System",
    page_icon="👓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

API_URL = "http://localhost:8000"

st.title("➕ Create New Order")

with st.form("order_form"):

    customer_name = st.text_input("Customer Name")

    store_location = st.selectbox(
        "Store Location", ["Durgapur", "Kolkata", "Delhi", "Mumbai"]
    )

    lens_type = st.selectbox("Lens Type", ["Single Vision", "Progressive", "Bifocal"])

    power = st.number_input("Power", value=-2.0)

    lens_index = st.selectbox("Lens Index", [1.50, 1.56, 1.60, 1.67,1.74])

    coating = st.selectbox(
        "Coating",
        [
            "Blue Cut",
            "Anti Glare",
            "UV Protection",
            "Scratch Resistant",
            "Anti Reflective",
            "Photochromic",
        ]
    )

    FRAMES = [
        "RayBan RB3025",
        "Titan Eye+",
        "John Jacobs JJ200",
        "Vincent Chase VC1001",
        "Oakley OX8156",
        "Lenskart Air Flex",
    ]

    frame = st.selectbox("Frame", FRAMES)

    quantity = st.number_input("Quantity", min_value=1, value=1, step=1)

    submitted = st.form_submit_button("Create Order")

if submitted:

    payload = {
        "customer_name": customer_name,
        "store_location": store_location,
        "lens_type": lens_type,
        "power": power,
        "lens_index": lens_index,
        "coating": coating,
        "frame": frame,
        "quantity": quantity,
    }

    response = requests.post(f"{API_URL}/orders", json=payload)

    if response.status_code == 200:
        st.success("Order Created Successfully")
    else:
        st.error("Failed")
