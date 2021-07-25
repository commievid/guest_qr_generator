import generate_key
import generate_qr
import webrouter
import epaper

print("Start")

print("Generating random password for guest Wifi")
# Take this from somewhere, environment variable, etc.
ssid = "Example"
ssid_key = generate_key.generate()

print("Generating QR code for guest Wifi")
image = generate_qr.generate(ssid, ssid_key)

print("Finished generating QR code for guest Wifi")

# print("Updating the password via WebDriver")
# webrouter.update_password(ssid_key)

epaper.draw_qr(ssid, ssid_key)