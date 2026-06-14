from apscheduler.schedulers.background import BackgroundScheduler

from database import SessionLocal
import crud

from ml_service import predict_breach
from email_service import send_alert_email


def check_orders():

    db = SessionLocal()

    try:

        orders = crud.get_orders(db)

        for order in orders:

            # Delivered orders should never trigger alerts
            if order.status == "Delivered":

                order.predicted_breach = False
                order.predicted_confidence = 0
                order.alert_sent = False

                continue

            prediction, confidence = predict_breach(order)

            order.predicted_breach = bool(prediction)
            order.predicted_confidence = confidence

            # Send email only once
            if prediction == 1 and confidence >= 80 and not order.alert_sent:

                send_alert_email(order, confidence)

                order.alert_sent = True

                print(f"Email Alert Sent for Order {order.id}")

        db.commit()

        # print("AI Monitoring Completed")

    except Exception as e:

        print("Scheduler Error:", e)

    finally:

        db.close()


scheduler = BackgroundScheduler()

scheduler.add_job(
    check_orders,
    "interval",
    seconds=1,
)
