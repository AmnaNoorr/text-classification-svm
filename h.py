import os

def find_csv_files(start_dir="C:/Users/Hp/Downloads", filename="IMDB Dataset.csv"):
    matches = []
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if "imdb" in file.lower() and file.endswith('.csv'):
                full_path = os.path.join(root, file)
                size = os.path.getsize(full_path)
                matches.append((full_path, size))
    return matches

# Search in Downloads
matches = find_csv_files()
if matches:
    print("Found IMDB CSV files:")
    for path, size in matches:
        print(f"  {path} ({size:,} bytes)")
else:
    print("No IMDB CSV files found in Downloads")