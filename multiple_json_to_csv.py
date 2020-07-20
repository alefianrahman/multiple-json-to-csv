import os
import pandas as pd
import sys


class MultipleJSONToCSV:
	"""An object that can convert multiple JSON files to a CSV file."""
	def __init__(self, source_path, destination_path):
		"""
		Initialize object's attributes.

		:param str path: Path to JSON files.
		:param str output: Output file name.
		"""
		self.source_path = source_path
		self.destination_path = destination_path

	def convert_json_to_csv(self):
		"""Convert multiple JSON files to a CSV file."""
		list_df = []
		for file in os.listdir(self.source_path):
			if file.endswith('.json'):
				source_file_path = self.source_path + file
				df = pd.read_json(source_file_path)
				list_df.append(df)
		all_df = pd.concat(list_df)
		all_df.to_csv(self.destination_path, index=False)
		print("All JSON files in {} are successfully converted into a CSV "
			  "file named {}".format(self.source_path, self.destination_path))


if __name__ == '__main__':
	json_path = sys.argv[1]  # Path to JSON files
	output_path = sys.argv[2]  # Output path
	converter = MultipleJSONToCSV(json_path, output_path)
	converter.convert_json_to_csv()
