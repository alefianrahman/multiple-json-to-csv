# Multiple JSON to CSV Converter
A file converter that converts multiple JSON files into a CSV file. 

## Tutorial: How to Use the Script. 
1. Clone the GitHub repository into your local machine/terminal.\
```git clone https://github.com/alefianrahman/multiple-json-to-csv.git``` (If using HTTPS)\
```git clone git@github.com:alefianrahman/multiple-json-to-csv.git``` (If using SSH)
2. Go to the ```script``` folder in the ```multiple-json-to-csv``` directory.
3. The script ```multiple_json_to_csv.py``` receives 2 arguments, the path to JSON files and the output filename. The command format in terminal:\
```python multiple_json_to_csv.py /path/to/json/files output_filename.csv```
4. As a demonstration, we can try to test the script by using the sample files in the ```samples``` folder. Suppose we want to combine all JSON files in the ```samples``` folder and generate a CSV file named ```output.csv```. In this case, we have cloned the repository in the home directory so that the path will start with ```~```. To combine the JSON files, we just need to type this command in terminal in the ```script``` folder: \
```python multiple_json_to_csv.py ~/multiple_json_to_csv/samples/ output.csv``` 

## Guidance on the JSON files
The JSON files that will be converted should consist fields with the same name and there is no nested (record) fields. For example, here are the proper formats: \
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
  "continent": "Europe"
  "country": "UK", 
  "city": "London", 
  "population": 8908081, 
  "updated_at": "2020-05-21 19:00:00"
}]
```
The JSON files can also consist more than one records as long as they have the same field name like:
```
[
{
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
  "population": 174883", 
  "updated_at": "2020-03-02 00:00:00"
}
]
```
Note: all the above JSON files are just samples and might not represent the actual data. 

## Authors
Alfian Rahman (https://linkedin.com/in/alefianrahman)
