import pandas as pd


ALLOWED_LOGIN_STATUSES = {"success", "failed"}
ALLOWED_DEVICES = {"mobile", "desktop", "tablet"}


def clean_logs(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df = df.drop_duplicates(subset=["event_id"])

    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    df = df.dropna(subset=["event_id", "timestamp", "user_id", "login_status"])

    df = df[df["login_status"].isin(ALLOWED_LOGIN_STATUSES)]
    df = df[df["device_type"].isin(ALLOWED_DEVICES)]

    df["risk_score"] = pd.to_numeric(df["risk_score"], errors="coerce")
    df = df[df["risk_score"].between(0, 100, inclusive="both")]

    df.loc[df["login_status"] == "success", "failure_reason"] = None

    return df


if __name__ == "__main__":
    raw_df = pd.read_csv("security_logs_raw.csv")
    clean_df = clean_logs(raw_df)
    clean_df.to_csv("security_logs_cleaned.csv", index=False)

    print(f"Raw records: {len(raw_df)}")
    print(f"Cleaned records: {len(clean_df)}")