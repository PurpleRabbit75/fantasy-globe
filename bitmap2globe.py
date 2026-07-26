import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#import webbrowser 
import urllib


URL = "https://web.archive.org/web/20180703195015id_/https://www.maptoglobe.com/#"
global driver
driver = webdriver.Edge()
print("Waiting for website to load...")
driver.get(URL)



def uploadFile():
    driver.execute_script('$("#imagesContext").trigger("click");')

    fileUploadButton = driver.find_element("id", "surfaceFile")
    fileUploadButton.send_keys("C:/Users/abrah/Documents/GitHub/fantasy-globe/map.bmp")


uploadFile()


driver.execute_script('$("[data-remodal-id=modalUpload]").remodal().open();')

time.sleep(0.5)

driver.execute_script("""
    var modal = $('[data-remodal-id="modalUpload"]');  // Get the modal element
    modal.trigger('confirmation');  // Manually trigger the 'confirmation' event
""")



print("--------------------------------------------------------")
time.sleep(120)



def countDown(seconds, message):
    print(message)
    for i in range (seconds):
        print(seconds - i)
        time.sleep(1)

countDown(10, "Program will terminate in")
driver.close()
print("program has terminated")