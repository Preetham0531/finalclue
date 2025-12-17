#!/usr/bin/env python3
"""
Simple QR code generator that downloads QR code from online API
"""
import urllib.request

# URL of your Streamlit app
app_url = "https://ihavebeenexpectingyou.streamlit.app/"

# Generate QR code using online API
qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?size=500x500&data={app_url}"

# Download and save the QR code
output_file = "qr_code.png"
print(f"Downloading QR code for: {app_url}")
urllib.request.urlretrieve(qr_code_url, output_file)
print(f"QR code saved successfully as: {output_file}")
print(f"You can find it in: {__file__[:__file__.rfind('/')]}/{output_file}")

