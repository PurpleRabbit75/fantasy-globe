import time
from selenium import webdriver
import requests
from bitmap2globe import *


def get_params_from_user():
    params = {
        "seed": "1111111",
        "projection": "M",
        "width": "500",
        "colourmap": "Olsson.col",
        "height": "250",
        "shading": "",
        "zoom": "1",
        "outline": "",
        "lati": "",
        "polar": "",
        "longi": "",
        "water": "-0.02",
        "grid": "none",
        "what": "Make map"
    }
    return params


def get_bitmap(params):
    session = requests.Session()

    request_map_regen = session.post("https://topps.diku.dk/torbenm/maps.msp",data=params)
    get_img_response = session.get(f"https://topps.diku.dk/torbenm/Maps/Map-{params["seed"][-3:]}.bmp")


    request_map_regen.raise_for_status()
    sleep(0.5)
    get_img_response.raise_for_status()


    with open(f"Map-{params["seed"][-3:]}.bmp", "wb") as f:
        f.write(get_img_response.content)

    return f"Map-{params["seed"][-3:]}.bmp"
    









def main():
    params = get_params_from_user()
    bitmap_path = get_bitmap(params)
