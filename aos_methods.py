import datetime
from time import sleep
import aos_locators
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.remote.webelement import WebElement
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
    print('-------------------------* Launch Advantage Shopping Online *-----------------------')
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
    print('-------------------------* Create New User *-------------------------')
    if driver.current_url == aos_locators.AOS_Url and driver.title == aos_locators.AOS_title:

        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
        sleep(2)
        if driver.current_url == aos_locators.AOS_register:
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
            if driver.current_url  == aos_locators.AOS_Url:
                print(f'New user is created successfully and you can see username at top menu: {aos_locators.new_username}')
                sleep(2)
            else:
                print('something went wrong')

# -----------------------------------------------------------------------------------------------------------------------------

def log_out(): #log out with new user
    print('-------------------------* Logout  User *-------------------------')
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
    sleep(2)
    print("Successfully log out")

# ----------------------------------------------------------------------------------------------------------

def login(username,password ): #login with new user
    print('-------------------------* Login User *-------------------------')
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
            if driver.current_url == aos_locators.AOS_Url:
                print(f'User is logged in successfully and you can see username at top menu: {aos_locators.new_username}')
            else:
                print('something went wrong')

#-----------------------------------------------------------------------------------------------------------------------------------------------------


def validate_new_user_display():  #Validate username is displayed
    print('-------------------------* Validate New User Display *-------------------------')
    if driver.current_url == aos_locators.AOS_Url:
        if driver.find_element(By.XPATH,  f'//a[contains(., "{aos_locators.new_username}")]'):
            sleep(3)
            print(f'--- Username {aos_locators.new_username} is displayed on Top right Menu ---')
        else:
            print("something went wrong:")
            sleep(3)

# ---------------------------------------------------------------------------------------------------------------------

def validate_home_page_texts_links():   # check functionality text are displayed
    print('-------------------------* Validate Home Page Texts Links *-------------------------')
    if driver.current_url == aos_locators.AOS_Url:
        assert driver.find_element(By.XPATH, '//span[contains(., "SPEAKERS")]').is_displayed()
        driver.find_element(By.ID, 'speakersTxt').click()
        sleep(3)
        driver.back()
        sleep(2)
        driver.find_element(By.ID, 'speakersLink').click()  # This is a shop Now line
        sleep(3)
        driver.back()
        sleep(2)
        print(f'Home page item SPEAKERS is displayed and clickable. Shop Now link is clickable.')
        sleep(2)
        assert driver.find_element(By.XPATH, '//span[contains(., "TABLETS")]').is_displayed()
        driver.find_element(By.ID, 'tabletsTxt').click()
        sleep(3)
        driver.back()
        sleep(2)
        driver.find_element(By.ID, 'tabletsLink').click()  # This is a shop Now line
        sleep(2)
        driver.back()
        print(f'Home page item TABLETS is displayed and clickable. Shop Now link is clickable.')
        sleep(2)
        assert driver.find_element(By.XPATH, '//span[contains(., "LAPTOPS")]').is_displayed()
        driver.find_element(By.ID, 'laptopsTxt').click()
        sleep(3)
        driver.back()
        sleep(2)
        driver.find_element(By.ID, 'laptopsLink').click()
        sleep(2)
        driver.back()
        print(f'Home page item LAPTOPS is displayed and clickable. Shop Now link is clickable.')
        sleep(2)
        assert driver.find_element(By.XPATH, '//span[contains(., "MICE")]').is_displayed()
        driver.find_element(By.ID, 'miceTxt').click()
        sleep(3)
        driver.back()
        sleep(2)
        driver.find_element(By.ID, 'miceLink').click()
        sleep(2)
        driver.back()
        print(f'Home page item MICE is displayed and clickable. Shop Now link is clickable.')
        sleep(2)
        assert driver.find_element(By.XPATH, '//span[contains(., "HEADPHONES")]').is_displayed()
        driver.find_element(By.ID, 'headphonesTxt').click()
        sleep(3)
        driver.back()
        sleep(2)
        driver.find_element(By.ID, 'headphonesLink').click()
        sleep(2)
        driver.back()
        print(f'Home page item HEADPHONES is displayed and clickable. Shop Now link is clickable.')
        sleep(2)
        assert driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').is_displayed()
        driver.find_element(By.ID, 'see_offer_btn').click()
        sleep(3)
        driver.back()
        sleep(2)
        print(f'Home page item SPECIAL OFFERS  is displayed and SEE OFFER is clickable')
        sleep(2)
        assert driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').is_displayed()
        driver.find_element(By.ID, 'details_16').click()
        sleep(3)
        driver.back()
        sleep(2)
        print(f'Home page item POPULAR ITEMS 1 is displayed')
        driver.find_element(By.ID, 'details_10').click()
        sleep(3)
        driver.back()
        sleep(2)
        print(f'Home page item POPULAR ITEMS 2 is displayed')
        driver.find_element(By.ID, 'details_21').click()
        sleep(3)
        driver.back()
        sleep(2)
        print(f'Home page item POPULAR ITEMS 3 is displayed')
        assert driver.find_element(By.XPATH,  f'//span[contains(., "dvantage")]').is_displayed()
        print(f'Main Logo is displayed')
        sleep(1)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

def validate_top_navigation_menu():
    print('-------------------------* Validate Top Navigation Menu *-------------------------')
    if driver.current_url == aos_locators.AOS_Url:
        sleep(4)
        driver.find_element(By.XPATH, '//a[contains(., "OUR PRODUCTS")]').click()
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').click()
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').click()
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
        sleep(2)
        driver.find_element(By.ID, 'menuSearch').click()
        sleep(2)
        driver.find_element(By.ID, 'menuUser').click()
        sleep(2)
        driver.refresh()
        # driver.find_element(By.CLASS_NAME, 'closeBtn loginPopUpCloseBtn').click()
        sleep(4)
        driver.find_element(By.ID, 'menuCart').click()
        sleep(2)
        driver.back()
        sleep(4)
        driver.find_element(By.ID, 'menuHelp').click()
        sleep(2)
        print(f'Top menu items OUR PRODUCTS | SPECIAL OFFER | POPULAR ITEM | CONTACT US | SEARCH ICON | SIGN IN ICON | CART ICON | QUESTION ICON is clickable')
        sleep(4)

# ----------------------------------------------------------------------------------------------------------------


def validate_social_media_link():
    print('-------------------------* Validate Social Media Link *-------------------------')
    if driver.current_url == aos_locators.AOS_Url:
        assert driver.find_element(By.XPATH, f'//h3[contains(., "FOLLOW US")]').is_displayed()
        print(f'FOLLOW US text is displayed')
        sleep(0.25)
        driver.find_element(By.XPATH, "//img[@name = 'follow_facebook']").click()
        sleep(3)
        a = driver.window_handles[0]
        b = driver.window_handles[1]
        driver.switch_to.window(b)
        driver.close()
        driver.switch_to.window(a)
        sleep(2)
        print(f'FACEBOOK is displayed and Clickable:')
        sleep(2)
        driver.find_element(By.XPATH, "//img[@name = 'follow_twitter']").click()
        sleep(3)
        a = driver.window_handles[0]
        b = driver.window_handles[1]
        driver.switch_to.window(b)
        driver.close()
        driver.switch_to.window(a)
        sleep(2)
        print(f'TWITTER is displayed and Clickable:')
        sleep(0.25)
        driver.find_element(By.XPATH, "//img[@name = 'follow_linkedin']").click()
        sleep(3)
        a = driver.window_handles[0]
        b = driver.window_handles[1]
        driver.switch_to.window(b)
        driver.close()
        driver.switch_to.window(a)
        sleep(1)
        #driver.back()
        sleep(2)
        print(f'LINKEDIN is displayed and Clickable:')
        sleep(2)

#------------------------------------------------------------------------------------------------------------------------------------------
def validate_contact_us_form():
    print('-------------------------* Validate Contact Us Form *-------------------------')
    if driver.current_url == aos_locators.AOS_Url:
        sleep(1)
        Select(driver.find_element(By.XPATH, "//select[@name = 'categoryListboxContactUs']")).select_by_visible_text('Speakers')
        sleep(2)
        Select(driver.find_element(By.XPATH, "//select[@name = 'productListboxContactUs']")).select_by_visible_text('HP Roar Wireless Speaker')
        sleep(2)
        driver.find_element(By.XPATH, "//input[@name = 'emailContactUs']").send_keys(aos_locators.email)
        sleep(2)
        driver.find_element(By.XPATH, "//textarea[@name = 'subjectTextareaContactUs']").send_keys(aos_locators.description)
        sleep(2)
        driver.find_element(By.ID , 'send_btnundefined').click()
        sleep(2)
        assert driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING')
        driver.find_element(By.LINK_TEXT , 'CONTINUE SHOPPING').click()
        sleep(2)
        print(f'Contact Us form is validated:')
        sleep(2)

#setUp()
#validate_home_page_texts_links()
#validate_top_navigation_menu()
#validate_contact_us_form()
#validate_social_media_link()
#create_new_user()
#validate_new_user_display()
#log_out()
#login(aos_locators.new_username, aos_locators.new_password)
#validate_new_user_display()
#log_out()
#teardown()
