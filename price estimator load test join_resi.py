import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import values
import testdata

# locators

# first page locators
change_plan = (By.XPATH, "//label[@for='UserJourneyAction_ChangePlan']")
acc_no = (By.ID, 'AccountNumber')
address = (By.XPATH, '//*[contains(@id, "AddressPicker-")]')
electricity = (By.CSS_SELECTOR, '.ELEC .cta-inner-wrapper')
no_of_people = (By.CSS_SELECTOR, '.required-field > .radio:nth-child(2) > label')
selectedPlan = (By.LINK_TEXT ,'POPULAR')
choosePlan = (By.LINK_TEXT ,'Choose plan')
emailaddress =(By.ID,  'Customer[CustomerInfo][EmailAddress]')
clickContinue =(By.LINK_TEXT ,'Continue')

# second page locators
title = (By.CSS_SELECTOR, '.list-items-4 > .radio:nth-child(2) > label')
first_name = (By.ID, 'Customer[CustomerInfo][FirstName]')
last_name = (By.ID, 'Customer[CustomerInfo][LastName]')
secound_page_emailaddress= (By.ID, 'Customer[CustomerInfo][EmailAddress]')
phone_number =(By.ID,  'Customer[CustomerInfo][PhoneNumber]')
birth_date = (By.ID, 'Customer[CustomerInfo][DateOfBirth]')
no_vulnerable_person = (By.XPATH, "//label[@for='Property[MedicalInfo][HasVulnerablePerson]_NO']")
no_medically_dependant_person = (By.XPATH, "//label[@for='Property[MedicalInfo][HasMedicalDependant]_NO']")
no_hazards = (By.XPATH, "//label[@for='Property[PropertyInfo][Hazards][]_No hazards']")
bank_acc = (By.ID, 'Promotion[DirectDebitDetails][BankAccountNumber]')
bill_monthly_period = (By.CSS_SELECTOR, '.tickbutton-list > .radio:nth-child(4) > label')
join_button = (By.CSS_SELECTOR,  '.btn-default')

adsl_plan = (By.CSS_SELECTOR, ".bb-plan-item:nth-child(6) .bb-plan-table .plain")
not_moving_house = (By.XPATH, "//label[@for='Property[MoveInfo][IsMovingHouse]_NO']")
no_contact_customer = (By.XPATH, "//label[@for='ExistingCustomer_NO'][contains(.,'No')]")
chaning_energ_supplier = (By.XPATH, "//label[contains(.,'Changing energy supplier')]")
no_broadband_provider = (By.XPATH, "//label[@for='Property[BroadbandInfo][HasBroadbandProvider]_NO']")
no_add_phoneline = (By.XPATH, "//label[@for='Property[BroadbandInfo][AddPhoneLine]_NO']")
modem_tobe_delivered_to_same_address = (By.XPATH, "//label[@for='Property[BroadbandInfo][ModemDeliveredToSameAddress]_YES']")
no_drivers_license = (By.XPATH, "//label[@for='Customer[HasDriversLicense]_NO']")

addr_sameas_postal_addr = (By.XPATH, "//label[@for='Property[PropertyInfo][AddressSameAsPostalAddress]_YES']")
bank_acc_ts_and_cs = (By.CSS_SELECTOR, '.col-xs-12 > .checkbox > label')
accept_general_ts_and_cs = (By.CSS_SELECTOR, '.row:nth-child(7) label')
broadband_tc_cs = (By.CSS_SELECTOR, ".row:nth-child(6) > .col-sm-12 label")
plan_ts_and_cs = (By.XPATH, "//div[@class='required-field checkbox form-group text-left has-feedback'][contains(.,'I accept the Terms and Conditions of the plan.')]")



def wait_for_elem(x):
    time.sleep(x)


#  setting up the driver ( can put in setUp tearDown if there more than 1 tests)
# chrome_options = Options()
# chrome_options.add_argument('--headless')
driver = webdriver.Remote(
          command_executor='http://localhost:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.CHROME)
# driver = webdriver.Chrome(executable_path=values.chromePath)
driver.maximize_window()
driver.get(values.base_url+"residential/all-plans")
driver.implicitly_wait(60)  # seconds
t1 = time.time()
print('Test: -> Load Test Started!')
#  asserting the 'make changes' page title
assert values.ALL_PLANS_PAGE_TITLE in driver.title
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
addressPicker.send_keys(testdata.address)
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

