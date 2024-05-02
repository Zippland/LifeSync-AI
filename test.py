import requests
from config import MAILGUN_API_KEY, MAILGUN_DOMAIN, EMAIL_RECEIVER

def test_mailgun():
    print("Testing Mailgun configuration...")
    data = {
        "from": f"Test User <mailgun@{MAILGUN_DOMAIN}>",
        "to": [EMAIL_RECEIVER],
        "subject": "Test Mailgun Setup",
        "text": "Hello, this is a test email to verify Mailgun setup."
    }

    response = requests.post(
        f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
        auth=("api", MAILGUN_API_KEY),
        data=data
    )

    if response.status_code == 200:
        print("Test email sent successfully!")
    else:
        print(f"Failed to send test email. Status code: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    test_mailgun()
