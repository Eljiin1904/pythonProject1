from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\eljin\\Downloads\\chromedriver.exe")
print(type(driver))
driver.implicitly_wait(5)

driver.get("https://www.nike.com/launch")
ShoeID = driver.find_element_by_class_name('image-component mod-image-component u-full-width').click()
