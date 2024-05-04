import pandas as pd
import os


directory = os.path.join(os.path.dirname(__file__), '../..', 'data')
print(directory)

# Define the file name you want to read
file_name = 'hey_data.csv'

# Construct the full file path
file_path = os.path.join(directory, file_name)

# Read the CSV file
df = pd.read_csv(file_path)
