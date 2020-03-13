from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


#usn = input("Enter your USN: ")
usn = '1da17im006'

caps = DesiredCapabilities().CHROME
#caps["pageLoadStrategy"] = "normal"  #  complete
caps["pageLoadStrategy"] = "eager"  #  interactive
#caps["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(desired_capabilities=caps, executable_path=r'C:\Users\Amogh\Desktop\chromedriver.exe')

driver.get('http://results.drait.in/')
searchbox = driver.find_element_by_xpath('//*[@id="usn"]')
searchbox.send_keys(usn)

searchButton = driver.find_element_by_xpath('//*[@id="ugpg"]/option[2]')
searchButton.click()

searchButton = driver.find_element_by_xpath('//*[@id="submit"]')
searchButton.click()