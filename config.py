from dotenv import load_dotenv
import os

env_file_loaded = load_dotenv()

# Notion config
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

# Mailbox config
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")
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
TIME_ZONE = os.getenv("TIME_ZONE")

# Hyper parameters
DEFINE_DATE = ""
EMAIL_TITLE = "Zylan's Schedule for"
