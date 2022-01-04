from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\eljin\\Downloads\\chromedriver.exe")
print(type(driver))
driver.implicitly_wait(5)

driver.get("https://www.nike.com/")
search = driver.find_element(By.ID, 'twotabsearchtextbox')
search.send_keys("jordan 5", Keys.ENTER)

expected_text = '"jordan 5"'
actual_text = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

assert expected_text == actual_text, f"Error. Expected text: {expected_text}, but actual text: {actual_text}"

driver.quit()
