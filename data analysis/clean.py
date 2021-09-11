import pandas as pd
import os
import pathlib
import json
from datetime import datetime
import utils

in_folder_path = "C:/Users/adity/Desktop/School/Adaptive App Screen/datasets/UbiqLog4UCI/UbiqLog4UCI"
out_folder_path = "C:/Users/adity/Desktop/School/Adaptive App Screen/datasets/UbiqLog4UCI/ApplicationData"

utils.init_output(out_folder_path)

def is_application_entry(entry):
    try:
        data = json.loads(entry)
        return "Application" in data
    except:
        print("ERROR:", entry)

def remove_application_label(entry):
    data = json.loads(entry)
    return data["Application"]

def combine_columns(df):
    pass

for user in os.listdir(in_folder_path):

    user_data = []

    for day in os.listdir("{}/{}".format(in_folder_path, user)):
        if pathlib.Path(day).suffix == ".txt":
            application_entries = utils.read("{}/{}/{}".format(in_folder_path, user, day), is_application_entry)
            without_label_application_entries = map(remove_application_label, application_entries)
            user_data += without_label_application_entries
    
    df = pd.DataFrame(user_data)
    df.to_json("{}/{}.json".format(out_folder_path, user))
    print(user)