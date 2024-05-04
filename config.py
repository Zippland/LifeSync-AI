from dotenv import load_dotenv
import os

env_file_loaded = load_dotenv()

ENV_NOTION_TOKEN = os.getenv("ENV_NOTION_TOKEN")
ENV_DATABASE_ID = os.getenv("ENV_DATABASE_ID")

# Mailbox config
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")

# OpenAI GPT api
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Weather API
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")