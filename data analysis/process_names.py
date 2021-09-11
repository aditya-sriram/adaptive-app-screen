import pandas as pd

filepath = "C:/Users/adity/Desktop/School/Adaptive App Screen/datasets/UbiqLog4UCI/Labelled/03-08--20-45-03/10_M.json"
df = pd.read_json(filepath)

process_names = df["ProcessName"].unique()
pd.DataFrame({"ProcessName": process_names}).to_json("./outputs/process_names.json")