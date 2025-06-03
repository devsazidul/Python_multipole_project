# pip install qrcode
# pip install pillow

import qrcode as qr

img=qr.make("https://www.facebook.com/Rabbi.molla.3994885")
img.save("facebook.png")