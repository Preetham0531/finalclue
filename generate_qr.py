import qrcode
from PIL import Image

# URL of your Streamlit app
app_url = "https://ihavebeenexpectingyou.streamlit.app/"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(app_url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qr_code.png")
print(f"QR code generated successfully for: {app_url}")
print("Saved as: qr_code.png")

