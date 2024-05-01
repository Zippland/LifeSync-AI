# Notion config
NOTION_TOKEN = "your_notion_api_key"
DATABASE_ID = "your_task_datebase_id"

# Mailbox config
SMTP_SERVER = ""
SMTP_PORT = 587  # Default to 587 if not specified
EMAIL_SENDER = "sender_email@example.com"
EMAIL_PASSWORD = "sender_pasword"
EMAIL_RECEIVER = "receiver_email@example.com"

# OpenAI GPT api
OPENAI_API_KEY = "your_openai_api_key"
GPT_VERSION = "gpt-3.5-turbo"

# wheather api
OPENWEATHER_API_KEY = "your_openweather_api_key"

# personal information
SCHEDUAL_PROMPT = "Wake up at 8:00, go to bed at 22:00, two hours of fitness from 19:00-21:00" # If the daily habitual arrangement is not interrupted
USERNAME = "Zylan" # what GPT calls you
USER_CAREER = ""
PRESENT_LOCATION = "Canberra" # Geolocation settings for weather notifications

# hyper parameter
DEFINE_DATE = "" # Select the date you need to schedule, the format is "YYYY-MM-DD", if it is empty it is today
EMAIL_TITTLE = "Zylan's Schedule for" # The title of the email, which will be immediately followed by the date
