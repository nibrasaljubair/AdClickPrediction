import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder


def main():
    # 1) Read CSV
    df = pd.read_csv("adsclicking.csv")
    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"], inplace=True)

    # 3) Encode categorical columns
    cat_cols = ["Gender", "Location", "Device", "Interest_Category"]
    for col in cat_cols:
        if col in df.columns and df[col].dtype == "object":
            df[col] = LabelEncoder().fit_transform(df[col])

    numeric_df = df.select_dtypes(include=[np.number])
    corr_matrix = numeric_df.corr()

    # 5) Plot 1: Correlation Heatmap
    plt.figure(figsize=(6, 5))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", square=True)
    plt.title("Correlation Heatmap of Numeric Features")
    plt.tight_layout()
    plt.savefig("correlation_heatmap.png")
    plt.close()
    print("Saved correlation_heatmap.png")

    numeric_cols_of_interest = ["Time_Spent_on_Site", "Number_of_Pages_Viewed", "Income", "Age"]
    for col in numeric_cols_of_interest:
        if col in df.columns:
            plt.figure(figsize=(6, 4))
            sns.violinplot(x="Click", y=col, data=df, palette="Set2", inner="quartile")
            plt.title(f"Distribution of {col} vs. Click")
            plt.tight_layout()
            outname = f"violin_{col}.png"
            plt.savefig(outname)
            plt.close()
            print(f"Saved {outname}")

    subset_cols = ["Age", "Income", "Time_Spent_on_Site", "Number_of_Pages_Viewed", "Click"]
    subset_cols = [c for c in subset_cols if c in df.columns]
    if len(subset_cols) > 1:
        pair_df = df[subset_cols].copy()
        pair_df["Click"] = pair_df["Click"].astype(str)

        sns.pairplot(
            pair_df,
            hue="Click",
            diag_kind="kde",
            palette="Set1",
            corner=True
        )
        plt.suptitle("Pairplot of Key Features (Color by Click)", y=1.02)
        plt.tight_layout()
        plt.savefig("pairplot_subset.png")
        plt.close()
        print("Saved pairplot_subset.png")

    print("\nAll plots saved. Check the *.png files to see the data patterns (or lack thereof).")


if __name__ == "__main__":
    main()
