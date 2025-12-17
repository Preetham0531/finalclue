# Well Done

A simple Streamlit app displaying "well done" with a bouquet logo. The app expires after 3 days from deployment.

## Installation

```bash
pip install -r requirements.txt
```

## Running the app

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## QR Code Generation

To generate a QR code for the app URL (https://ihavebeenexpectingyou.streamlit.app/), you can:

1. Use an online QR code generator: https://www.qr-code-generator.com/
2. Or use Python:
   ```bash
   pip install qrcode[pil]
   python generate_qr.py
   ```

## Expiration

The app is set to expire 3 days after deployment. Update the `DEPLOYMENT_DATE` in `app.py` to set the expiration date.
