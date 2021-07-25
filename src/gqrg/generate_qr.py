import wifi_qrcode_generator
import logging

logging.basicConfig(level = logging.INFO)

def generate(ssid, ssid_key):
    image = wifi_qrcode_generator.wifi_qrcode(ssid, False, "WPA", ssid_key)
    w, h = image.size
    logging.debug("Width: ", w)
    logging.debug("Height: ", h)
    image.crop((35, 35, w - 35, h - 35)).save("qr.png")

    logging.info("QR code generated successfully")

    return image
