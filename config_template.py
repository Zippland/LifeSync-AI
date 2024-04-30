import os

# Notion config
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
DATABASE_ID = os.getenv('DATABASE_ID')

# Mailbox config
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))  # Default to 587 if not specified
EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER')

# OpenAI GPT api
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GPT_VERSION = "gpt-3.5-turbo"
USERNAME = os.getenv('USERNAME')  # The name you want GPT to call you

# hyper parameter
DEFINE_DATE = os.getenv('DEFINE_DATE') #选择需要计划的日期，格式为 "YYYY-MM-DD"，如果为空就是今天
SCHEDUAL_PROMPT = os.getenv('SCHEDUAL_PROMPT') # 如果不被打断的日常习惯安排
