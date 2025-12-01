import qrcode

data = input("Enter the url or text: ")

qr = qrcode.QRCode(

    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4
) 

qr.add_data(data)
qr.make(fit = True)

img = qr.make_image(fill_colour = "black", back_colour = "white")

img.save("MyQRCODE.png")
print("QR code generated!!")