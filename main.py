from time import sleep
from selenium import webdriver
import requests
import os


def get_params_from_user():
    map_params = {
        "seed": "1111111",
        "projection": "M",
        "width": "500",
        "colourmap": "Mars.col",
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

    browser = "edge" # pick from "chrome", "firefox", "edge", safari should also work, but I can't test for it
    renderer = "archive.org" # pick from "archive.org" or "woowspace.com"
    timeout = 120 # Amount of time in seconds before the program terminates
    return [map_params, browser, renderer, timeout]


def get_bitmap(map_params):
    session = requests.Session()

    request_map_regen = session.post("https://topps.diku.dk/torbenm/maps.msp",data=map_params)
    get_img_response = session.get(f"https://topps.diku.dk/torbenm/Maps/Map-{map_params["seed"][-3:]}.bmp")


    request_map_regen.raise_for_status()
    sleep(0.5)
    get_img_response.raise_for_status()


    with open(f"Map-{map_params["seed"][-3:]}.bmp", "wb") as f:
        f.write(get_img_response.content)

    return os.path.realpath(f"Map-{map_params["seed"][-3:]}.bmp")
    


def render_file(driver, path_to_bitmap):
    driver.execute_script('$("#imagesContext").trigger("click");')

    fileUploadButton = driver.find_element("id", "surfaceFile")
    fileUploadButton.send_keys(path_to_bitmap)

    driver.execute_script('$("[data-remodal-id=modalUpload]").remodal().open();')

    sleep(0.5)

    driver.execute_script("""
        var modal = $('[data-remodal-id="modalUpload"]');  // Get the modal element
        modal.trigger('confirmation');  // Manually trigger the 'confirmation' event
    """)






def main():
    map_params, browser, renderer, timeout = get_params_from_user()
    bitmap_path = get_bitmap(map_params)

    if (browser == "edge"):
        driver = webdriver.Edge()
    elif (browser == "firefox"):
        driver = webdriver.Firefox()
    elif (browser == "chrome"):
        driver = webdriver.Chrome()
    else:
        raise ValueError

    if (renderer == "archive.org"):
        URL = "https://web.archive.org/web/20180703195015id_/https://www.maptoglobe.com/#"
    elif (renderer == "woowspace.com"):
        URL = "https://woowspace.com/MapToGlobe.html"
    else:
        raise ValueError

    driver.get(URL)
    render_file(driver, bitmap_path)


    sleep(timeout)

    def countDown(seconds, message):
        print(message)
        for i in range (seconds):
            print(seconds - i)
            sleep(1)

    countDown(10, "Program will terminate in")
    driver.close()
    print("program has terminated")


main()