import wifi_qrcode_generator
# pip install wifi-qrcode-generator

def generate(ssid, ssid_key):
    image = wifi_qrcode_generator.wifi_qrcode(ssid, False, "WPA", ssid_key)
    w, h = image.size
    print("Width: ", w)
    print("Height: ", h)
    image.crop((35, 35, w - 35, h - 35)).save("qr.png")
    return image
