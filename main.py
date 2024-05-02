import re
from src.get_task import fetch_tasks_from_notion
from src.email_notifier import send_email
from src.gpt_advice_generator import generate_advice_with_gpt
from src.get_wheather import get_weather
from datetime import datetime
from config import USERNAME, DEFINE_DATE, PRESENT_LOCATION

today_tasks = fetch_tasks_from_notion()
future_tasks = fetch_tasks_from_notion("future")
weather = get_weather()

if DEFINE_DATE:
    try:
        custom_date = datetime.strptime(DEFINE_DATE, '%Y-%m-%d').strftime('%Y-%m-%d')
    except ValueError:
        print("Invalid date format in DEFINE_DATE. It should be 'YYYY-MM-DD'. Using today's date instead.")
        custom_date = datetime.now().strftime('%Y-%m-%d')
else:
    custom_date = datetime.now().strftime('%Y-%m-%d')

no_format = ""
advice = "<!DOCTYPE html> <html lang=\"en\"> <head> <meta charset=\"UTF-8\"> <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">  <style> body { font-family: 'Arial', sans-serif; margin: 0; padding: 0; background-color: #f4f4f4; } .container { max-width: 600px; margin: auto; background: #ffffff; padding: 20px; } .header { background-color: #0088ff; color: #ffffff; padding: 10px; text-align: center; } .body { padding: 20px; color: #333333; line-height: 1.6; } .footer { background-color: #0088ff; color: #ffffff; padding: 10px; text-align: center; } .section { margin-bottom: 20px; } </style> </head> <body> <div class=\"container\"> <div class=\"header\"> <h1>Zylan's Task for "+custom_date+"</h1> </div> <div class=\"body\"> <div class=\"section\"> <h2>尊敬的"+USERNAME+"：</h2> <p>以下是您在"+PRESENT_LOCATION+" "+custom_date+" 的日常提醒邮件。</p> </div> <div class=\"section\">"
# weather
no_format_temp = re.sub(r'<body>|</body>|```html?|```', '', generate_advice_with_gpt(weather,"1"))
advice += no_format_temp
no_format += no_format_temp
advice += "</div>            <div class=\"section\"> "
# ontline of task
no_format_temp = re.sub(r'<body>|</body>|```html?|```', '', generate_advice_with_gpt(today_tasks,"2"))
advice += no_format_temp
no_format += no_format_temp
advice += "</div>            <div class=\"section\"> "
# task time map
no_format_temp = re.sub(r'<body>|</body>|```html?|```', '', generate_advice_with_gpt(today_tasks,"3"))
advice += no_format_temp
no_format += no_format_temp
advice += "</div>            <div class=\"section\"> "
# future task
no_format_temp = re.sub(r'<body>|</body>|```html?|```', '', generate_advice_with_gpt(future_tasks,"4"))
advice += no_format_temp
no_format += no_format_temp
advice += "</div>            <div class=\"section\"> "
# other advice
no_format_temp = re.sub(r'<body>|</body>|```html?|```', '', generate_advice_with_gpt(no_format,"5"))
advice += no_format_temp
# ending
advice += "</div> <p>希望今日的安排能助您高效完成任务。</p>    <p>祝您今天工作顺利，心情愉快！</p>    <p>秘书呈上</p></body></html>"
email_body = f"{advice}"
send_email(email_body)
