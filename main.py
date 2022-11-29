from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from twilio.rest import Client
from dotenv import load_dotenv
import time
import os

# load_dotenv()

print("STARTING AAA")

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=chrome_options)

driver.get(
    "https://epprd.mcmaster.ca/psp/prepprd/?cmd=login&languageCd=ENG&")

print("Starting")
driver.implicitly_wait(10)

print("ok done waiting")
username = driver.find_element_by_id("userid")
username.send_keys(os.getenv("USER_ID"))

password = driver.find_element_by_id("pwd")
password.send_keys(os.getenv("PASS"))

driver.find_element_by_name('Submit').click()

# driver.find_element_by_xpath('//*[@id="MCM_IMG_CLASS$10"]').click()
driver.get("https://epprd.mcmaster.ca/psp/prepprd/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL")

# press enroll top left
frame = driver.find_element_by_xpath('//*[@id="ptifrmtgtframe"]')
driver.switch_to.frame(frame)
driver.find_element_by_id('DERIVED_SSS_SCR_SSS_LINK_ANCHOR3').click()

# uncomment line 40 and comment line 42 if your course is in winter semester
# although you might need to check the other ID's as they may be different

# driver.find_element_by_id('SSR_DUMMY_RECV1$sels$2$$0').click()

driver.find_element_by_id('SSR_DUMMY_RECV1$sels$1$$0').click()
driver.find_element_by_id('DERIVED_SSS_SCT_SSR_PB_GO').click()

while True:
    print("Starting loop")
    driver.find_element_by_id('DERIVED_REGFRM1_LINK_ADD_ENRL$82$').click()

    try:
        driver.find_element_by_id('DERIVED_REGFRM1_SSR_PB_SUBMIT').click()
    except:
        driver.switch_to.default_content
        driver.find_element_by_id('DERIVED_REGFRM1_SSR_PB_SUBMIT').click()

    message = driver.find_element_by_xpath(
        '//*[@id="win0divDERIVED_REGFRM1_SS_MESSAGE_LONG$0"]/div').text
    if not "full" in message:
        client = Client(os.getenv("TWILIO_SID"), os.getenv("AUTH"))

        message = client.messages.create(
            body="Your course has been selected!",
            from_=os.getenv("FROM_NUMBER"),
            to=os.getenv("TARGET_NUMBER")
        )
        print(message.body)
        driver.quit()
    else:
        driver.find_element_by_xpath('//*[@id="selectedtab"]/a').click()
    print("Tried")
    # checks every 5 min
    time.sleep(300)
