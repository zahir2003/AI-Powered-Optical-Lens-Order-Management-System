import pandas as pd
import random

lens_types = ["Single Vision", "Progressive", "Bifocal"]

stages = [
    "Order Placed",
    "Prescription Verified",
    "Lens Allocated",
    "Production",
    "QC",
    "Packed",
    "Shipped",
]

store_locations = ["Durgapur", "Kolkata", "Delhi", "Mumbai", "Bangalore"]

data = []

for _ in range(10000):

    lens = random.choice(lens_types)

    stage = random.choice(stages)

    store = random.choice(store_locations)

    inventory_available = random.choice([0, 1])

    sla_hours = {"Single Vision": 24, "Progressive": 72, "Bifocal": 48}[lens]

    elapsed_hours = random.randint(1, 100)

    days_in_current_stage = random.randint(0, 5)

    elapsed_percentage = elapsed_hours / sla_hours

    risk_score = 0

    if inventory_available == 0:
        risk_score += 40

    if stage == "Production":
        risk_score += 15

    if stage == "QC":
        risk_score += 25

    if elapsed_percentage > 0.6:
        risk_score += 25

    if elapsed_percentage > 0.8:
        risk_score += 20

    if lens == "Progressive":
        risk_score += 10

    if days_in_current_stage > 2:
        risk_score += 15

    # Add randomness
    risk_score += random.randint(-5, 5)

    risk_score = max(0, min(risk_score, 100))

    threshold = 50

    if risk_score >= threshold:
        breached = 1
    else:
        breached = 0

    # add a little noise
    if random.random() < 0.08:
        breached = 1 - breached

    data.append(
        [
            lens,
            stage,
            store,
            inventory_available,
            elapsed_hours,
            sla_hours,
            days_in_current_stage,
            breached,
        ]
    )

df = pd.DataFrame(
    data,
    columns=[
        "lens_type",
        "stage",
        "store_location",
        "inventory_available",
        "elapsed_hours",
        "sla_hours",
        "days_in_current_stage",
        "breached",
    ],
)

df.to_csv("historical_orders.csv", index=False)

print("Dataset Generated Successfully!")
print(df.head())
