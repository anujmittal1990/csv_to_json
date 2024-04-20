					
import pandas as pd
import json

class csv_to_json:
    def __init__(self, master_file, detail_file):
        self.master_file = master_file
        self.detail_file = detail_file


    def read_files(self):
        # Reading master CSV file
        master_df = pd.read_csv(self.master_file)
        # Reading detail CSV file
        detail_df = pd.read_csv(self.detail_file)
        # Converting master data to JSON
        master_json = master_df.to_dict(orient='records')
        # Converting detail data to JSON
        detail_json = detail_df.to_dict(orient='records')
        # Merging into a dictionary
        self.json_data = {
            "emp_data": master_json,
            "dept_data": detail_json
        }
        return self.json_data
     
    def save_file(self):
        # Saving data to a JSON file
        with open('data.json', 'w') as f:
            json.dump(self.json_data, f, indent=4)



# Calling csv_to_json and their methods
json_converter = csv_to_json('files/emp.csv', 'files/dept.csv')
json_data = json_converter.read_files()
json_converter.save_file()
print("JSON data saved to 'data.json'.")
