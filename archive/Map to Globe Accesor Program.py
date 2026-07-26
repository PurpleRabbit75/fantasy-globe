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



# ImagesButton = driver.find_element("id", "imagesContext")
# ImagesButton.click()
def uploadFile():
    driver.execute_script('$("#imagesContext").trigger("click");')

    fileUploadButton = driver.find_element("id", "surfaceFile")
    fileUploadButton.send_keys("C:/Users/abrah/Desktop/Auto-Generated Maps/AutomatedMapTest.bmp")
'''
#Selector: body > div.remodal-wrapper.remodal-is-opened > div > button.remodal-confirm
#xpath: /html/body/div[11]/div/button[2]
# confirmButton = driver.find_element(By.CSS_SELECTOR, "button[data-remodal-action='confirm'].remodal-confirm")
# driver.execute_script("arguments[0].click();", confirmButton)
# print("waiting 5 seconds for button to load...")
#time.sleep(15)
# print(confirmButton.is_displayed())  # Check visibility
# print(confirmButton.is_enabled())    # Check if it's enabled
# # print(confirmButton)
# confirmButton.click()
#WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-remodal-action='confirm']"))).click()'''

uploadFile()



driver.execute_script('$("[data-remodal-id=modalUpload]").remodal().open();')

# driver.execute_script("""
#     var modal = $('[data-remodal-id="modalUpload"]');
#     var confirmButton = modal.find('.remodal-confirm');
#     //if (!confirmButton.prop('disabled')) {
#     confirmButton.click();
#     //}
# """)

# Trigger the 'confirmation' event on the modal
driver.execute_script("""
    var modal = $('[data-remodal-id="modalUpload"]');  // Get the modal element
    modal.trigger('confirmation');  // Manually trigger the 'confirmation' event
""")




# print(1, "--------------------------------------------------------")
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "div.remodal-wrapper.remodal-is-opened"))
# )



# print(2, "--------------------------------------------------------")
# altxpath = "//button[@data-remodal-action='confirm']"
# ok = driver.find_element("xpath", "//button[@data-remodal-action='confirm' and contains(@class, 'remodal-confirm')]")

# print("Enabled:", ok.is_enabled())
# print("Displayed:", ok.is_displayed())
# modal = driver.find_element(By.CSS_SELECTOR, "div.remodal-wrapper.remodal-is-opened")

# #ok_button = driver.find_element(By.XPATH, "//button[@data-remodal-action='confirm']")
# ok_button = ok
# print("CSS Display:", str(driver.execute_script("return arguments[0].style.display;", ok_button)))
# print("CSS Visibility:", str(driver.execute_script("return arguments[0].style.visibility;", ok_button)))
# print("Opacity:", driver.execute_script("return window.getComputedStyle(arguments[0]).opacity;", ok_button))
# driver.execute_script('$(".remodal").remodal().open();')

# parent_element = ok_button.find_element(By.XPATH, "..")  # Parent element
# print("Parent CSS Display:", driver.execute_script("return arguments[0].style.display;", parent_element))
# print("Parent CSS Visibility:", driver.execute_script("return arguments[0].style.visibility;", parent_element))
# print("Parent Opacity:", driver.execute_script("return window.getComputedStyle(arguments[0]).opacity;", parent_element))

# grandparent_element = ok_button.find_element(By.XPATH, "..")  # grandParent element
# print("grandParent CSS Display:", driver.execute_script("return arguments[0].style.display;", grandparent_element))
# print("grandParent CSS Visibility:", driver.execute_script("return arguments[0].style.visibility;", grandparent_element))
# print("grandParent Opacity:", driver.execute_script("return window.getComputedStyle(arguments[0]).opacity;", grandparent_element))

# print("Modal displayed:", modal.is_displayed())
# print("Modal CSS Display:", driver.execute_script("return arguments[0].style.display;", modal))
# print("Modal CSS Visibility:", driver.execute_script("return arguments[0].style.visibility;", modal))
# print("Modal Opacity:", driver.execute_script("return window.getComputedStyle(arguments[0]).opacity;", modal))



# print(3, "--------------------------------------------------------")
# while (ok.is_enabled() == False or ok.is_displayed() == False):
#     time.sleep(1)
#     output = ""
#     if(ok.is_enabled() == False):
#         output = "Button is disabled; "
#     if (ok.is_displayed() == False):
#         output = output + "Button is not displayed; "
#     print(output)
# if (ok.is_enabled() and ok.is_displayed()):
#     ok.click()
#     ok.submit()
#     print("Button was clicked [ii]")



print(4, "--------------------------------------------------------")
time.sleep(120)











def countDown(seconds, message):
    print(message)
    for i in range (seconds):
        print(seconds - i)
        time.sleep(1)

countDown(10, "Program will terminate in")
driver.close()
print("program has terminated")