import datetime
from time import sleep
import aos_locators
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.support.select import Select

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)
# ------------------------------------------------------------------------------


def setUp():
    driver.maximize_window()  # Open web browser and maximize the window
    driver.implicitly_wait(30)  # wait for the web browser
    print(f'test started at:{datetime.datetime.now()}')
    driver.get(aos_locators.AOS_Url)  # navigating to the AOS website
    sleep(0.25)

    # check that url address and the title are correct
    if driver.current_url == aos_locators.AOS_Url and driver.title == aos_locators.AOS_title:
        print(f'We are at the correct website:',{driver.current_url})
        print(f'We are seeing correct title page',{driver.title})

    else:
        print(f'We are not at that correct website/check your code')

# ---------------------------------------------------------------------------------------------

def teardown():  # function to end the session
    if driver is not None:
        print(f'-----------')
        print(f'test completed at:{datetime.datetime.now()}')
        driver.close()
        driver.quit()

# ---------------------------------------------------------------------------------------------

def create_new_user(): #create new user
    if driver.current_url == aos_locators.AOS_Url and driver.title == aos_locators.AOS_title:

        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(2)

        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
        sleep(2)
        if driver.current_url == 'https://advantageonlineshopping.com/#/register':
            driver.find_element(By.XPATH, "//input[@name = 'usernameRegisterPage']").send_keys(aos_locators.new_username)
            sleep(2)
            driver.find_element(By.XPATH, "//input[@name = 'emailRegisterPage']").send_keys(aos_locators.email)
            sleep(2)
            driver.find_element(By.XPATH, "//input[@name = 'passwordRegisterPage']").send_keys(aos_locators.new_password)
            sleep(2)
            driver.find_element(By.XPATH, "//input[@name = 'confirm_passwordRegisterPage']").send_keys(aos_locators.new_password)
            sleep(2)
            driver.find_element(By.XPATH, "//input[@name = 'first_nameRegisterPage']").send_keys(aos_locators.first_name)
            sleep(2)
            driver.find_element(By.XPATH, "//input[@name = 'last_nameRegisterPage']").send_keys(aos_locators.last_name)
            sleep(2)

            driver.find_element(By.XPATH, "//input[@name = 'phone_numberRegisterPage']").send_keys(aos_locators.phone_number1)
            sleep(2)
            Select(driver.find_element(By.XPATH, "//select[@name = 'countryListboxRegisterPage']")).select_by_visible_text('Canada')
            sleep(2)
            driver.find_element(By.XPATH, "//input[@name = 'cityRegisterPage']").send_keys(aos_locators.city)
            sleep(2)
            driver.find_element(By.XPATH, "//input[@name = 'addressRegisterPage']").send_keys(aos_locators.address)
            sleep(2)
            driver.find_element(By.XPATH, "//input[@name = 'state_/_province_/_regionRegisterPage']").send_keys(aos_locators.province)
            sleep(2)
            driver.find_element(By.XPATH, "//input[@name = 'postal_codeRegisterPage']").send_keys(aos_locators.postcode)
            sleep(2)
            driver.find_element(By.XPATH, "//input[@name = 'i_agree']").click()
            sleep(2)
            driver.find_element(By.XPATH, "//button[@id = 'register_btnundefined']").click()
            sleep(2)
            if driver.current_url  == 'https://advantageonlineshopping.com/#/':
                assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
                print(f'New user is created successfully and you can see username at top menu: {aos_locators.new_username}')
                sleep(2)
            else:
                print('something went wrong')
# ---------------------------------------------------------------------------------------------

def log_out(): #log out with new user
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
    sleep(2)
    print("Successfully log out")

# ----------------------------------------------------------------------------------------------------------

def login(username,password ): #login with new user
    if driver.current_url == aos_locators.AOS_Url:
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(2)
        if driver.current_url == aos_locators.AOS_Url:
            driver.find_element(By.XPATH, "//input[@name = 'username']").send_keys(username)
            sleep(2)
            driver.find_element(By.XPATH, "//input[@name = 'password']").send_keys(password)
            sleep(2)
            driver.find_element(By.XPATH, "//button[@id = 'sign_in_btnundefined']").click()
            sleep(2)
            assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
            print(f'User is logged in successfully and you can see username at top menu: {aos_locators.new_username}')

# ---------------------------------------------------------------------------------------------------------------------














#setUp()
#create_new_user()

#log_out()
#login(aos_locators.new_username, aos_locators.new_password)

#log_out()

#teardown()
