def format_email(advice, USER_NAME):
    return f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f5f5f7;
                color: #1d1d1f;
            }}
            .container {{
                width: 100%;
                max-width: 600px;
                margin: 0 auto;
                background-color: #ffffff;
                border-radius: 12px;
                overflow: hidden;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                background-color: #007aff;
                color: #ffffff;
                padding: 30px 20px;
                text-align: center;
                border-bottom: 1px solid #e5e5ea;
            }}
            .header h1 {{
                margin: 0;
                font-size: 32px;
                font-weight: 700;
                letter-spacing: -0.5px;
            }}
            .body {{
                padding: 30px 20px;
            }}
            .body h1 {{
                font-size: 24px;
                margin-bottom: 20px;
                font-weight: bold;
                color: #1d1d1f;
            }}
            .body p {{
                line-height: 1.6;
                margin-bottom: 20px;
                color: #3a3a3c;
            }}
            .advice {{
                line-height: 1.6;
                margin-bottom: 20px;
                background-color: #f5f5f7;
                padding: 15px;
                border-radius: 8px;
                color: #1d1d1f;
            }}
            .footer {{
                background-color: #f5f5f7;
                color: #8e8e93;
                padding: 20px;
                text-align: center;
                border-top: 1px solid #e5e5ea;
            }}
            .footer p {{
                margin: 0;
                font-size: 14px;
            }}
            .footer small {{
                display: block;
                margin-top: 5px;
                font-size: 12px;
                color: #aeaeb2;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Header -->
            <div class="header">
                <h1>日程提醒</h1>
            </div>
            <!-- Body -->
            <div class="body">
                <h1>尊敬的{USER_NAME}：</h1>
                <p>以下是您的日常提醒邮件。</p>
                <div class="advice">
                    {advice}
                </div>
                <p>希望今日的安排能助您高效完成任务。</p>
                <p>祝您今天工作顺利，心情愉快！</p>
            </div>
            <!-- Footer -->
            <div class="footer">
                <p>秘书呈上</p>
                <small>© 2024 秘书团队. 保留所有权利。</small>
            </div>
        </div>
    </body>
    </html>
    """

# Example usage:
# email_body = format_email("您的今日日程如下：<ul><li>9:00 AM - 会议</li><li>11:00 AM - 项目讨论</li></ul>", "张三")
