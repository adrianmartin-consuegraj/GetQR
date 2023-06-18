import qrcode

# Website URL
website_url = "https://www.huellafeliz.es"

# Generate QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data(website_url)
qr.make(fit=True)

# Create an image from the QR code
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
qr_image.save("website_qr.png")