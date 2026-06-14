import streamlit as st
st.set_page_config(
    page_title="Dashboard | AI-Powered Order Management System",
    page_icon="👓",
    layout="wide",
)
import requests
import pandas as pd
import plotly.express as px

from ui_utils import show_header
from streamlit_autorefresh import st_autorefresh

# st_autorefresh(interval=10000, key="dashboard_refresh") 

API_URL = "http://127.0.0.1:8000"

# st.set_page_config(page_title="AI Order Management System", layout="wide")

# Common Header + Navigation
show_header(active_page="dashboard")

# Fetch Data
orders = requests.get(f"{API_URL}/orders").json()
alerts = requests.get(f"{API_URL}/alerts").json()
inventory = requests.get(f"{API_URL}/inventory").json()

orders_df = pd.DataFrame(orders)
alerts_df = pd.DataFrame(alerts)
inventory_df = pd.DataFrame(inventory)

# ==========================
# FILTERS
# ==========================

if not orders_df.empty:

    st.subheader("Filters")

    col1, col2, col3 = st.columns(3)

    with col1:
        status_filter = st.selectbox(
            "Status", ["All"] + sorted(orders_df["status"].unique().tolist())
        )

    with col2:
        lens_filter = st.selectbox(
            "Lens Type", ["All"] + sorted(orders_df["lens_type"].unique().tolist())
        )

    with col3:
        store_filter = st.selectbox(
            "Store Location",
            ["All"] + sorted(orders_df["store_location"].unique().tolist()),
        )

    filtered_orders = orders_df.copy()

    if status_filter != "All":
        filtered_orders = filtered_orders[filtered_orders["status"] == status_filter]

    if lens_filter != "All":
        filtered_orders = filtered_orders[filtered_orders["lens_type"] == lens_filter]

    if store_filter != "All":
        filtered_orders = filtered_orders[
            filtered_orders["store_location"] == store_filter
        ]

else:

    filtered_orders = orders_df

# ==========================
# KPI SECTION
# ==========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div style="text-align:center;">
            <div>Total Orders</div>
            <h1 style="margin-top:12px;">{len(filtered_orders)}</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div style="text-align:center;">
            <div>High Risk Orders</div>
            <h1 style="margin-top:12px;">{len(alerts_df)}</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    delivered = (
        len(filtered_orders[filtered_orders["status"] == "Delivered"]) if not filtered_orders.empty else 0
    )

    st.markdown(
        f"""
        <div style="text-align:center;">
            <div>Delivered Orders</div>
            <h1 style="margin-top:12px;">{delivered}</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col4:
    st.markdown(
        f"""
        <div style="text-align:center;">
            <div>Inventory Items</div>
            <h1 style="margin-top:12px;">{len(inventory_df)}</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

# ==========================
# CHARTS
# ==========================

if not filtered_orders.empty:

    col1, col2 = st.columns(2)

    with col1:

        status_chart = px.pie(
            filtered_orders,
            names="status",
            title="Orders by Status",
        )

        st.plotly_chart(
            status_chart,
            use_container_width=True,
        )

    with col2:

        lens_chart = px.bar(
            filtered_orders,
            x="lens_type",
            title="Orders by Lens Type",
        )

        st.plotly_chart(
            lens_chart,
            use_container_width=True,
        )

st.divider()

# ==========================
# ORDERS
# ==========================

st.markdown(
    """
    <h2 style='font-size:36px;font-weight:700'>
    📦 Orders
    </h2>
    """,
    unsafe_allow_html=True,
)

if not filtered_orders.empty:

    column_order = [
        "id",
        "customer_name",
        "store_location",
        "lens_type",
        "power",
        "lens_index",
        "coating",
        "frame",
        "quantity",
        "status",
        "inventory_available",
        "sla_hours",
        "elapsed_hours",
        "delay_reason",
        "predicted_breach",
        "predicted_confidence",
        "created_at",
    ]

    available_columns = [col for col in column_order if col in filtered_orders.columns]

    filtered_orders = filtered_orders[available_columns]

    st.dataframe(
        filtered_orders,
        use_container_width=True,
        hide_index=True,
    )

else:
    st.info("No Orders Found")

# ==========================
# AI ALERTS
# ==========================

st.markdown(
    """
    <h2 style='font-size:36px;font-weight:700'>
    🚨 AI Alerts
    </h2>
    """,
    unsafe_allow_html=True,
)

if alerts_df.empty:
    st.success("No High-Risk Orders Found")
else:
    st.dataframe(
        alerts_df,
        use_container_width=True,
        hide_index=True,
    )

st.divider()

# ==========================
# INVENTORY
# ==========================

st.markdown(
    """
    <h2 style='font-size:36px;font-weight:700'>
    🏭 Inventory
    </h2>
    """,
    unsafe_allow_html=True,
)

if not inventory_df.empty:
    st.dataframe(
        inventory_df,
        use_container_width=True,
        hide_index=True,
    )
else:
    st.info("No Inventory Found")
