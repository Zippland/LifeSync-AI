from datetime import datetime
from config import USERNAME

def format_email(advice = "",ending = False):
    if advice == "":
        return "<!DOCTYPE html> <html lang=\"en\"> <head> <meta charset=\"UTF-8\"> <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">  <style> body { font-family: 'Arial', sans-serif; margin: 0; padding: 0; background-color: #f4f4f4; } .container { max-width: 600px; margin: auto; background: #ffffff; padding: 20px; } .header { background-color: #0088ff; color: #ffffff; padding: 10px; text-align: center; } .body { padding: 20px; color: #333333; line-height: 1.6; } .footer { background-color: #0088ff; color: #ffffff; padding: 10px; text-align: center; } .section { margin-bottom: 20px; } </style> </head> <body> <div class=\"container\"> <div class=\"header\"> <h1>Zylan's Schedule Task Notifier</h1> </div> <div class=\"body\"> <div class=\"section\"> <h2>尊敬的"+USERNAME+"：</h2> <p>以下是您的日常提醒邮件。</p></div><div class=\"section\"> "
    else:
        if ending == True:
            return advice + "</div> <p>希望今日的安排能助您高效完成任务。</p>    <p>祝您今天工作顺利，心情愉快！</p>    <p>秘书呈上</p></body></html>"
        return advice + "</div><div class=\"section\"> "
