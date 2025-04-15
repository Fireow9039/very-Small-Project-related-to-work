import pandas as pd
import glob
import os
import chardet

# Define directories
input_dir = "/Users/rohanjaiswal/Desktop/RA work Self/Text file to csv/pythonProject1/HIPPA"  # Folder with .txt files
output_dir = "/Users/rohanjaiswal/Desktop/RA work Self/Text file to csv/pythonProject1/HIPPA CSV"  # Folder for output
csv_output = os.path.join(output_dir, "merged_output.csv")  # Final merged CSV

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Get all text files in the input directory
file_names = glob.glob(os.path.join(input_dir, "*.txt"))


# Function to detect file encoding
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        return chardet.detect(f.read())["encoding"]


# Initialize list to store data
data_list = []

# Process each text file
for file in file_names:
    encoding = detect_encoding(file)  # Detect encoding dynamically
    deal_id = os.path.basename(file)  # Extract filename as Deal ID

    try:
        # Read file line by line
        with open(file, "r", encoding=encoding, errors="ignore") as f:
            for line in f:
                line = line.strip()  # Remove extra spaces and new lines
                if line:  # Ignore empty lines
                    data_list.append([deal_id, line])

    except Exception as e:
        print(f"Error reading {file}: {e}")

# Create DataFrame with columns: Deal ID and Text Row
df = pd.DataFrame(data_list, columns=["Deal ID", "Text Row"])

# Save to CSV
df.to_csv(csv_output, index=False)

print(f"All files merged successfully into {csv_output}")
