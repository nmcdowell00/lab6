import requests
from bs4 import BeautifulSoup
from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
from webdriver_manager.chrome import ChromeDriverManager

print("sample test case started")  
#driver = webdriver.Chrome("/Users/natemcdowell/Desktop/chromedriver-2")  
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
#driver=webdriver.firefox()  
#driver=webdriver.ie()  
#maximize the window size  
driver.maximize_window()  
#navigate to the url  
driver.get("https://find.pitt.edu/")  
#identify the Google search text box and enter the value  
#driver.find_element("search").send_keys("Nate")
#driver.find_element("name", "search").

search_box = driver.find_element("name", "search")
search_box.send_keys('Nate')
time.sleep(3)  

#click on the Google search button  
button = driver.find_element("id","btnSearch")
button.send_keys(Keys.ENTER)  

# this seems to be working but I just cant get the text w/in the element to output 
results = driver.find_element("id", "resultsInfo")
print(results) 
print(results.text) # this is supposed to output the text but it cant find it

print(driver.current_url)
time.sleep(10)  
#close the browser  
driver.close()  
print("sample test case successfully completed")  