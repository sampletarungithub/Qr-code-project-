
import qrcode as qr
from PIL import Image

qr=qr.QRCode(version=1,
             error_correction=qr.ERROR_CORRECT_H,
             box_size=20,border=4)
qr.add_data("https://in.pinterest.com/vandanalather/khatu-shyam/")
qr.make(fit=True)

img=qr.make_image(fill_color="red",back_color="White")
img.save("Khatu_Shyam_Darshan.png")
