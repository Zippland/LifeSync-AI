from dotenv import load_dotenv
import os

# 尝试加载 .env 文件，load_dotenv() 会返回一个布尔值表示加载是否成功
env_file_loaded = load_dotenv()
if env_file_loaded:
    print(".env file loaded successfully")
else:
    print(".env file not found, loading environment variables from system")

# Notion config
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

# Mailbox config
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = 587
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

# OpenAI GPT api
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GPT_VERSION = os.getenv("GPT_VERSION")

# Weather API
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Personal information
SCHEDULE_PROMPT =  os.getenv("SCHEDULE_PROMPT")
USERNAME =  os.getenv("USERNAME")
USER_CAREER =  os.getenv("USER_CAREER")
PRESENT_LOCATION = os.getenv("PRESENT_LOCATION")

# Hyper parameters
DEFINE_DATE = ""
EMAIL_TITLE = "Zylan's Schedule for"
