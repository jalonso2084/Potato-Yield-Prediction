# Path to the original file
original_file_path = r"C:\Users\jorge\OneDrive\Documents\csv_files\Climate_change_impacts_on_precipitation_and_temperature_in_PEI.docx.csv"

# Path to save the corrected file
corrected_file_path = r"C:\Users\jorge\OneDrive\Documents\csv_files\Corrected_Climate_change_impacts.csv"

# Read the original file and store its lines
with open(original_file_path, 'r') as file:
    lines = file.readlines()  # Read all lines into a list

# Remove the problematic line (line 9, which is index 8 in zero-based indexing)
corrected_lines = [line for i, line in enumerate(lines) if i != 8]

# Save the corrected content to a new file
with open(corrected_file_path, 'w') as corrected_file:
    corrected_file.writelines(corrected_lines)

print(f"Corrected file saved at: {corrected_file_path}")
