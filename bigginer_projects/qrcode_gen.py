from turtle import fillcolor
import qrcode
import qrcode.constants
from scipy import constants
def gr_gen(data , file_name):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black",back_color="white")
    img.save(f"{file_name}.png")
data =input("Enter any data or url")
file_name = input("Enter name of the file to save")
gr_gen(data,file_name)
print("Qr code successfully generated")