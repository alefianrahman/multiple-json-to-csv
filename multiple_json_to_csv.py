import pandas as pd
import numpy as np
import os

"""
This library will receive multiple JSON files in a folder, combine the 
files, and output the files to a CSV file.
"""

json_path = '/path/to/json'  # Path to JSON files
output_name = 'results.csv'  # Output filename


def multiple_json_to_csv(path=json_path, filename=output_name):
    """
    This function will receive multiple JSON files in a folder, combine the
    files, and output the files to a CSV file.
    """
    list_data = []  # initiate empty list

    # Combine multiple JSON files into a list of Data Frames
    for file in (os.listdir(path)):
        if '.json' in file:
            file_path = json_path + os.sep + file
            list_data.append(pd.read_json(file_path))

    all_data = None  # Initiate a dummy variable

    # Merge all Data Frames
    for data in list_data:
        if all_data is None:
            all_data = data
        else:
            all_data.append(data)

    # Convert the Data Frame to a CSV file
    all_data.to_csv(filename, index=False)


if __name__ == '__main__':
    multiple_json_to_csv()




