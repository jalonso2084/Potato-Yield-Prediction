import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler

# Directory containing your CSV files
directory = r"C:\Users\jorge\OneDrive\Documents\csv_files"

# Directory to save cleaned files
cleaned_directory = r"C:\Users\jorge\OneDrive\Documents\csv_files_cleaned"
os.makedirs(cleaned_directory, exist_ok=True)

# List to store cleaning summaries for each file
cleaning_summary = []

# Loop through each file in the directory
for file_name in os.listdir(directory):
    if file_name.endswith(".csv"):
        file_path = os.path.join(directory, file_name)
        try:
            # Load the CSV file
            df = pd.read_csv(file_path, on_bad_lines='skip')

            # Step 1: Unit Standardization (Example: Precipitation to mm, Yield to tons/ha)
            if "Precipitation" in df.columns:
                df["Precipitation"] = df["Precipitation"].apply(lambda x: x * 25.4 if x < 10 else x)  # Example: inches to mm
            if "Yield" in df.columns:
                df["Yield"] = df["Yield"].apply(lambda x: x / 1000)  # Example: kg/ha to tons/ha

            # Step 2: Remove Duplicates
            duplicates_before = len(df) - len(df.drop_duplicates())
            df.drop_duplicates(inplace=True)

            # Step 3: Normalize Numerical Columns
            scaler = MinMaxScaler()
            numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
            if not numeric_cols.empty:
                df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

            # Save the cleaned DataFrame to the cleaned directory
            cleaned_file_path = os.path.join(cleaned_directory, f"cleaned_{file_name}")
            df.to_csv(cleaned_file_path, index=False)

            # Update summary with cleaning details
            cleaning_summary.append({
                "File Name": file_name,
                "Duplicates Removed": duplicates_before,
                "Columns Normalized": list(numeric_cols)
            })

            print(f"File: {file_name} cleaned and saved to {cleaned_file_path}")

        except Exception as e:
            # Log the error
            print(f"Error processing file: {file_name}")
            print(f"Error: {e}")
            cleaning_summary.append({
                "File Name": file_name,
                "Error": str(e)
            })

# Convert the cleaning summary list into a DataFrame
summary_df = pd.DataFrame(cleaning_summary)

# Save the summary to a CSV file
summary_path = os.path.join(directory, "data_cleaning_summary.csv")
summary_df.to_csv(summary_path, index=False)

# Print completion message
print(f"Data cleaning completed. Summary saved to: {summary_path}")
