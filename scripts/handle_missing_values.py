import pandas as pd
import os

# Directory containing your CSV files
directory = r"C:\Users\jorge\OneDrive\Documents\csv_files"

# Directory to save cleaned files
cleaned_directory = r"C:\Users\jorge\OneDrive\Documents\csv_files_cleaned"
os.makedirs(cleaned_directory, exist_ok=True)

# List to store missing value summaries for each file
missing_values_summary = []

# Loop through each file in the directory
for file_name in os.listdir(directory):
    if file_name.endswith(".csv"):
        file_path = os.path.join(directory, file_name)
        try:
            # Load the CSV file
            df = pd.read_csv(file_path, on_bad_lines='skip')
            
            # Get the initial count of missing values
            total_missing = df.isnull().sum().sum()
            column_missing = df.isnull().sum()

            # Handle missing values:
            # 1. Drop columns with more than 50% missing values
            df = df.dropna(axis=1, thresh=len(df) * 0.5)
            
            # 2. Fill numerical columns with the mean
            for column in df.select_dtypes(include=['float64', 'int64']).columns:
                df[column].fillna(df[column].mean(), inplace=True)
            
            # 3. Fill categorical columns with the mode
            for column in df.select_dtypes(include=['object']).columns:
                df[column].fillna(df[column].mode()[0], inplace=True)

            # Save the cleaned DataFrame to the cleaned directory
            cleaned_file_path = os.path.join(cleaned_directory, f"cleaned_{file_name}")
            df.to_csv(cleaned_file_path, index=False)

            # Update summary with post-cleaning information
            remaining_missing = df.isnull().sum().sum()
            missing_values_summary.append({
                "File Name": file_name,
                "Total Missing Values (Before)": total_missing,
                "Total Missing Values (After)": remaining_missing,
                "Dropped Columns": list(column_missing[column_missing > len(df) * 0.5].index)
            })

            print(f"File: {file_name} cleaned and saved to {cleaned_file_path}")

        except Exception as e:
            # Log the error
            print(f"Error processing file: {file_name}")
            print(f"Error: {e}")
            missing_values_summary.append({
                "File Name": file_name,
                "Error": str(e)
            })

# Convert the summary list into a DataFrame
summary_df = pd.DataFrame(missing_values_summary)

# Save the summary to a CSV file
summary_summary_path = os.path.join(directory, "missing_values_summary_cleaned.csv")
summary_df.to_csv(summary_summary_path, index=False)

# Print completion message
print(f"Cleaning completed. Summary saved to: {summary_summary_path}")
