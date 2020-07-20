# Multiple JSON to CSV Converter
A file converter that converts multiple JSON files into a CSV file. 

## Tutorial: How to Use the Script
1. Clone this GitHub repository into your local machine using ```git``` command: \
```git clone https://github.com/alefianrahman/multiple-json-to-csv.git``` (If using HTTPS)\
```git clone git@github.com:alefianrahman/multiple-json-to-csv.git``` (If using SSH)
2. Go to the ```multiple-json-to-csv``` directory.
3. The script ```multiple_json_to_csv.py``` receives 2 arguments, the path to JSON files and the output path. The command format in terminal:\
```python multiple_json_to_csv.py /path/to/json/files output/path/file.csv```
4. As a demonstration, we can test the script using the sample files in the ```samples``` folder. Suppose we want to combine all JSON files in the ```samples``` folder and generate a CSV file named ```output.csv```. To combine the JSON files, we just need to type this command in terminal: \
```python multiple_json_to_csv.py samples/ output/output.csv``` 

## Guidance on the JSON Files
The JSON files that will be converted should consist fields with the same key name and there is no nested (record) fields. For example, here are the proper formats: \
File 1
```
[{
  "continent": "Asia", 
  "country": "Indonesia", 
  "city": "Jakarta",
  "population": 10770487, 
  "updated_at": "2020-02-01 12:00:00"
}]
``` 
File 2 
```
[{
  "continent": "Europe",
  "country": "UK", 
  "city": "London", 
  "population": 8908081, 
  "updated_at": "2020-05-21 19:00:00"
}]
```
The JSON files can also consist more than one records as long as they have the same field name. For example:
```
[{
  "continent": "Africa", 
  "country": "Egypt", 
  "city": "Cairo", 
  "population": 9500000, 
  "updated_at": "2020-06-17 04:00:00"
}, 
{
  "continent": "Europe", 
  "country": "Belgium", 
  "city": "Brussels", 
  "population": 174883, 
  "updated_at": "2020-03-02 00:00:00"
}]
```
Note: all the above JSON files are just samples and might not represent the actual data. 

## Authors
Alfian Rahman (https://linkedin.com/in/alefianrahman)
