import datetime
from time import sleep
import aos_locators
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)
# ------------------------------------------------------------------------------
def setup():
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
        sleep(2)
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
    sleep(2)
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
    sleep(2)
    print("Successfully log out")

# ----------------------------------------------------------------------------------------------------------

def login(username,password ): #login with new user
    print('-------------------------* Login User *-------------------------')
    if driver.current_url == aos_locators.AOS_Url:
        sleep(2)
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
            sleep(2)

#-----------------------------------------------------------------------------------------------------------------------------------------------------


def validate_new_user_display():  #Validate username is displayed
    print('-------------------------* Validate New User Display *-------------------------')
    if driver.current_url == aos_locators.AOS_Url:
        sleep(2)
        if driver.find_element(By.XPATH,  f'//a[contains(., "{aos_locators.new_username}")]'):
            sleep(3)
            print(f'--- Username {aos_locators.new_username} is displayed on Top right Menu ---')
        else:
            print("something went wrong:")
            sleep(3)
        sleep(2)

# ---------------------------------------------------------------------------------------------------------------------

def validate_home_page_texts_links():   # check functionality text are displayed
    print('-------------------------* Validate Home Page Texts Links *-------------------------')
    if driver.current_url == aos_locators.AOS_Url:
        sleep(2)
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
        sleep(2)

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
        sleep(2)
        assert driver.find_element(By.XPATH, f'//h3[contains(., "FOLLOW US")]').is_displayed()
        print(f'FOLLOW US text is displayed')
        sleep(0.25)
        driver.find_element(By.XPATH, "//img[@name = 'follow_facebook']").click()
        sleep(3)
        a = driver.window_handles[0]
        b = driver.window_handles[1]
        driver.switch_to.window(b)
        if driver.current_url == 'https://www.facebook.com/MicroFocus/':
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
        if driver.current_url == 'https://twitter.com/MicroFocus':
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
        #url = 'https://www.linkedin.com/company/1024?trk=tyah&trkInfo=clickedVertical%3Ashowcase%2CclickedEntityId%3A1024%2Cidx%3A2-1-2%2CtarId%3A145431482.327%2Ctas%3Ahewlett%20packard%20enterprise%20software'
        #if 'linkedin.com' in url:
        if 'LinkedIn' in driver.title:
            sleep(2)
            driver.close()
            driver.switch_to.window(a)
            sleep(2)
            print(f'LINKEDIN is displayed and Clickable:')
            sleep(2)


#------------------------------------------------------------------------------------------------------------------------------------------
def validate_contact_us_form():
    print('-------------------------* Validate Contact Us Form *-------------------------')
    if driver.current_url == aos_locators.AOS_Url:
        sleep(2)
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



def checkout_shopping_cart():
    print('-------------------------* Checkout Shopping Cart *-------------------------')
    if driver.current_url == aos_locators.AOS_Url:
        sleep(2)
        driver.find_element(By.ID, 'speakersTxt').click()
        sleep(3)
        if driver.current_url == 'https://advantageonlineshopping.com/#/category/Speakers/4':
            sleep(1)
            driver.find_element(By.LINK_TEXT , 'HP Roar Plus Wireless Speaker').click()
            sleep(2)
            if driver.current_url == 'https://advantageonlineshopping.com/#/product/21':
                sleep(2)
                driver.find_element(By.XPATH, "//button[@name = 'save_to_cart']").click()
                sleep(2)
                driver.find_element(By.ID, 'menuCart').click()
                sleep(2)
                if driver.current_url == 'https://advantageonlineshopping.com/#/shoppingCart':
                    sleep(2)
                    driver.find_element(By.ID, 'checkOutButton').click()
                    sleep(2)
                    if driver.current_url == 'https://advantageonlineshopping.com/#/orderPayment':
                        assert driver.find_element(By.XPATH, f'//label[contains(., "{aos_locators.full_name}")]').is_displayed()
                        sleep(3)
                        print(f'--- Full Name {aos_locators.full_name} is displayed on shipping details page---')
                        sleep(2)
                        driver.find_element(By.ID, 'next_btn').click()
                        sleep(2)
                        if driver.current_url == 'https://advantageonlineshopping.com/#/orderPayment':
                            driver.find_element(By.XPATH, "//input[@name = 'safepay_username']").send_keys(aos_locators.new_username)
                            sleep(2)
                            driver.find_element(By.XPATH, "//input[@name = 'safepay_password']").send_keys(aos_locators.new_password)
                            sleep(2)
                            driver.find_element(By.ID, 'pay_now_btn_SAFEPAY').click()
                            sleep(2)
                            assert driver.find_element(By.XPATH, f'//span [contains(., "Thank you for buying with Advantage")]').is_displayed()
                            sleep(2)
                            print(f'--- Validated Order is created by validating Thank you for buying with Advantage message is displayed ---')
                            sleep(2)
                            tracking_number = driver.find_element(By.ID, 'trackingNumberLabel').text
                            print(f' Tracking Number is : {tracking_number}')
                            sleep(2)
                            aos_locators.order_number = driver.find_element(By.ID, 'orderNumberLabel').text
                            print(f' Order Number is : {aos_locators.order_number}')
                            sleep(2)
                            if driver.current_url == 'https://advantageonlineshopping.com/#/orderPayment':
                                if driver.find_element(By.XPATH, f'//label[contains(., "{aos_locators.full_name}")]'):
                                    sleep(2)
                                    print(f'Fullname: {aos_locators.full_name} is validated in shipping details ')
                                else:
                                    print("something went wrong:")
                                    sleep(2)
                                if driver.find_element(By.XPATH, f'//label[contains(., "{aos_locators.phone_number1}")]'):
                                    sleep(2)
                                    print(f'Phone Number: {aos_locators.phone_number1} is validated in shipping details ')
                                else:
                                    print("something went wrong:")
                                    sleep(2)


#----------------------------------------------------------------------------------------------------------------------------------
def validate_order_page():
    print('-------------------------* Validate Order Page *-------------------------')
    if driver.current_url == aos_locators.AOS_Url:
        sleep(2)
        driver.find_element(By.ID, 'menuUser').click()
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[2]').click()
        sleep(2)
        if driver.current_url == 'https://advantageonlineshopping.com/#/MyOrders':
            order_element = driver.find_element(By.XPATH, f'//label[contains(text(), "{aos_locators.order_number}")]')
            assert order_element.is_displayed()
            sleep(1)
            print(f' Validated order is displayed  --- confirmed!')
            sleep(2)


def delete_order():
    print('-------------------------* Delete Order *-------------------------')
    if driver.current_url == 'https://advantageonlineshopping.com/#/MyOrders':
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'REMOVE').click()
        sleep(2)
        driver.find_element(By.XPATH, f'//label[contains(text(), "CANCEL")]').click()
        sleep(2)
        print(f'Order is deleted ')
        assert driver.find_element(By.XPATH, f'//label[contains(text(), "No orders")]').is_displayed()
        sleep(2)
        print(f'Validated Order is deleted by validating "No orders" text displayed ')
        sleep(2)
#-----------------------------------------------------------------------------------------------------------------------------
def delete_user():
    print('-------------------------* Delete User *-------------------------')
    if driver.current_url == aos_locators.AOS_Url:
        sleep(2)
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
        sleep(5)
        assert driver.find_element(By.XPATH, f'//label[contains(text(), "{aos_locators.full_name}")]').is_displayed()
        sleep(2)
        print(f'Validated Fullname {aos_locators.full_name} is displayed in My account details')
        sleep(3)
        driver.find_element(By.CLASS_NAME , 'deleteBtnText').click()
        sleep(3)
        #assert driver.find_element(By.XPATH, f'//*[contains(@class, "deletePopupBtn deleteRed")]').is_displayed()
        #sleep(2)
        driver.find_element(By.XPATH, f'//*[contains(@class, "deletePopupBtn deleteRed")]').click()
        sleep(2)
        print('Confirmation message is displayed: Account deleted Successfully')
        sleep(2)
#--------------------------------------------------------------------------------------------------------------

def delete_user_account():
    print(f'*---------------------------------------~* DELETE USER ACCOUNT *~---------------------------------------*')
    if driver.current_url == 'https://advantageonlineshopping.com/#/MyOrders':
        sleep(1)
        if driver.find_element(By.XPATH, f'//a[contains(., "{aos_locators.new_username}")]'):
            print(f'Username: {aos_locators.new_username} is displayed at Top right Menu.')
            sleep(2)
        else:
            print(f'User login not validated.')

        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(2)
        # Access user account details
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
        sleep(1)

        # Account details page before deletion
        assert driver.find_element(By.XPATH, f'//label[contains(., "{aos_locators.full_name}")]').is_displayed()
        sleep(3)
        print(f'Account details page for user: "{aos_locators.full_name}" is displayed.')
        assert driver.find_element(By.XPATH, '//button[contains(., "Delete Account")]').is_displayed()
        popup = driver.find_element(By.XPATH, '//button[contains(., "Delete Account")]').is_displayed()
        print(f'Delete popup is displayed: {popup}')
        sleep(2)

        # Click the Delete Account button
        driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
        sleep(5)
       # assert driver.find_element(By.XPATH, '//*[contains(@class, "deletePopupBtn deleteRed")]').is_displayed()
       # popup1 = driver.find_element(By.XPATH, '//*[contains(@class, "deletePopupBtn deleteRed")]').is_displayed()
        #print(f'Delete Confirmation screen is displayed: {popup1}')
        #sleep(2)
        driver.find_element(By.XPATH, '//*[contains(@class, "deletePopupBtn deleteRed")]').click()
        sleep(3)
        print(f'Confirmation message is displayed: Account deleted successfully.')
        sleep(4)
        #print(f'User {aos_locators.full_name} with email address {aos_locators.email} is deleted!')

#-----------------------------------------------------------------------------------------

def validate_account_deleted():
    sleep(2)
    print('-------------------------* Validate Account Deleted *-------------------------')
    if driver.current_url == aos_locators.AOS_Url:
        sleep(3)
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(2)
        if driver.current_url == aos_locators.AOS_Url:
            driver.find_element(By.XPATH, "//input[@name = 'username']").send_keys(aos_locators.new_username)
            sleep(2)
            driver.find_element(By.XPATH, "//input[@name = 'password']").send_keys(aos_locators.new_password)
            sleep(2)
            driver.find_element(By.XPATH, "//button[@id = 'sign_in_btnundefined']").click()
            sleep(2)
            assert driver.find_element(By.XPATH, f'//label[contains(text(), "Incorrect user name or password.")]').is_displayed()
            sleep(2)
            print("Confirmed Account deleted by validating error message Incorrect username and password displayed ")


#----------------------------------------------------------------------------------------------------------------------------------------
#setUp()
#validate_home_page_texts_links()
#validate_top_navigation_menu()
#validate_contact_us_form()
#validate_social_media_link()
#create_new_user()
#delete_user()
#validate_account_deleted()
#validate_new_user_display()
#log_out()
#login(aos_locators.new_username, aos_locators.new_password)
#checkout_shopping_cart()
#log_out()
#login(aos_locators.new_username, aos_locators.new_password)
#validate_order_page()
#delete_order()
#validate_new_user_display()
#log_out()
#teardown()
