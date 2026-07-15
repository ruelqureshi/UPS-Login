# UPS Login & Browser Automation

## Overview

This script automates logging into a UPS account using Selenium. It launches a Chrome browser, applies a few anti-detection settings, opens the UPS login page, enters the email and password with human-like typing delays, and submits the login form.

## Requirements

* Python 3.x
* Selenium
* undetected-chromedriver
* selenium-stealth

Install the required packages:

```bash
pip install selenium undetected-chromedriver selenium-stealth
```

## How It Works

1. Starts an `undetected-chromedriver` Chrome session.
2. Applies browser fingerprint modifications using `selenium-stealth`.
3. Opens the UPS login page.
4. Types the email address character by character with random delays.
5. Submits the email and enters the password using the same approach.
6. Waits briefly after login before closing the browser.

## Configuration

Update the following variables before running the script:

```python
email = "<email>"
password = "<password>"
```

Replace them with valid UPS account credentials.

## Notes

* The script uses `implicit_wait` along with a few fixed delays to allow page elements to load.
* Random typing delays are used to better simulate normal user input.
