from selenium import webdriver
import time
import smtplib
from email import message
from selenium.webdriver.chrome.options import Options # added chrome options to run it headless
import logging
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import requests

stored_messsages = []
today = datetime.today().strftime('%d-%m-%Y')


################################################################################################

def send_telegram(stored_messages):
    #left blank intentionally
    base_url = '***telegram bot api***'.format(a=''.join(stored_messages))
    requests.get(base_url)


################################################################################################

def send_error_email(e):
    EMAIL_ADDRESS = '***email address***'
    EMAIL_PASSWORD = '***email app specific password***'

    from_addr = '***email address***'
    to_addr1 = '***email address***'
    

    ### message ###
    subject = 'Weekend Game: ERROR!'
    body = '{x}'.format(x=e)

    msg = message.Message()

    msg.add_header('from',from_addr)
    msg.add_header('to',to_addr1)
    msg.add_header('subject', subject)
    msg.set_payload(body)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(from_addr, '***server specific password***')
    server.send_message(msg, from_addr=from_addr, to_addrs=to_addr1)

################################################################################################

def fill_form(name, member, email, phone, course, session):

    if course == 'x':

        #webdriver config

        chrome_options = Options() # added chrome options to run it headless
        # chrome_options.add_argument("--headless") # added chrome options to run it headless
        # web = webdriver.Chrome(options=chrome_options) # added chrome options to run it headless
        web = webdriver.Remote('http://localhost:4444/wd/hub', DesiredCapabilities.CHROME) #options=webdriver.ChromeOptions()) # added chrome for docker in server and configure to run in dockered chrome in script

        web.get("***website***")

        # web.maximize_window() # For maximizing window
        web.implicitly_wait(20) # gives an implicit wait for 20 seconds

        #click registration form link
        registration_form = web.find_element('xpath','***xpath***')
        registration_form.click()
        time.sleep(3)
    
        # have to switch to the new opened window in order to interact with it. 
        # Seeing it open in chrome doesn't count... it wont work.
        web.switch_to.window(web.window_handles[-1]) 

        #fill in personal info
        name_find = web.find_element('xpath','***xpath***')
        name_find.send_keys(name)

        member_find = web.find_element('xpath','***xpath***')
        member_find.send_keys(member)

        email_find = web.find_element('xpath','***xpath***')
        email_find.send_keys(email)

        phone_find = web.find_element('xpath','***xpath***')
        phone_find.send_keys(phone)

        ######################################  course option (sat) ######################################## 

        radio_x_course_option1 = web.find_element('xpath', '***xpath***')
        radio_x_course_option1.click()
        time.sleep(3)

        ######################################## session (sat) ############################################
        try:
            if session == 'pm':
                #pm
                radio_session_pm1 = web.find_element('xpath', '***xpath***')
                radio_session_pm1.click()  
            elif session == 'am':
               #am
                radio_session_am1 = web.find_element('xpath', '***xpath***')
                radio_session_am1.click()
        except:
            try:
                #pm
                radio_session_pm1 = web.find_element('xpath', '***xpath***')
                radio_session_pm1.click()  
            except:
                #am
                radio_session_am1 = web.find_element('xpath', '***xpath***')
                radio_session_am1.click()

        ######################################  course option (sat) ######################################## 

        radio_x_course_option2 = web.find_element('xpath', '***xpath***') 
        radio_x_course_option2.click()
        time.sleep(3)

        ######################################## session (sat) ############################################
        try:

            if session == 'pm':
                #pm
                radio_session_pm1 = web.find_element('xpath', '***xpath***')
                radio_session_pm1.click()
                
            elif session == 'am':
                #am
                radio_session_am1 = web.find_element('xpath', '***xpath***')
                radio_session_am1.click()
        except:
            try:
                #pm
                radio_session_pm1 = web.find_element('xpath', '***xpath***')
                radio_session_pm1.click()
            except:
                #am
                radio_session_am1 = web.find_element('xpath', '***xpath***')
                radio_session_am1.click()

        radio_playersupdate = web.find_element('xpath', '***xpath***')
        radio_playersupdate.click()

        radio_disclaimer = web.find_element('xpath', '***xpath***')
        radio_disclaimer.click()
    else:
        
        #webdriver config
        
        chrome_options = Options() # added chrome options to run it headless
        # chrome_options.add_argument("--headless") # if you wish to run code in IDE headless
        # web = webdriver.Chrome(options=chrome_options) # added chrome options to run it headless
        web = webdriver.Remote('http://localhost:4444/wd/hub', DesiredCapabilities.CHROME) # added chrome for docker in server and configure to run in dockered chrome in script
        

        web.get("***website***")

        # web.maximize_window() # For maximizing window
        web.implicitly_wait(20) # gives an implicit wait for 20 seconds

        #click registration form link

        registration_form = web.find_element('xpath','***xpath***')
        registration_form.click()
        time.sleep(3)
    
        # have to switch to the new opened window in order to interact with it. 
        # Seeing it open in chrome doesn't count... it wont work.

        web.switch_to.window(web.window_handles[-1]) 

        #fill in personal info
        name_find = web.find_element('xpath','***xpath***')
        name_find.send_keys(name)

        member_find = web.find_element('xpath','***xpath***')
        member_find.send_keys(member)

        email_find = web.find_element('xpath','***xpath***')
        email_find.send_keys(email)

        phone_find = web.find_element('xpath','***xpath***')
        phone_find.send_keys(phone)

        ######################################  course option (sat) ######################################## 

        radio_y_course_option1 = web.find_element('xpath', '***xpath***')
        radio_y_course_option1.click()
        time.sleep(3)

        ######################################## session (sat) ############################################
        try:
            if session == 'pm':
                #pm
                radio_session_pm1 = web.find_element('xpath', '***xpath***')
                radio_session_pm1.click()
            elif session == 'am':
                #am
                radio_session_am1 = web.find_element('xpath', '***xpath***')
                radio_session_am1.click()
                
        except:
            try:
                #pm
                radio_session_pm1 = web.find_element('xpath', '***xpath***')
                radio_session_pm1.click()
            except:
                #am
                radio_session_am1 = web.find_element('xpath', '***xpath***')
                radio_session_am1.click()

        ######################################  course option (sun) ######################################## 

        radio_y_course_option2 = web.find_element('xpath', '***xpath***')
        radio_y_course_option2.click()
        time.sleep(3)

        ######################################## session (sun) ############################################
        try:
            if session == 'pm':
                #pm
                radio_session_pm1 = web.find_element('xpath', '***xpath***')
                radio_session_pm1.click()
            elif session == 'am':
                #am
                radio_session_am1 = web.find_element('xpath', '***xpath***')
                radio_session_am1.click()
        except:
            try:
                #pm
                radio_session_pm1 = web.find_element('xpath', '***xpath***')
                radio_session_pm1.click()
            except:
                #am
                radio_session_am1 = web.find_element('xpath', '***xpath***')
                radio_session_am1.click()

        radio_playersupdate = web.find_element('xpath', '***xpath***')
        radio_playersupdate.click()

        radio_disclaimer = web.find_element('xpath', '***xpath***')
        radio_disclaimer.click()

        time.sleep(5)
    
     
    
    ## submit form ###

    submit = web.find_element('xpath', '***xpath***')
    submit.click()


    time.sleep(3)

    # store email information in each run (will run 1 time each member)
    stored_value = str(f'\n{name}, {course}, {session}\n')
    print(stored_value)
    stored_messsages.append(stored_value)

    time.sleep(5)
    web.quit()


try:
    logging.debug('********** START **********')
    print('********** START **********')
    fill_form('name','membership number', 'email' ,'phone number', 'x','am')
    fill_form('name','membership number', 'email' ,'phone number', 'x','am')
    fill_form('name','membership number', 'email' ,'phone number', 'y','am')
    send_telegram(stored_messsages)

except Exception as e:
    logging.debug(e)
    print(e)
    send_error_email(e)

else: # only runs when try runs successfully
    logging.debug('booking code ran successfully!')
    print('booking code ran successfully!')
    
finally: # runs regardless if try and except is successful
    logging.debug('********** END **********')
    print('********** END **********')

