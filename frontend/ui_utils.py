# ui_utils.py

import streamlit as st

def show_header(active_page="dashboard"):
    st.title("👓 AI-Powered Order Management System")


# # def show_header(active_page="dashboard"):

# #     st.markdown(
# #         """
# #         <style>

# #         /* Hide Sidebar */
# #         [data-testid="stSidebar"]{
# #             display:none;
# #         }

# #         /* Main App Title */
# #         .main-title{
# #             font-size:60px;
# #             font-weight:900;
# #             margin-bottom:30px;
# #             text-align:center;
# #         }

# #         /* Navigation Buttons */
# #         div.stButton > button {

# #             width:100%;

# #             height:80px !important;

# #             font-size:28px !important;

# #             font-weight:700 !important;

# #             border-radius:20px !important;

# #             background: rgba(255,255,255,0.08) !important;

# #             backdrop-filter: blur(20px);

# #             -webkit-backdrop-filter: blur(20px);

# #             border:1px solid rgba(255,255,255,0.15) !important;

# #             color:white !important;

# #             transition: all 0.3s ease;

# #             box-shadow:
# #                 0 8px 32px rgba(0,0,0,0.35);
# #         }

# #         div.stButton > button:hover {

# #             border:1px solid #4ea8ff !important;

# #             transform:translateY(-3px);

# #             box-shadow:
# #                 0 12px 40px rgba(78,168,255,0.25);
# #         }

# #         /* ACTIVE PAGE GLOW EFFECT */

# #         div.stButton button[kind="primary"]{

# #             border:2px solid #4ea8ff !important;

# #             background: rgba(78,168,255,0.15) !important;

# #             color:white !important;

# #             box-shadow:
# #                 0 0 20px rgba(78,168,255,0.9),
# #                 0 0 40px rgba(78,168,255,0.5),
# #                 0 8px 32px rgba(0,0,0,0.35) !important;

# #             transform: translateY(-2px);
# #         }

# #         /* KPI Cards */

# #         div[data-testid="metric-container"]{

# #             background: rgba(255,255,255,0.06);

# #             backdrop-filter: blur(18px);

# #             border:1px solid rgba(255,255,255,0.12);

# #             border-radius:20px;

# #             padding:18px;

# #             box-shadow:
# #                 0 8px 32px rgba(0,0,0,0.25);
# #         }

# #         </style>
# #         """,
# #         unsafe_allow_html=True,
# #     )

#     # st.markdown(
#     #     """
#     #     <div class="main-title">
#     #         👓 AI-Powered Order Management System
#     #     </div>
#     #     """,
#     #     unsafe_allow_html=True,
#     # )

#     col1, col2, col3, col4, col5 = st.columns(5)

#     with col1:

#         dashboard_type = "primary" if active_page == "dashboard" else "secondary"

#         if st.button(
#             "Dashboard",
#             use_container_width=True,
#             type=dashboard_type,
#         ):
#             st.switch_page("dashboard.py")

#     with col2:

#         create_type = "primary" if active_page == "create" else "secondary"

#         if st.button(
#             "Create Order",
#             use_container_width=True,
#             type=create_type,
#         ):
#             st.switch_page("pages/1_Create_Order.py")

#     with col3:

#         update_type = "primary" if active_page == "update" else "secondary"

#         if st.button(
#             "Update Status",
#             use_container_width=True,
#             type=update_type,
#         ):
#             st.switch_page("pages/2_Update_Status.py")

#     with col4:

#         inventory_type = "primary" if active_page == "inventory" else "secondary"

#         if st.button(
#             "Inventory",
#             use_container_width=True,
#             type=inventory_type,
#         ):
#             st.switch_page("pages/3_Inventory.py")

#     with col5:

#         alerts_type = "primary" if active_page == "alerts" else "secondary"

#         if st.button(
#             "Alerts",
#             use_container_width=True,
#             type=alerts_type,
#         ):
#             st.switch_page("pages/4_Alerts.py")

#     st.markdown("<br>", unsafe_allow_html=True)
