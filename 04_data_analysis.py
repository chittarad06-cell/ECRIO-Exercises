"""Exercises 13-21: structured data, NumPy, pandas, cleaning, grouping, and trends."""

import numpy as np
import pandas as pd


def sample_dataset():
    return pd.DataFrame(
        {
            "Name": ["Asha", "Ravi", "Meera", "John", "Asha", "Sara"],
            "Age": [17, 22, np.nan, 41, 17, 35],
            "Sales": [800, 1500, 2300, 1200, 800, 3100],
            "Department": ["A", "B", "A", "B", "A", "C"],
            "Date": pd.to_datetime(
                ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04", "2026-01-01", "2026-01-05"]
            ),
        }
    )


def exercise_13_data_processing_report():
    return (
        "Structured data is organized in rows and columns, such as CSV files and database tables. "
        "Unstructured data has no fixed schema, such as emails, images, videos, and free-text reports. "
        "The five common stages of data processing are collection, cleaning, transformation, analysis, and visualization/reporting."
    )


def exercise_14_numpy_statistics():
    array = np.array([10, 20, 30, 40, 50])
    return {
        "array_plus_5": (array + 5).tolist(),
        "array_times_2": (array * 2).tolist(),
        "mean": float(np.mean(array)),
        "median": float(np.median(array)),
        "standard_deviation": float(np.std(array)),
    }


def exercise_15_to_20_pandas_operations():
    df = sample_dataset()
    cleaned = df.drop_duplicates().copy()
    cleaned["Age"] = cleaned["Age"].fillna(cleaned["Age"].mean())

    filtered = cleaned[cleaned["Sales"] > 1000]
    pivot = cleaned.pivot_table(values="Sales", index="Department", aggfunc=["sum", "mean"])
    min_max_sales = (cleaned["Sales"] - cleaned["Sales"].min()) / (cleaned["Sales"].max() - cleaned["Sales"].min())
    z_score_sales = (cleaned["Sales"] - cleaned["Sales"].mean()) / cleaned["Sales"].std()

    return {
        "shape": cleaned.shape,
        "filtered_names": filtered["Name"].tolist(),
        "group_sales": cleaned.groupby("Department")["Sales"].sum().to_dict(),
        "pivot_table": pivot.round(2).to_dict(),
        "min_max_sales": min_max_sales.round(3).tolist(),
        "z_score_sales": z_score_sales.round(3).tolist(),
        "json_preview": cleaned.to_json(orient="records", date_format="iso"),
    }


def exercise_21_time_series():
    df = sample_dataset().drop_duplicates().sort_values("Date")
    df["rolling_sales"] = df["Sales"].rolling(window=2, min_periods=1).mean()
    return df[["Date", "Sales", "rolling_sales"]].to_dict(orient="records")


if __name__ == "__main__":
    print("Exercise 13:", exercise_13_data_processing_report())
    print("Exercise 14:", exercise_14_numpy_statistics())
    print("Exercises 15-20:", exercise_15_to_20_pandas_operations())
    print("Exercise 21:", exercise_21_time_series())
