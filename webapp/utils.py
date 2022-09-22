from os import listdir
from os.path import join


def find_latest(root_path):
    year_path = join(root_path, listdir(root_path)[-1])
    month_path = join(year_path, listdir(year_path)[-1])
    day_path = join(month_path, listdir(month_path)[-1])
    time_path = join(day_path, listdir(day_path)[-1])
    latest_path = time_path[time_path.find("collections") :]
    return latest_path
