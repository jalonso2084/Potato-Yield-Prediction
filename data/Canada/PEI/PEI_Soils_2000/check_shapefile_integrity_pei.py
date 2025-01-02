import os

# Path to the folder containing shapefiles
folder_path = r"C:\Users\jorge\Potato-Yield-Prediction\data\Canada\PEI\PEI_Soils_2000"

# List of shapefile base names (without extensions)
shapefiles = ["soil", "dss_v3_pe"]  # Add any other shapefile base names here

# Check for required files
required_extensions = [".shp", ".dbf", ".prj", ".shx"]

for shapefile in shapefiles:
    print(f"Checking {shapefile} in {folder_path}...")
    for ext in required_extensions:
        file_path = os.path.join(folder_path, shapefile + ext)
        if os.path.exists(file_path):
            print(f"  Found: {file_path}")
        else:
            print(f"  Missing: {file_path}")
