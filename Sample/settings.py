import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print BASE_DIR


new_dir = os.path.join(BASE_DIR, 'Data', "log_data_2015_09_01" + ".csv")

print new_dir

