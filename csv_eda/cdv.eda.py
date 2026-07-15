import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

def show_section(title):
    print(f"\n{'=' * 12} {title} {'=' * 12}")

def run_eda(csv_path):
    out = Path("output")
    out.mkdir(exist_ok=True)

    df = pd.read_csv(csv_path)

    shape_df = pd.DataFrame({
        "rows": [df.shape[0]],
        "columns": [df.shape[1]]
    })
    shape_df.to_csv(out / "shape.csv", index=False)

    summary = pd.DataFrame({
        "column": df.columns,
        "dtype": df.dtypes.astype(str).values,
        "missing": df.isnull().sum().values,
        "missing_pct": (df.isnull().sum().values / len(df) * 100).round(2),
        "unique": df.nunique().values
    })
    summary.to_csv(out / "column_summary.csv", index=False)

    show_section("Shape")
    print(shape_df.to_markdown(index=False, tablefmt="grid"))

    show_section("Column Summary")
    print(summary.head(10).to_markdown(index=False, tablefmt="grid"))

    show_section("First 10 Rows")
    print(df.head(10).to_markdown(index=False, tablefmt="grid"))

    num = df.select_dtypes(include="number")
    cat = df.select_dtypes(exclude="number")

    if not num.empty:
        num.describe().to_csv(out / "numeric_stats.csv")
        corr = num.corr(numeric_only=True)

        plt.figure(figsize=(10, 6))
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Numeric Correlation")
        plt.tight_layout()
        plt.savefig(out / "correlation_heatmap.png", dpi=200)
        plt.close()

        for col in num.columns[:6]:
            plt.figure(figsize=(7, 4))
            sns.histplot(df[col].dropna(), kde=True)
            plt.title(f"Distribution: {col}")
            plt.tight_layout()
            plt.savefig(out / f"{col}_hist.png", dpi=200)
            plt.close()

    for col in cat.columns[:6]:
        vc = df[col].astype(str).value_counts().head(10)
        vc.to_csv(out / f"{col}_value_counts.csv")

        plt.figure(figsize=(8, 4))
        vc.plot(kind="bar")
        plt.title(f"Top Values: {col}")
        plt.tight_layout()
        plt.savefig(out / f"{col}_bar.png", dpi=200)
        plt.close()

    show_section("Saved Files")
    print(f"Saved outputs to: {out.resolve()}")

root = tk.Tk()
root.withdraw()

csv_path = filedialog.askopenfilename(
    title="Select a CSV file",
    filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
)

if csv_path:
    run_eda(csv_path)
else:
    print("No file selected.")