import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "ml", "model.pkl")
LENS_ENCODER_PATH = os.path.join(BASE_DIR, "ml", "lens_encoder.pkl")
STAGE_ENCODER_PATH = os.path.join(BASE_DIR, "ml", "stage_encoder.pkl")
STORE_ENCODER_PATH = os.path.join(BASE_DIR, "ml", "store_encoder.pkl")

model = joblib.load(MODEL_PATH)

lens_encoder = joblib.load(LENS_ENCODER_PATH)
stage_encoder = joblib.load(STAGE_ENCODER_PATH)
store_encoder = joblib.load(STORE_ENCODER_PATH)


def predict_breach(order):

    try:

        # -----------------------
        # Delivered Orders
        # -----------------------

        if order.status == "Delivered":
            return 0, 0

        # -----------------------
        # QC Failure / Reorder
        # -----------------------

        if order.status in ["QC Failed", "Reorder"]:
            return 1, 100

        # -----------------------
        # Remaining SLA Time
        # -----------------------

        remaining_hours = order.sla_hours - order.elapsed_hours

        # Already breached SLA
        if remaining_hours <= 0:
            return 1, 100

        # Very close to SLA
        if remaining_hours <= 4:
            return 1, 90

        # -----------------------
        # Normal Workflow
        # -----------------------
        # Order Placed
        # Production
        # QC
        # Packed
        # Shipped
        #
        # If enough SLA time remains,
        # the order is considered safe.
        # -----------------------

        return 0, 0

    except Exception as e:

        print("Prediction Error:", e)

        return 0, 0
