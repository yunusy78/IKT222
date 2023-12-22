import requests
from discordwebhook import Discord
from bs4 import BeautifulSoup
import time

def check_jonas_login(response_text):
    soup = BeautifulSoup(response_text, 'html.parser')
    login_message = soup.find('div', {'id': 'responseMessage', 'class': 'mt-4'}).text
    return "Jonas Dahl" in login_message

def send_discord_notification(webhook_url, content):
    webhook = Discord(url=webhook_url)
    webhook.post(content=content)

discord_webhook_url = "https://discord.com/api/webhooks/1182257428696420403/fHFJfsmG5UV1mu0WTgmaQpCLoy9-CgcgpWXUDZM94Umc80yDXAgsbxGdV3oANVSxJddc"

while True:
    wireguard_check_url = "https://portal.regjeringen.uiaikt.no/"

    try:
        response = requests.get(wireguard_check_url)
        response.raise_for_status()

        login_status = check_jonas_login(response.text)

        if login_status:
            message = "Jonas Dahl logged in to check WireGuard credentials!"
            send_discord_notification(discord_webhook_url, message)
        else:
            # Jonas did not log in, send an error message through the webhook
            error_message = "Jonas Dahl did not log in as expected."
            send_discord_notification(discord_webhook_url, error_message)

            # If the Result value is "incorrect", perform specific actions
            if "Result: incorrect" in response.text:
                print("Incorrect result detected. Performing additional actions...")
                # Perform additional actions here
                # For example:
                #   - Make a request to another website.
                #   - Send an email.
                #   - Use another Discord webhook.

    except requests.exceptions.RequestException as e:
        # If an error occurred during the request, send the error through the webhook
        error_message = f"Request error: {e}"
        send_discord_notification(discord_webhook_url, error_message)

    # Set the interval based on your needs (for example, 3600 seconds to check every hour)
    time.sleep(60)