from datetime import datetime


def calculate_remaining_time(order):
    elapsed = (datetime.utcnow() - order.created_at).total_seconds() / 3600

    remaining = order.sla_hours - elapsed

    return round(remaining, 2)
