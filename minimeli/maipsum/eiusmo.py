from selenium import webdriver

driver = webdriver.Chrome()
create = driver.find_element(By.XPATH, "//div[@class='create-button-wrapper']/button")  
