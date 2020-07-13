import os
import pandas as pd
import sys


class MultipleJSONtoCSV:
	"""An object that can convert multiple JSON files to a CSV file."""
	def __init__(self, path, output):
		"""
		Initialize object's attributes.

		:param str path: Path to JSON files.
		:param str output: Output file name.
		"""
		self.path = path
		self.output = output

	def convert_json_to_csv(self):
		"""Convert multiple JSON files to a CSV file."""
		list_df = []
		for file in os.listdir(self.path):
			if file.endswith('.json'):
				file_path = self.path + file
				df = pd.read_json(file_path)
				list_df.append(df)
		all_df = pd.concat(list_df)
		all_df.to_csv(self.output, index=False)
		print("All JSON files in {} are successfully converted into a CSV "
			  "file named {}".format(self.path, self.output))


if __name__ == '__main__':
	json_path = sys.argv[1]  # Path to JSON files
	output_name = sys.argv[2]  # Output filename
	obj = MultipleJSONtoCSV(json_path, output_name)
	obj.convert_json_to_csv()
