#QR CODE GENERATOR

import qrcode

def create_qr(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("my_qr.png")


data = input("Enter data to encode in QR: ")
create_qr(data)

print("QR generated successfully")