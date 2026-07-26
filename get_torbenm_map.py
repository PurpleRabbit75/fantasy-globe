import requests

session = requests.Session()
# use the exact field names you captured from DevTools
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

form_request = session.post(
    "https://topps.diku.dk/torbenm/maps.msp",
    data=params
)
form_request.raise_for_status()


img_response = session.get(f"https://topps.diku.dk/torbenm/Maps/Map-{params["seed"][-3:]}.bmp")
img_response.raise_for_status()

with open("map.bmp", "wb") as f:
    f.write(img_response.content)



# seed=1111111&projection=M&width=500&colourmap=Olsson.col&height=250&shading=&zoom=1&outline=&lati=&polar=&longi=&water=-0.02&grid=none&what=Make+map