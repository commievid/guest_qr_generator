import generate_key
import generate_qr
import webrouter
import epaper
import logging

logging.basicConfig(level = logging.INFO)

logging.info("Start")

logging.info("Generating random password for guest Wifi")
# Take this from somewhere, environment variable, etc.
ssid = "Example"
ssid_key = generate_key.generate()

logging.info("Generating QR code for guest Wifi")
image = generate_qr.generate(ssid, ssid_key)

logging.debug("Finished generating QR code for guest Wifi")

logging.info("Updating the password via WebDriver")
webrouter.update_password(ssid_key)

logging.info("Sending QR code to e-Paper")
epaper.draw_qr(ssid, ssid_key)
