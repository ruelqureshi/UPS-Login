from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
import undetected_chromedriver as uc
import time
import random

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
#chrome_options.add_argument("--headless")

driver = uc.Chrome(options=chrome_options)

driver.maximize_window()

stealth(driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)

driver.implicitly_wait(10)

driver.get('https://www.ups.com/lasso/login')

# Credentials
email = "<email>"
password = "<password>"

# Locate and fill email field
time.sleep(2)  # Mimic human delay
enter_email = driver.find_element('xpath', "//input[@id='email']")
enter_email.click()
for e in email:
    enter_email.send_keys(e)
    time.sleep(random.uniform(0.1, 0.2))  # Random delay between 0.1 and 0.2 seconds
enter_email.send_keys(Keys.ENTER)

# Locate and fill password field
time.sleep(2)
enter_password = driver.find_element('xpath', "//input[@id='pwd']")
enter_password.click()
for p in password:
    enter_password.send_keys(p)
    time.sleep(random.uniform(0.1, 0.2))  # Random delay between 0.1 and 0.2 seconds
enter_password.send_keys(Keys.ENTER)

print('[+] Done')
time.sleep(10)
driver.quit()