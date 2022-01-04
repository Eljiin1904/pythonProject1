from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\\Users\eljin\\Downloads\\chromedriver.exe")
print(type(driver))
driver.implicitly_wait(5)

driver.get("https://www.amazon.com/")
#SignIn Button - Test #1
SignIn = driver.find_element(By.ID, 'nav-link-accountList-nav-line-1').click()
print("Test#1 Sign In: Passed!")

#Enter Email - Test #2
EmailID = driver.find_element_by_id('ap_email').send_keys("eljinwhitehead@gmail.com", Keys.TAB)
ContineButton = driver.find_element_by_id("continue").click()
print("Test#2 - Enter Email: Passed!")

driver.implicitly_wait(1)
#Enter Password - Test#3
PasswordID = driver.find_element_by_id('ap_password').send_keys("!3styx4$", Keys.ENTER)
#Password page options
#SignOnButton = driver.find_element(By.ID,'signInSubmit').click()
#ForgotPassButton = driver.find_element_by_id('auth-fpp-link-bottom').click()
print("Test#3 - Enter Password: Passed!")

#Main Page - Item Search - Test#4
search = driver.find_element(By.ID, 'twotabsearchtextbox')
search.send_keys("jordan mens air jordan 5 retro dd0587 600 raging bull 2021", Keys.ENTER)
print("Test#4 -Item Search: Passed!")
driver.implicitly_wait(1)

#Item Results Page - Test#5
ClickItem = driver.find_element_by_class_name('s-image').click()
#ClickItem.send_keys("s-image", Keys.ENTER)
print("Test#5 - Item Results Page: Passed!")

#ShoeSize Button - Dropdown - Test#6
ShoeSizeButton = driver.find_element_by_class_name('a-dropdown-prompt').click()
DropDownSize = driver.find_element_by_id('native_dropdown_selected_size_name_6').click()
print("Test#6 - ShoeSize Button: Passed!")

#AddToCartButton - Test#7
AddtoCart = driver.find_element_by_id('add-to-cart-button').click()
print("Test#7 - AddToCartButton: Passed!")

#AddToCartAction
AddFunction = driver.find_element_by_id('nav-cart').click()
print("Test#8 - Add Cart Action: Passed!")

driver.implicitly_wait(1)

#ProceedToCheckout - Test#8
ProceedToCheck = driver.find_element_by_class_name('a-button-input').click()
print("Test#8 - Check Out: Passed!")

##CheckOut - Test#9
#CheckOut = driver.find_element_by_class_name('a-button-inner')
#print("Test#9 - Checkout: Passed! ")
driver.quit()