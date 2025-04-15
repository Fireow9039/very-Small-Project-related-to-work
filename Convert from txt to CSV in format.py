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
for index, file in enumerate(file_names, start=1):  # Serial No. starts from 1
    encoding = detect_encoding(file)  # Detect encoding dynamically
    deal_id = os.path.basename(file)  # Extract filename as Deal ID

    try:
        # Read the entire file content
        with open(file, "r", encoding=encoding, errors="ignore") as f:
            text_content = f.read().replace("\n", " ")  # Replace newlines with spaces

        # Append to data list
        data_list.append([index, deal_id, text_content])

    except Exception as e:
        print(f"Error reading {file}: {e}")

# Create DataFrame with columns: Serial No., Deal ID, Text Row
df = pd.DataFrame(data_list, columns=["Serial No.", "Deal ID", "Text Row"])

# Save to CSV
df.to_csv(csv_output, index=False)

print(f"All files merged successfully into {csv_output}")
