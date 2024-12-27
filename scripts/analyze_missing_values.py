import pandas as pd
import os

# Directory containing your CSV files
directory = r"C:\Users\jorge\OneDrive\Documents\csv_files"

# List to store missing value summaries for each file
missing_values_summary = []

# Loop through each file in the directory
for file_name in os.listdir(directory):
    if file_name.endswith(".csv"):
        file_path = os.path.join(directory, file_name)
        try:
            # Load the CSV file, skipping problematic lines
            df = pd.read_csv(file_path, on_bad_lines='skip')  # Updated to use 'on_bad_lines'
            
            # Count missing values
            total_missing = df.isnull().sum().sum()
            column_missing = df.isnull().sum()
            
            # Add results to summary
            missing_values_summary.append({
                "File Name": file_name,
                "Total Missing Values": total_missing,
                "Columns with Missing Values": column_missing[column_missing > 0].to_dict()
            })
            
            print(f"File: {file_name}")
            print(f"Total Missing Values: {total_missing}")
            print("Columns with Missing Values:")
            print(column_missing[column_missing > 0])
            print("\n")
        
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
summary_df.to_csv(os.path.join(directory, "missing_values_summary.csv"), index=False)

# Print completion message
print("Analysis completed. Check 'missing_values_summary.csv' for details.")
