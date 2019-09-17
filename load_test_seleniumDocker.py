"""
to run:
1-run docker-compose up (from where the yml file is located)
2-run docker-compose scale chrome=4
3- run the test in terminal
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# locators

address_field = (By.XPATH, '//*[contains(@id, "AddressPicker-")]')
no_of_people = (By.CSS_SELECTOR, '.required-field > .radio:nth-child(2) > label')
selectedPlan = (By.LINK_TEXT ,'POPULAR')
choosePlan = (By.LINK_TEXT ,'Choose plan')
emailaddress =(By.ID,  'Customer[CustomerInfo][EmailAddress]')
no_contact_customer = (By.XPATH, "//label[@for='ExistingCustomer_NO'][contains(.,'No')]")

# test data
address = '2 Burton Way, Bishopdale, Nelson 7011'
emailaddress = 'AutoTest@contact.co.nz'

# path to chrome driver location
chromePath = '/Users/test/Desktop/p/chromedriver'
#  base url
base_url = 'https://www.google.com'
GoogleHomePage_TITLE = "Google"

def wait_for_elem(x):
    time.sleep(x)

#  setting up the driver ( can put in setUp tearDown if there more than 1 tests)
# chrome_options = Options()
# chrome_options.add_argument('--headless')
driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',desired_capabilities=DesiredCapabilities.CHROME)
# driver = webdriver.Chrome(executable_path=chromePath)
driver.maximize_window()
driver.get(base_url")
driver.implicitly_wait(60)  # seconds
t1 = time.time()
print('Test: -> Load Test Started!')
#  asserting the 'Google' page title
assert GoogleHomePage_TITLE in driver.title

total_time_taken = time.time() - t1

print("XYZ Load Test Completed with Success!!")
print(f"Total time taken: {round(total_time_taken,2)} Seconds!")
driver.close()

