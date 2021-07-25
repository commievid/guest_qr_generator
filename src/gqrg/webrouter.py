from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import keyring
from pyvirtualdisplay import Display
import logging

logging.basicConfig(level = logging.INFO)

def update_password(ssid_key, headless = True):
    
    if headless:
        logging.info("Starting virtual display")
        disp = Display()
        disp.start()

    logging.info("Starting chromedriver")
    driver = webdriver.Chrome()

    logging.info("Connecting to router")
    # Password will need setting first: keyring.set_password
    driver.get("http://admin:" + keyring.get_password("gqrg", "admin") + "@192.168.1.1")

    wait = WebDriverWait(driver, 10)
    frame = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[3]/iframe")))
    driver.switch_to.frame(frame)      

    element = wait.until(EC.element_to_be_clickable((By.ID, "guest")))
    element.click()

    passphrase = wait.until(EC.visibility_of_element_located((By.ID, 'passphrase')))

    passphrase.clear()
    passphrase.send_keys(ssid_key)

    apply = wait.until(EC.visibility_of_element_located((By.ID, "apply")))
    apply.click()

    time.sleep(5)

    logging.info("Logging out")
    driver.switch_to.default_content()
    driver.switch_to.frame("topframe")      

    logout = wait.until(EC.visibility_of_element_located((By.ID, "logout")))
    logout.click()

    time.sleep(5)

    logging.info("Stopping chromedriver")
    driver.close()
    driver.quit()

    if headless:
        logging.info("Stopping virtual display")
        disp.stop()
    