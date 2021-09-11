import utils
import pandas as pd
import numpy as np

in_folder_path = "C:/Users/adity/Desktop/School/Adaptive App Screen/datasets/UbiqLog4UCI/TimeFilteredData/18-07--08-06-56"
out_folder_dir = "C:/Users/adity/Desktop/School/Adaptive App Screen/datasets/UbiqLog4UCI/Labelled"

out_folder_path = utils.init_output(out_folder_dir)


def label(filename):
    df = pd.read_json("{}/{}".format(in_folder_path, filename))
    df["Start"] = pd.to_datetime(df.Start)
    
    new_df = pd.DataFrame({
        "Day": np.repeat(np.arange(1,8), 24),
        "Hour": np.repeat([np.arange(0,24)], 7, axis=0).flatten(),
        "Label": 0,
        "ProcessName": None
    })
    
    print(new_df)


utils.map_filenames(in_folder_path, label)
