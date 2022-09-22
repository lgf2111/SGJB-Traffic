from os import listdir, walk, getcwd
from os.path import join


def find_latest(root_path):
    year_path = join(root_path, listdir(root_path)[-1])
    month_path = join(year_path, listdir(year_path)[-1])
    day_path = join(month_path, listdir(month_path)[-1])
    time_path = join(day_path, listdir(day_path)[-1])
    latest_path = "/".join(time_path.split("/")[-5:])
    return latest_path


def get_all_images(area):
    image_urls = []
    for root, dirs, files in walk(getcwd()):
        root = "/" + "/".join(root.split("/")[-5:])
        for f in files:
            if area == "Woodlands Causeway" and f == "4.png":
                image_urls.append("/".join([root, f]))
            elif area == "Tuas Second Link" and f == "10.png":
                image_urls.append("/".join([root, f]))
    return image_urls
