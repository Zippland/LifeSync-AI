import smtplib
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from config import SMTP_SERVER, SMTP_PORT, EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER, DEFINE_DATE, EMAIL_TITLE

def send_email(body):
    print("Sending email...")
    try:
        # Use regular expressions to clean Markdown code block markers from the body
        cleaned_body = re.sub(r'```(?:html)?', '', body)  # Remove ``` and ```html

        # Check if DEFINE_DATE is empty; if empty, use today's date, otherwise use the custom date
        if DEFINE_DATE:
            try:
                custom_date = datetime.strptime(DEFINE_DATE, '%Y-%m-%d').strftime('%Y-%m-%d')
            except ValueError:
                print("Invalid date format in DEFINE_DATE. It should be 'YYYY-MM-DD'. Using today's date instead.")
                custom_date = datetime.now().strftime('%Y-%m-%d')
        else:
            custom_date = datetime.now().strftime('%Y-%m-%d')

        message = MIMEMultipart()
        message['From'] = EMAIL_SENDER
        message['To'] = EMAIL_RECEIVER  # Ensure the recipient address is defined
        message['Subject'] = f"{EMAIL_TITLE} {custom_date}"  # Use custom or today's date in the subject

        # Set the body to HTML format and use the cleaned body
        message.attach(MIMEText(cleaned_body, 'html'))  # Format email content as HTML

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Enable TLS
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, message.as_string())
        server.quit()
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed: Check your SMTP username and password.")
    except smtplib.SMTPException as e:
        print("SMTP error occurred: " + str(e))
    except Exception as e:
        print("An error occurred while sending the email:")
        print(e)
