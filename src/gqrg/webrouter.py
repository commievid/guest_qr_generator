from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import keyring
import keyring.backend
from keyrings.alt.file import PlaintextKeyring
from pyvirtualdisplay import Display
import logging

logging.basicConfig(level = logging.INFO)

def update_password(ssid_key, headless = True):

    # Not best practice to use plain text keyring, but for Linux by default
    # the keyring asks for an additional encryption password which would need
    # extra stuff to sort out
    keyring.set_keyring(PlaintextKeyring())

    if headless:
        logging.info("Starting virtual display")
        disp = Display()
        disp.start()

    # The EPD drivers seem to only want to run as sudo, which means that the
    # chromedriver will need start Chrome with no sandbox. This is not a good
    # normally, but in the realms of a Selenium automated process, maybe ok
    logging.info("Starting chromedriver")
    opts = webdriver.ChromeOptions()
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options = opts)

    logging.info("Connecting to router")
    # Password will need setting first: keyring.set_password
    driver.get("http://admin:" + keyring.get_password("gqrg", "admin") + "@192.168.1.1")

    wait = WebDriverWait(driver, 30)
    frame = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/table/tbody/tr/td[2]/div/iframe")))
    # /html/body/div[2]/div/div[3]/iframe
    driver.switch_to.frame(frame)

    element = wait.until(EC.element_to_be_clickable((By.ID, "guest")))
    element.click()

    passphrase = wait.until(EC.visibility_of_element_located((By.ID, 'passphrase')))
    #  passphrase

    passphrase.clear()
    passphrase.send_keys(ssid_key)

    apply = wait.until(EC.visibility_of_element_located((By.ID, "apply")))
    apply.click()

    time.sleep(5)

    logging.info("Logging out")
    driver.switch_to.default_content()
    frame = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/iframe")))
    driver.switch_to.frame(frame)

    logout = wait.until(EC.visibility_of_element_located((By.ID, "logout")))
    logout.click()

    time.sleep(5)

    logging.info("Stopping chromedriver")
    driver.close()
    driver.quit()

    if headless:
        logging.info("Stopping virtual display")
        disp.stop()