import pandas as pd
import random
import uuid
from datetime import datetime, timedelta

NUM_RECORDS = 200

countries = ["GR", "US", "DE", "FR", "UK"]
devices = ["mobile", "desktop", "tablet"]
login_statuses = ["success", "failed"]
failure_reasons = ["wrong_password", "user_not_found", "account_locked", None]


def generate_log():
    status = random.choice(login_statuses)

    return {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.now() - timedelta(minutes=random.randint(0, 5000)),
        "user_id": f"user_{random.randint(1, 50)}",
        "ip_address": f"192.168.{random.randint(0,255)}.{random.randint(0,255)}",
        "country": random.choice(countries),
        "device_type": random.choice(devices),
        "login_status": status,
        "failure_reason": random.choice(failure_reasons) if status == "failed" else None,
        "risk_score": random.randint(0, 100)
    }


def generate_dataset(n=NUM_RECORDS):
    data = [generate_log() for _ in range(n)]
    df = pd.DataFrame(data)
    return df


if __name__ == "__main__":
    df = generate_dataset()
    df.to_csv("security_logs_raw.csv", index=False)
    print("Generated dataset with", len(df), "records")