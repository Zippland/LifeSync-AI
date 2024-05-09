import pytz
from src.send_email.format_email import format_email
from src.get_task.task_from_notion import fetch_tasks_from_notion
from src.send_email.email_notifier import send_email
from src.ai_operations.gpt_email_advice import email_advice_with_ai
from src.get_wheather import get_weather
from datetime import datetime
from src.get_env.env_from_notion import get_user_env_vars

# Get the current time in UTC, and then convert to the specified UTC offset
utc_now = datetime.now(pytz.utc)
user_data = get_user_env_vars()

for user_id in user_data:
    user_notion_token = user_data[user_id]["USER_NOTION_TOKEN"]
    user_database_id = user_data[user_id]["USER_DATABASE_ID"]
    gpt_version = "gpt-3.5-turbo"
    present_location = user_data[user_id]["PRESENT_LOCATION"]
    user_name = user_data[user_id]["USER_NAME"]
    user_career = user_data[user_id]["USER_CAREER"]
    schedule_prompt = user_data[user_id]["SCHEDULE_PROMPT"]
    custom_date = utc_now.astimezone(pytz.timezone('Etc/GMT-' + user_data[user_id]["TIME_ZONE"])).date()

    today_tasks = fetch_tasks_from_notion(custom_date, user_notion_token, user_database_id, "today")
    future_tasks = fetch_tasks_from_notion(custom_date, user_notion_token, user_database_id, "future")
    weather = get_weather(present_location)

    no_format_advice = ""
    formated_advice = format_email("", user_name)

    # # weather
    # adviece_weather = email_advice_with_ai("1", weather, gpt_version, present_location, user_career)
    # formated_advice += format_email(adviece_weather)
    # no_format_advice += adviece_weather
    # # ontline of task
    # advice_outline = email_advice_with_ai("2", today_tasks, gpt_version, present_location, user_career)
    # formated_advice += format_email(advice_outline)
    # no_format_advice += advice_outline
    # # task time stamp
    # advice_timestamp = email_advice_with_ai("3", today_tasks, gpt_version, present_location, user_career, schedule_prompt)
    # formated_advice += format_email(advice_timestamp)
    # no_format_advice += advice_timestamp
    # # future task
    # advice_future = email_advice_with_ai("4", future_tasks, gpt_version, present_location, user_career)
    # formated_advice += format_email(advice_future)
    # no_format_advice += advice_future
    # # other advice
    # advice_others = email_advice_with_ai("5", no_format_advice, gpt_version, present_location, user_career)
    # formated_advice += format_email(advice_others, USER_NAME = user_data[user_id]["USER_NAME"], ending = True)


    email_body = f"{formated_advice}"
    print(email_body)
