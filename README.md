# Selenium Web Automation Script for Bstack Demo

This Python script demonstrates how to automate web interactions using Selenium WebDriver to navigate the Bstack Demo website, log in, and perform basic actions.

## Requirements

Before running this script, you need to have the following installed:

- [Python](https://www.python.org/downloads/)
- [Selenium WebDriver](https://pypi.org/project/selenium/)
- [Chrome WebDriver](https://sites.google.com/chromium.org/driver/)
  
  You can install Selenium and Chrome WebDriver using pip:
  

## Usage

1. Clone the repository or download the script to your local machine.

2. Open the script in a text editor and update the Chrome WebDriver path (if necessary) and any other configurations.

3. Run the script:

4. The script will open a Chrome browser, navigate to the Bstack Demo website, and perform the following actions:
- Click on the "Sign In" button.
- Enter a username and password.
- Submit the login form.
- Verify that the logout button is displayed, indicating a successful login.

5. After completing the actions, the script will close the browser.

## Customization

You can customize this script for your specific needs by modifying the following:

- Website URL: Change the URL in `driver.get()` to navigate to a different website.
- Username and Password: Modify the username and password values as needed.
- Locators: Adjust the CSS selectors or element locators to match the structure of the web page you are automating.
