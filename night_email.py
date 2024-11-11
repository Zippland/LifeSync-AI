import pytz
from src.send_email.format_email import format_email
from src.get_notion.task_from_notion import fetch_tasks_from_notion
from src.send_email.email_notifier import send_email
from src.ai_operations.ai_night_advice import email_advice_with_ai
from src.get_wheather import get_weather_forecast
from datetime import datetime
from src.get_env.env_from_notion import get_user_env_vars
from src.get_notion.event_from_notion import fetch_event_from_notion

# Get the current time in UTC, and then convert to the specified UTC offset
utc_now = datetime.now(pytz.utc)
user_data = get_user_env_vars()

for user_id in user_data:
    user_notion_token = user_data[user_id]["USER_NOTION_TOKEN"]
    user_database_id = user_data[user_id]["USER_DATABASE_ID"]
    user_event_database_id = user_data[user_id]["USER_EVENT_DATABASE_ID"]
    gpt_version = user_data[user_id]["GPT_VERSION"]
    present_location = user_data[user_id]["PRESENT_LOCATION"]
    user_name = user_data[user_id]["USER_NAME"]
    user_career = user_data[user_id]["USER_CAREER"]
    schedule_prompt = user_data[user_id]["SCHEDULE_PROMPT"]
    time_zone_offset = int(user_data[user_id]["TIME_ZONE"])

    # Convert UTC time to user's local time
    local_time = utc_now.astimezone(pytz.timezone(f'Etc/GMT{"+" if time_zone_offset < 0 else "-"}{abs(time_zone_offset)}'))
    print("local_time: \n" + str(local_time))
    custom_date = local_time.date()

    tasks = fetch_tasks_from_notion(custom_date, user_notion_token, user_database_id, 
                                  time_zone_offset, include_completed=True)  # 修正变量名
    events = fetch_event_from_notion(custom_date, user_notion_token, user_event_database_id,
                                   time_zone_offset, include_completed=True)  # 修正变量名

    forecast_data = get_weather_forecast(present_location, time_zone_offset)

    data = {
        "weather": forecast_data['tomorrow'],
        # tasks
        "today_tasks": tasks["today_due"],
        "in_progress_tasks": tasks["in_progress"],
        "future_tasks": tasks["future"],
        "completed_tasks": tasks["completed"],
        # events
        "in_progress_events": events["in_progress"],
        "tomorrow_events": events["tomorrow"],     # 注意这里改成了tomorrow
        "upcoming_events": events["upcoming"],     # 后天及以后的事件
        "completed_events": events["completed"]
    }

    advice = email_advice_with_ai(data, gpt_version, present_location, user_career, local_time, schedule_prompt)
    print("Final advice:\n" + advice)

    tittle = "日程晚报"
    email_body = f"{format_email(advice, user_name, tittle,"")}"
    send_email(email_body, user_data[user_id]["EMAIL_RECEIVER"], user_data[user_id]["EMAIL_TITLE"], time_zone_offset)