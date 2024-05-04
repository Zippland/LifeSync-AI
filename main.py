import pytz
from src.email.format_email import format_email
from src.get_task.task_notion import fetch_tasks_from_notion
from src.email.email_notifier import send_email
from src.gpt_advice_generator import generate_advice_with_gpt
from src.get_wheather import get_weather
from datetime import datetime
from config import DEFINE_DATE, TIME_ZONE

# Determine the custom date; default to today if DEFINE_DATE is not set or invalid
if DEFINE_DATE:
    try:
        custom_date = datetime.strptime(DEFINE_DATE, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format in DEFINE_DATE. It should be 'YYYY-MM-DD'. Using today's date instead.")
        custom_date = datetime.now().date()
else:
    # Get the current time in UTC, and then convert to the specified UTC offset
    utc_now = datetime.now(pytz.utc)
    tz = pytz.timezone('Etc/GMT-' + TIME_ZONE)
    custom_date = utc_now.astimezone(tz).date()

today_tasks = fetch_tasks_from_notion(custom_date, "today")
future_tasks = fetch_tasks_from_notion(custom_date, "future")
weather = get_weather()

no_format_advice = ""
formated_advice = format_email()

# weather
adviece_weather = generate_advice_with_gpt(weather,"1")
formated_advice += format_email(adviece_weather)
no_format_advice += adviece_weather
# ontline of task
advice_outline = generate_advice_with_gpt(today_tasks,"2")
formated_advice += format_email(advice_outline)
no_format_advice += advice_outline
# task time stamp
advice_timestamp = generate_advice_with_gpt(today_tasks,"3")
formated_advice += format_email(advice_timestamp)
no_format_advice += advice_timestamp
# future task
advice_future = generate_advice_with_gpt(future_tasks,"4")
formated_advice += format_email(advice_future)
no_format_advice += advice_future
# other advice
advice_others = generate_advice_with_gpt(no_format_advice,"5")
formated_advice += format_email(advice_others,True)


email_body = f"{formated_advice}"
send_email(email_body)
