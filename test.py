from selenium import webdriver
import requests
x
print(response.url)
response.replace(url='https://techcrunch.com/search/heartbleed#stq=heartbleed&stp=2')
print(response.url)

next = self.driver.find_element(By.XPATH,"//a[@class='page-link next']")
nextpage = next.get_attribute("href")
yield scrapy.Request(url=nextpage, dont_filter=False)