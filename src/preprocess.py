import pandas as pd

def preprocess_data(input_path, output_path):
    # 1. Load the full raw dataset
    df = pd.read_csv(input_path)

    # 2. Select only columns relevant to the problem
    selected_columns = [
        "4. On average, how many hours of sleep do you get on a typical day?",
        "High stress",
        "Academic performance"
    ]

    df_model = df[selected_columns]

    # 3. Rename columns to clean, usable names
    df_model = df_model.rename(columns={
        "4. On average, how many hours of sleep do you get on a typical day?": "sleep_hours",
        "High stress": "stress",
        "Academic performance": "score"
    })

    # 4. Basic cleaning
    df_model = df_model.dropna()

    # 5. Save cleaned dataset
    df_model.to_csv(output_path, index=False)

    print("Cleaned data saved at:", output_path)

if __name__ == "__main__":
    preprocess_data("data/raw.csv", "data/cleaned.csv")
