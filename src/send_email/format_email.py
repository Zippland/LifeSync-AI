def format_email(advice, USER_NAME, title, time_of_day="morning"):
    # 根据时间选择问候语
    greeting = "早安" if time_of_day == "morning" else "晚安"
    
    return f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            /* Base Styles */
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                line-height: 1.6;
                color: #1a2b42;
                background-color: #f5f7fa;
                margin: 0;
                padding: 0;
            }}

            .container {{
                max-width: 700px;
                margin: 0 auto;
                background: #ffffff;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                border-radius: 12px;
                overflow: hidden;
            }}

            /* Header */
            .header {{
                background-color: #0060e6;  /* 设置背景色为蓝色 */
                padding: 32px 24px;
                text-align: center;
            }}

            .header h1 {{
                margin: 0;
                font-size: 28px;
                font-weight: 600;
                letter-spacing: 0.5px;
                color: white;
                text-align: center;
            }}

            .header p {{
                margin: 8px 0 0 0;
                color: rgba(255, 255, 255, 0.9);
                font-size: 16px;
                text-align: center;
            }}

            /* Content */
            .content {{
                padding: 24px;
            }}

            /* Sections */
            .section {{
                margin-bottom: 32px;
                background: #ffffff;
                border-radius: 8px;
                border: 1px solid #e5e9f0;
                overflow: hidden;
            }}

            .section-header {{
                background: #f8f9fd;
                padding: 16px 20px;
                border-bottom: 1px solid #e5e9f0;
            }}

            .section-header h2 {{
                margin: 0;
                font-size: 20px;
                color: #0060e6;
                font-weight: 600;
            }}

            .section-content {{
                padding: 20px;
            }}

            /* Overview Card */
            .overview-card {{
                background: linear-gradient(135deg, #f0f7ff 0%, #e6f0ff 100%);
                border-radius: 8px;
                padding: 20px;
                margin-bottom: 24px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            }}

            .overview-card h3 {{
                margin: 0 0 12px 0;
                font-size: 18px;
                color: #0060e6;
            }}

            .overview-card p {{
                margin: 0;
                color: #2c4b6e;
                font-size: 16px;
                line-height: 1.6;
            }}

            /* Weather Display */
            .weather-info {{
                background: linear-gradient(135deg, #ffffff 0%, #f8f9fd 100%);
                border-radius: 8px;
                padding: 20px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
                margin-bottom: 24px;
            }}

            .weather-info h3 {{
                margin: 0 0 16px 0;
                font-size: 18px;
                color: #0060e6;
            }}

            .weather-summary {{
                color: #1a2b42;
                font-size: 16px;
                line-height: 1.6;
                margin-bottom: 16px;
            }}

            .weather-advice {{
                color: #2c4b6e;
                font-size: 15px;
                background: #f0f7ff;
                padding: 12px 16px;
                border-radius: 6px;
                border-left: 4px solid #0060e6;
            }}

            /* Timeline */
            .timeline {{
                position: relative;
                padding: 0;
                margin: 0;
                list-style: none;
            }}

            .timeline-item {{
                display: flex;
                align-items: flex-start;
                margin-bottom: 20px;
                position: relative;
            }}

            .timeline-item:last-child {{
                margin-bottom: 0;
            }}

            .timeline-time {{
                flex: 0 0 60px;
                color: #0060e6;
                font-weight: 600;
                font-size: 15px;
                padding-right: 10px;
                text-align: right;
                position: relative;
            }}

            .timeline-time::after {{
                content: '';
                position: absolute;
                right: -6px;
                top: 8px;
                width: 12px;
                height: 12px;
                border-radius: 50%;
                background: #ffffff;
                border: 2px solid #0060e6;
            }}

            .timeline-content {{
                flex: 1;
                padding-left: 12px;
                border-left: 2px solid #e5e9f0;
                min-height: 40px;
            }}

            .timeline-title {{
                margin: 0;
                font-size: 16px;
                font-weight: 600;
                color: #1a2b42;
            }}

            .timeline-desc {{
                margin: 8px 0 0 0;
                font-size: 14px;
                color: #4a5568;
            }}

            /* Task Labels */
            .task-label {{
                display: inline-block;
                padding: 3px 8px;
                border-radius: 4px;
                font-size: 12px;
                font-weight: 500;
                margin-left: 8px;
                vertical-align: middle;
            }}

            .task-priority-high {{
                background-color: #fee2e2;
                color: #ef4444;
            }}

            .task-priority-medium {{
                background-color: #fef3c7;
                color: #f59e0b;
            }}

            .task-priority-low {{
                background-color: #ecfdf5;
                color: #10b981;
            }}

            /* Important Notes */
            .important-notes {{
                background: linear-gradient(135deg, #fffbeb 0%, #fff7ed 100%);
                border-radius: 8px;
                padding: 20px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            }}

            .important-notes h3 {{
                margin: 0 0 12px 0;
                font-size: 18px;
                color: #b45309;
            }}

            .important-notes ul {{
                margin: 0;
                padding-left: 20px;
            }}

            .important-notes li {{
                margin-bottom: 8px;
                color: #92400e;
                font-size: 15px;
                line-height: 1.5;
            }}

            .important-notes li:last-child {{
                margin-bottom: 0;
            }}

            /* Footer */
            .footer {{
                background: #f8f9fd;
                padding: 20px;
                text-align: center;
                border-top: 1px solid #e5e9f0;
            }}

            .footer p {{
                margin: 0;
                color: #4a5568;
                font-size: 14px;
                line-height: 1.6;
            }}

            .sign-off {{
                font-style: italic;
                color: #0060e6;
                margin-top: 8px;
            }}

            @media screen and (max-width: 600px) {{
                .container {{
                    margin: 0;
                    border-radius: 0;
                }}

                .timeline-time {{
                    flex: 0 0 80px;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>{title}</h1>
                <p>{greeting}，{USER_NAME}</p>
            </div>
            <div class="content">
                {advice}
                <p class="sign-off">祝您度过愉快的一天！</p>
            </div>
            <div class="footer">
                <p>您的AI助理随时为您服务</p>
                <p style="margin-top: 8px; font-size: 12px;">© 2024 AI Assistant. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    """