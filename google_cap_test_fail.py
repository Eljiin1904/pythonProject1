from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\eljin\\Downloads\\chromedriver.exe")
driver.get("http://www.google.com")

pagetitle = driver.title
print(pagetitle)
assert "amazon" in pagetitle

#print(driver.quit)
driver.quit()
