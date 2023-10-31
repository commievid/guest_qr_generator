import generate_key
import generate_qr
import webrouter
import epaper
import logging
import keyring
from keyings.alt.file import PlaintextKeyring

# Not best practice to use the plain text keyring
keyring.set_keyring(PlaintextKeyring())

logging.basicConfig(level = logging.INFO)

logging.info("Start")

logging.info("Generating random password for guest Wifi")

ssid = keyring.get_password("gqrg", "ssid")
ssid_key = generate_key.generate()

logging.info("Generating QR code for guest Wifi")
image = generate_qr.generate(ssid, ssid_key)

logging.debug("Finished generating QR code for guest Wifi")

logging.info("Updating the password via WebDriver")
webrouter.update_password(ssid_key)

logging.info("Sending QR code to e-Paper")
epaper.draw_qr(ssid, ssid_key)
