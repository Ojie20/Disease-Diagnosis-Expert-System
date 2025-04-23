import pandas as pd
import os

RAW_FILE = os.path.join('data', 'raw', 'Training.csv')
OUTPUT_FILE = os.path.join('data', 'cleaned', 'cleaned_training.csv')

def preprocess_for_model():
    # Load dataset
    df = pd.read_csv(RAW_FILE)

    # Drop unnamed or empty columns
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # Drop rows with missing values (optional; dataset appears clean)
    df.dropna(inplace=True)

    # Ensure all columns are lowercase and stripped
    df.columns = df.columns.str.lower().str.strip()

    # Save cleaned model-ready version
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)

    print(f"✅ Cleaned model-ready dataset saved to: {OUTPUT_FILE}")
    print(f"Rows: {len(df)}, Columns: {len(df.columns)}")

if __name__ == '__main__':
    preprocess_for_model()
