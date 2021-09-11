import utils
import pandas as pd
import numpy as np

in_folder_path = "C:/Users/adity/Desktop/School/Adaptive App Screen/datasets/UbiqLog4UCI/TimeFilteredData/18-07--08-06-56"
out_folder_dir = "C:/Users/adity/Desktop/School/Adaptive App Screen/datasets/UbiqLog4UCI/Labelled"

out_folder_path = utils.init_output(out_folder_dir)


def label(filename):
    df = pd.read_json("{}/{}".format(in_folder_path, filename))
    df["Start"] = pd.to_datetime(df.Start)
    
    df["Day"] = df.Start.dt.dayofweek
    df["Hour"] = df.Start.dt.hour
    df["Label"] = 1

    del df["Start"]
    del df["End"]

    rows = df.iterrows()
    for _, row in rows:

        process_names = df[(df.ProcessName != row.ProcessName) | ((df.Hour != row.Hour) & (df.Day != row.Day))]["ProcessName"].unique()
        
        for process_name in process_names:
            df = df.append({"ProcessName": process_name, "Day": row["Day"], "Hour": row["Hour"], "Label": 0}, ignore_index=True)

    df[["ProcessName", "Day", "Hour", "Label"]].to_json("{}/{}".format(out_folder_path, filename))
    print(df)


utils.map_filenames(in_folder_path, label)

