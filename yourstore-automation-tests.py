import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# Function to create folder structure by date, time, and test case
def evidence(name_case):
    current_date = datetime.now().strftime("%Y%m%d")  # Formato de fecha: YYYYMMDD
    current_time = datetime.now().strftime("%H%M%S")  # Formato de hora: HHMMSS
    base_folder = os.path.join("evidence", current_date, current_time, name_case)
    
    if not os.path.exists(base_folder):
        os.makedirs(base_folder)
    
    return base_folder

# Function to take a screenshot
def screenshot(driver, test_case_folder, screenshot_name):
    file_path = os.path.join(test_case_folder, f"{screenshot_name}.png")
    driver.save_screenshot(file_path)

def wait_and_click(driver, locator):
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(locator))
    element.click()

def wait_and_send_keys(driver, locator, keys):
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
    element.send_keys(keys)

#Test cases

def user_registration():
    test_case_name = "New user registration"
    test_case_folder = evidence(test_case_name)

    user_first_name = "Lena"
    user_last_name = "Rivel"
    user_email = "lenarivel@yopmail.com"
    user_phone_number = "1111112222"
    user_password = "abc123"

    driver = webdriver.Chrome()
    driver.maximize_window()

    url = "http://opencart.abstracta.us/"
    driver.get(url)

    wait_and_click(driver, (By.CLASS_NAME, "caret"))
    time.sleep(1)
    screenshot(driver, test_case_folder, "access to the registration section")
    wait_and_click(driver, (By.PARTIAL_LINK_TEXT, "Register"))

    wait_and_send_keys(driver, (By.ID, "input-firstname"), user_first_name)
    wait_and_send_keys(driver, (By.ID, "input-lastname"), user_last_name)
    wait_and_send_keys(driver, (By.ID, "input-email"), user_email)
    wait_and_send_keys(driver, (By.ID, "input-telephone"), user_phone_number)
    wait_and_send_keys(driver, (By.ID, "input-password"), user_password)
    wait_and_send_keys(driver, (By.ID, "input-confirm"), user_password)

    wait_and_click(driver, (By.NAME, "agree"))

    screenshot(driver, test_case_folder, "complete registration form")
    time.sleep(1)
    wait_and_click(driver, (By.CSS_SELECTOR, "input[value='Continue']"))

    if "Congratulations! Your new account has been successfully created!" in driver.page_source:
        print("Passed: The registration was completed successfully.")
    else:
        print("Failed: There was an issue during the registration.")

    screenshot(driver, test_case_folder, "registration result")
    time.sleep(1)
    driver.quit()

def existing_user_registration():
    test_case_name = "Existing user registration"
    test_case_folder = evidence(test_case_name)

    user_first_name = "Lena"
    user_last_name = "Rivel"
    user_email = "lenarivel@yopmail.com"
    user_phone_number = "1111112222"
    user_password = "abc123"

    driver = webdriver.Chrome()
    driver.maximize_window()

    url = "http://opencart.abstracta.us/"
    driver.get(url)

    wait_and_click(driver, (By.CLASS_NAME, "caret"))
    time.sleep(1)
    screenshot(driver, test_case_folder, "access to the registration section")
    wait_and_click(driver, (By.PARTIAL_LINK_TEXT, "Register"))

    wait_and_send_keys(driver, (By.ID, "input-firstname"), user_first_name)
    wait_and_send_keys(driver, (By.ID, "input-lastname"), user_last_name)
    wait_and_send_keys(driver, (By.ID, "input-email"), user_email)
    wait_and_send_keys(driver, (By.ID, "input-telephone"), user_phone_number)
    wait_and_send_keys(driver, (By.ID, "input-password"), user_password)
    wait_and_send_keys(driver, (By.ID, "input-confirm"), user_password)
    wait_and_click(driver, (By.NAME, "agree"))

    screenshot(driver, test_case_folder, "complete registration form")
    time.sleep(1)
    wait_and_click(driver, (By.CSS_SELECTOR, "input[value='Continue']"))

    if "Warning: E-Mail Address is already registered!" in driver.page_source:
        print("Passed: Unable to register, user already exists")
    else:
        print("Failed: Registration was successful with an existing user")

    screenshot(driver, test_case_folder, "registration result")
    time.sleep(1)
    driver.quit()

def login():
    test_case_name = "Login with an existing user"
    test_case_folder = evidence(test_case_name)

    user_email = "lenarivel@yopmail.com"
    user_password = "abc123"

    driver = webdriver.Chrome()
    driver.maximize_window()

    url = "http://opencart.abstracta.us/"
    driver.get(url)

    wait_and_click(driver, (By.CLASS_NAME, "caret"))
    time.sleep(1)
    screenshot(driver, test_case_folder, "access to the login section")
    wait_and_click(driver, (By.PARTIAL_LINK_TEXT, "Login"))
    

    wait_and_send_keys(driver, (By.ID, "input-email"), user_email)
    wait_and_send_keys(driver, (By.ID, "input-password"), user_password)
    time.sleep(1)

    screenshot(driver, test_case_folder, "complete login form")
    wait_and_click(driver, (By.CSS_SELECTOR, "input[value='Login']"))

    url_esperada = "https://opencart.abstracta.us/index.php?route=account/account"

    if driver.current_url == url_esperada:
        print("Passed: The login was redirected to the expected URL.")
    else:
        print(f"Failed: There was an issue during the login. Current URL: {driver.current_url}")

    screenshot(driver, test_case_folder, "login result")
    time.sleep(1)
    driver.quit()

def login_unregistered_user():
    test_case_name = "Login with an unregistered user"
    test_case_folder = evidence(test_case_name)

    user_email = "noexiste@yopmail.com"
    user_password = "abc123"

    driver = webdriver.Chrome()
    driver.maximize_window()

    url = "http://opencart.abstracta.us/"
    driver.get(url)

    wait_and_click(driver, (By.CLASS_NAME, "caret"))
    time.sleep(1)
    screenshot(driver, test_case_folder, "access to the login section")
    wait_and_click(driver, (By.PARTIAL_LINK_TEXT, "Login"))

    wait_and_send_keys(driver, (By.ID, "input-email"), user_email)
    wait_and_send_keys(driver, (By.ID, "input-password"), user_password)

    screenshot(driver, test_case_folder, "complete login form")
    time.sleep(1)

    wait_and_click(driver, (By.CSS_SELECTOR, "input[value='Login']"))

    # url_esperada = "https://opencart.abstracta.us/index.php?route=account/account"

    if "Warning: No match for E-Mail Address and/or Password." in driver.page_source:
        print("Passed: Couldn't log in, user not registered.")
    else:
        print("Failed: Logged in with an unregistered user.")

    screenshot(driver, test_case_folder, "login result")
    time.sleep(1)
    driver.quit()

def guest_checkout():
    test_case_name = "Guest checkout"
    test_case_folder = evidence(test_case_name)
    device_name = "Palm Treo Pro"

    driver = webdriver.Chrome()
    driver.maximize_window()

    url = "http://opencart.abstracta.us/"
    driver.get(url)
    
    wait_and_click(driver, (By.PARTIAL_LINK_TEXT, "Phones & PDAs"))

    screenshot(driver, test_case_folder, "Mobile Dashboard")

    wait_and_click(driver, (By.PARTIAL_LINK_TEXT, "Phones & PDAs"))
    wait_and_click(driver, (By.PARTIAL_LINK_TEXT, device_name))
    wait_and_click(driver, (By.XPATH,'//button[text()="Add to Cart"]'))

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-success")))

    screenshot(driver, test_case_folder, "The item was added to the cart")

    wait_and_click(driver, (By.ID, "cart-total"))
    wait_and_click(driver, (By.XPATH, "//*[@id='cart']/ul/li[2]/div/p/a[1]/strong"))

    screenshot(driver, test_case_folder, "Cart details")

    wait_and_click(driver, (By.CSS_SELECTOR, 'a[href="https://opencart.abstracta.us:443/index.php?route=checkout/checkout"].btn.btn-primary'))

    wait_and_click(driver, (By.CSS_SELECTOR, 'input[value="guest"]'))

    screenshot(driver, test_case_folder, "Continue as a guest.")

    wait_and_click(driver, (By.CSS_SELECTOR, 'input[value="Continue"]'))

    #billing details
    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, 'button-guest')))

    wait_and_send_keys(driver, (By.ID, "input-payment-firstname"), "Juana")
    wait_and_send_keys(driver, (By.ID, "input-payment-lastname"), "Ruiz")
    wait_and_send_keys(driver, (By.ID, "input-payment-email"), "juana@yopmail.com")
    wait_and_send_keys(driver, (By.ID, "input-payment-telephone"), "1122223333")
    wait_and_send_keys(driver, (By.ID, "input-payment-address-1"), "Prueba 123")
    wait_and_send_keys(driver, (By.ID, "input-payment-city"), "Buenos Aires")
    wait_and_send_keys(driver, (By.ID, "input-payment-postcode"), "1234")

    select_country = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "country_id")))

    select = Select(select_country)

    select.select_by_value("10")

    driver.implicitly_wait(20)

    select_zone = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "zone_id")))

    select1 = Select(select_zone)

    select1.select_by_value("156")

    screenshot(driver, test_case_folder, "Complete billing information")

    wait_and_click(driver, (By.ID, 'button-guest'))

    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, 'button-shipping-method')))

    screenshot(driver, test_case_folder, "Delivery method")

    wait_and_click(driver, (By.ID, 'button-shipping-method'))

    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, 'button-payment-method')))

    wait_and_click(driver, (By.CSS_SELECTOR, 'input[value="cod"]'))
    wait_and_click(driver, (By.NAME, "agree"))

    screenshot(driver, test_case_folder, "Payment Method")

    wait_and_click(driver, (By.ID, 'button-payment-method'))

    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, 'button-confirm')))

    screenshot(driver, test_case_folder, "Purchase confirmation")

    wait_and_click(driver, (By.ID, 'button-confirm'))

    time.sleep(3)

    if "Your order has been placed!" in driver.page_source:
        print("Passed: Successful guest checkout completed.")
    else:
        print("Failed: The purchase could not be completed.")

    screenshot(driver, test_case_folder, "Guest Checkout Result")
    time.sleep(1)
    driver.quit()

def register_account_checkout():
    test_case_name = "Purchase with user account"
    test_case_folder = evidence(test_case_name)
    device_name = "Palm Treo Pro"
    user_email = "abc@yopmail.com"
    user_password = "abc123"

    driver = webdriver.Chrome()
    driver.maximize_window()

    url = "http://opencart.abstracta.us/"
    driver.get(url)

    wait_and_click(driver, (By.PARTIAL_LINK_TEXT, "Phones & PDAs"))

    screenshot(driver, test_case_folder, "Mobile Dashboard")

    wait_and_click(driver, (By.PARTIAL_LINK_TEXT, "Phones & PDAs"))
    wait_and_click(driver, (By.PARTIAL_LINK_TEXT, device_name))
    wait_and_click(driver, (By.XPATH,'//button[text()="Add to Cart"]'))

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-success")))

    screenshot(driver, test_case_folder, "The item was added to the cart")

    wait_and_click(driver, (By.ID, "cart-total"))
    wait_and_click(driver, (By.XPATH, "//*[@id='cart']/ul/li[2]/div/p/a[1]/strong"))

    screenshot(driver, test_case_folder, "Cart details")

    wait_and_click(driver, (By.CSS_SELECTOR, 'a[href="https://opencart.abstracta.us:443/index.php?route=checkout/checkout"].btn.btn-primary'))

    wait_and_click(driver, (By.CSS_SELECTOR, 'input[value="register"]'))
    wait_and_send_keys(driver, (By.ID, "input-email"), user_email)
    wait_and_send_keys(driver, (By.ID, "input-password"), user_password)

    screenshot(driver, test_case_folder, "Selected to continue with a user")

    wait_and_click(driver, (By.ID, "button-login"))

    # time.sleep(3)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'button-payment-address')))
    screenshot(driver, test_case_folder, "Billing details")
    wait_and_click(driver, (By.ID, 'button-payment-address'))

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'button-shipping-address')))
    screenshot(driver, test_case_folder, "Shipping details")
    wait_and_click(driver, (By.ID, 'button-shipping-address'))

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'button-shipping-method')))
    screenshot(driver, test_case_folder, "Delivery method")
    wait_and_click(driver, (By.ID, 'button-shipping-method'))

    wait_and_click(driver, (By.CSS_SELECTOR, 'input[value="cod"]'))
    wait_and_click(driver, (By.NAME, "agree"))
    screenshot(driver, test_case_folder, "Payment Method")

    wait_and_click(driver, (By.ID, 'button-payment-method'))

    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, 'button-confirm')))

    screenshot(driver, test_case_folder, "Purchase confirmation")

    wait_and_click(driver, (By.ID, 'button-confirm'))

    time.sleep(3)

    if "Your order has been placed!" in driver.page_source:
        print("Passed: Successful purchase with user account.")
    else:
        print("Failed: The purchase could not be completed.")

    screenshot(driver, test_case_folder, "Purchase result with registered user")
    time.sleep(1)

    driver.quit()


# Run the test cases

# user_registration()
# existing_user_registration()
# login()
# login_unregistered_user()
# guest_checkout()
# register_account_checkout()