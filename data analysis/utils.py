import os
from datetime import datetime

def read(filepath, fn):
    if not os.path.isfile(filepath):
        print('File does not exist.')
    else:
        with open(filepath, encoding="utf8") as f:
            content = f.read().splitlines()

        return filter(fn, content)

def map_filenames(in_folder_path, func):
    for filename in os.listdir(in_folder_path)[:1]:
        func(filename)

def init_output(out_folder_dir):
    now = datetime.now()
    out_folder_path = "{}/{}".format(out_folder_dir, now.strftime("%d-%m--%H-%M-%S"))
    os.mkdir(out_folder_path)
    return out_folder_path
