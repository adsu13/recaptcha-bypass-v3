# Recaptcha Bypass

This project is an example of how to solve invisible reCAPTCHA v3 using Flask and the pychrome library.

## How It Works

This script uses **pychrome** to interact with the Chrome browser, executing Google's reCAPTCHA code directly in the browser and returning the response token.

## Requirements

- **Python 3.x**
- **Google Chrome**
- **Flask**
- **pychrome**

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/adsu13/recaptcha-bypass-v3.git
    cd recaptcha-bypass
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Start Chrome with the remote debugging port enabled:
    ```bash
    google-chrome --remote-debugging-port=9222
    ```

4. Run the application:
    ```bash
    python src/app.py
    ```

## How to Use

Access the `/recaptcha/v3` route to get the reCAPTCHA token.

Request example:
```bash
curl "http://localhost:8082/recaptcha/v3?key=PAGEKEY&action=PAGEACTION"
