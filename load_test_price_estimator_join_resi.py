import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# locators

address = (By.XPATH, '//*[contains(@id, "AddressPicker-")]')
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
base_url = 'https://test.contact.co.nz/'
ALL_PLANS_PAGE_TITLE = "Contact Energy | Power Company | For Home | All Plans"

def wait_for_elem(x):
    time.sleep(x)

#  setting up the driver ( can put in setUp tearDown if there more than 1 tests)
# chrome_options = Options()
# chrome_options.add_argument('--headless')
driver = webdriver.Remote(
          command_executor='http://localhost:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.CHROME)
# driver = webdriver.Chrome(executable_path=chromePath)
driver.maximize_window()
driver.get(base_url+"residential/all-plans")
driver.implicitly_wait(60)  # seconds
t1 = time.time()
print('Test: -> Load Test Started!')
#  asserting the 'make changes' page title
assert ALL_PLANS_PAGE_TITLE in driver.title
basicPlan = popular = driver.find_element(*choosePlan)
basicPlan.click()
print("Basic Plan - Clicked!")
print("Broadband + Electricity Selected!")
#  no contact customer
no_customer = driver.find_element(*no_contact_customer)
no_customer.click()
print("No Contact Customer - Clicked!")

#  enter address
addressPicker = driver.find_element(*address)
addressPicker.send_keys(address)
wait_for_elem(5)
addressPicker.send_keys(Keys.ARROW_DOWN)
addressPicker.send_keys(Keys.RETURN)
print('Address Picked!')

wait_for_elem(3)
# No of people  >1
no_of_people = (By.CSS_SELECTOR, '.required-field > .radio:nth-child(2) > label')
no_of_people = driver.find_element(*no_of_people)
no_of_people.click()
print('Number of people Selected = 1')


wait_for_elem(2)
# No of people >2
no_of_people = (By.CSS_SELECTOR, '.required-field > .radio:nth-child(3) > label')
no_of_people = driver.find_element(*no_of_people)
no_of_people.click()
print('Number of people Selected  = 2')

wait_for_elem(2)
# No of people > 3
no_of_people = (By.CSS_SELECTOR, '.required-field > .radio:nth-child(4) > label')
no_of_people = driver.find_element(*no_of_people)
no_of_people.click()
print('Number of people Selected = 3')


wait_for_elem(2)
# No of people > 4
no_of_people = (By.CSS_SELECTOR, '.required-field > .radio:nth-child(5) > label')
no_of_people = driver.find_element(*no_of_people)
no_of_people.click()
print('Number of people Selected = 4')

wait_for_elem(2)
# No of people > 5
no_of_people = (By.CSS_SELECTOR, '.required-field > .radio:nth-child(6) > label')
no_of_people = driver.find_element(*no_of_people)
no_of_people.click()
print('Number of people Selected = 5+')


#  now selecting pipped gas and going from 5 users back to 1 user
driver.execute_script("window.scrollTo(1000,0);")
pippedGas = (By.XPATH  , "/html/body/div[2]/div[3]/div/form[2]/div[1]/div[2]")
wait_for_elem(3)
# adding pipped gas
pGas = driver.find_element(*pippedGas)
pGas.click()
print('Selected Piped gas')


# wait_for_elem(2)
# No of people > 4
no_of_people = (By.CSS_SELECTOR, '.required-field > .radio:nth-child(5) > label')
no_of_people = driver.find_element(*no_of_people)
no_of_people.click()
print('Number of people Selected = 4')

# wait_for_elem(2)
# No of people > 3
no_of_people = (By.CSS_SELECTOR, '.required-field > .radio:nth-child(4) > label')
no_of_people = driver.find_element(*no_of_people)
no_of_people.click()
print('Number of people Selected = 3')

# wait_for_elem(2)
# No of people >2
no_of_people = (By.CSS_SELECTOR, '.required-field > .radio:nth-child(3) > label')
no_of_people = driver.find_element(*no_of_people)
no_of_people.click()
print('Number of people Selected  = 2')

# wait_for_elem(3)
# No of people  >1
no_of_people = (By.CSS_SELECTOR, '.required-field > .radio:nth-child(2) > label')
no_of_people = driver.find_element(*no_of_people)
no_of_people.click()
print('Number of people Selected = 1')

total_time_taken = time.time() - t1

print("Price Estimator Load Test Completed with Success!!")
print(f"Total time taken: {round(total_time_taken,2)} Seconds!")
driver.close()

