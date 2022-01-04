from selenium import webdriver
from selenium.webdriver.common.by import
from selenium.webdriver.common.keys import

driver = webdriver.Chrome(executable_path="C:\\Users\eljin\\Downloads\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("http://www.amazon.com")
search = driver.find_element(By.ID, 'twotabsearchtextbox')
search.send_keys("Jordan 5", Keys.ENTER)


#print(driver.quit)
#driver.quit()
