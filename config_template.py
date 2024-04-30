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
GPT_VERSION = "gpt-4-turbo"
USERNAME = os.getenv('USERNAME')  # The name you want GPT to call you
