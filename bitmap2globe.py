from time import sleep
from selenium import webdriver


URL = "https://web.archive.org/web/20180703195015id_/https://www.maptoglobe.com/#"
global driver
driver = webdriver.Edge()
print("Waiting for website to load...")
driver.get(URL)



def uploadFile(path_to_bitmap):
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
    uploadFile("C:/Users/abrah/Documents/GitHub/fantasy-globe/map.bmp")


    print("--------------------------------------------------------")
    sleep(120)



    def countDown(seconds, message):
        print(message)
        for i in range (seconds):
            print(seconds - i)
            sleep(1)

    countDown(10, "Program will terminate in")
    driver.close()
    print("program has terminated")

main()
