from src.task_manager import fetch_tasks_from_notion
from src.email_notifier import send_email
from src.gpt_advice_generator import generate_advice_with_gpt
from src.get_wheather import get_weather

today_tasks = fetch_tasks_from_notion()
future_tasks = fetch_tasks_from_notion("future")
weather = get_weather()

advice = generate_advice_with_gpt(weather, today_tasks,future_tasks)
email_body = f"{advice}"
send_email(email_body)
