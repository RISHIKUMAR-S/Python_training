from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
print("sample test case started")
driver = webdriver.Chrome(r"C:\Users\Rishi\Desktop\chromedriver.exe")
#maximize the window size
driver.maximize_window()
#navigate to the url
driver.get("https://www.youtube.com/")
time.sleep(5)
#identify the Google search text box and enter the value
#find = driver.find_element("xpath",'//*[@id="input"]/html/body/ntp-app//div/ntp-realbox//div/input')
findvideo = driver.find_element(By.NAME,"search_query")
findvideo.click()
findvideo.clear()
findvideo.send_keys("javatpoint")
findvideo.send_keys(Keys.ENTER)
time.sleep(10)
#close the browser
driver.close()
#print("sample test case successfully completed")
