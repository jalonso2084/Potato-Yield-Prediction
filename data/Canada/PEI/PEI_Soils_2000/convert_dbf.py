from dbfread import DBF
import pandas as pd

# Replace with your actual .dbf file path
dbf_file = 'mapunit.dbf'

# Read the .dbf file
table = DBF(dbf_file, load=True)
data = pd.DataFrame(iter(table))

# Save as CSV or Excel
data.to_csv('output_file.csv', index=False)
data.to_excel('output_file.xlsx', index=False)

print("File converted successfully to CSV and Excel formats!")
