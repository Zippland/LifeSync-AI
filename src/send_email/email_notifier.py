import requests
import re
from datetime import datetime
from config import MAILGUN_API_KEY, MAILGUN_DOMAIN, EMAIL_RECEIVER, DEFINE_DATE, EMAIL_TITLE

def send_email(body):
    print("Sending email...")
    try:
        # 使用正则表达式清理body中的Markdown代码块标记
        cleaned_body = re.sub(r'```(?:html)?', '', body)  # 删除```和```html

        # 判断 DEFINE_DATE 是否为空，如果为空则默认为今天的日期，否则使用自定义日期
        if DEFINE_DATE:
            try:
                custom_date = datetime.strptime(DEFINE_DATE, '%Y-%m-%d').strftime('%Y-%m-%d')
            except ValueError:
                print("Invalid date format in DEFINE_DATE. It should be 'YYYY-MM-DD'. Using today's date instead.")
                custom_date = datetime.now().strftime('%Y-%m-%d')
        else:
            custom_date = datetime.now().strftime('%Y-%m-%d')

        # 配置邮件参数
        data = {
            "from": f"LifeSync-AI <mailgun@{MAILGUN_DOMAIN}>",
            "to": [EMAIL_RECEIVER],
            "subject": f"{EMAIL_TITLE} {custom_date}",
            "html": cleaned_body
        }

        # 发送邮件请求到 Mailgun API
        response = requests.post(
            f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
            auth=("api", MAILGUN_API_KEY),
            data=data
        )
        
        if response.status_code == 200:
            print("Email sent successfully!")
        else:
            print(f"Failed to send email. Status code: {response.status_code}, Response: {response.text}")

    except Exception as e:
        print("An error occurred while sending the email:")
        print(e)

