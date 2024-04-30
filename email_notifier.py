import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from config import SMTP_SERVER, SMTP_PORT, EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER, DEFINE_DATE

def send_email(body):
    print("Sending email...")
    try:
        # 判断 DEFINE_DATE 是否为空，如果为空则默认为今天的日期，否则使用自定义日期
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
        message['To'] = EMAIL_RECEIVER  # 确保已定义收件人地址
        message['Subject'] = f"Zylan's task for {custom_date}"  # 使用自定义日期或今天的日期在主题中

        # 将正文设置为Markdown格式
        message.attach(MIMEText(body, 'plain'))  # 如果服务器支持可以尝试使用 'markdown'

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # 启用TLS
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, message.as_string())
        server.quit()
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError as e:
        print("Failed to authenticate with the SMTP server. Check your username and password.")
        print(e)
    except Exception as e:
        print("An error occurred while sending the email:")
        print(e)
