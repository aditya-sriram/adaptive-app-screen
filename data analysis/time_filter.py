import utils
import pandas as pd

min_duration = 5
in_folder_path = "C:/Users/adity/Desktop/School/Adaptive App Screen/datasets/UbiqLog4UCI/ApplicationData/14-07--10-17-04"
out_folder_dir = "C:/Users/adity/Desktop/School/Adaptive App Screen/datasets/UbiqLog4UCI/TimeFilteredData"

out_folder_path = utils.init_output(out_folder_dir)


def time_filter(filename):
    df = pd.read_json("{}/{}".format(in_folder_path, filename))

    Start = pd.to_datetime(df.Start, format="%m-%d-%Y %H:%M:%S")
    End = pd.to_datetime(df.End, format="%m-%d-%Y %H:%M:%S")

    filtered_df = df[(pd.to_timedelta(End - Start).dt.total_seconds() > min_duration*60)]
    print(len(filtered_df.ProcessName.unique()))
    filtered_df.to_json("{}/{}".format(out_folder_path, filename))

utils.map_filenames(in_folder_path, time_filter)
