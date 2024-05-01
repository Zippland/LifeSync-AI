from task_manager import fetch_tasks_from_notion
from email_notifier import send_email
from gpt_advice_generator import generate_advice_with_gpt
from get_wheather import get_weather

tasks = fetch_tasks_from_notion()
weather = get_weather()
if tasks:
    advice = generate_advice_with_gpt(weather, tasks)
    email_body = f"{advice}"
    send_email(email_body)
else:
    send_email("No tasks for today.")
