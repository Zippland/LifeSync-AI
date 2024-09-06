from notion_client import Client
from datetime import datetime, timedelta

def fetch_tasks_from_notion(custom_date, USER_NOTION_TOKEN, USER_DATABASE_ID):
    notion = Client(auth=USER_NOTION_TOKEN)
    print("\nFetching tasks from Notion...\n")
    
    try:
        results = notion.databases.query(
            database_id=USER_DATABASE_ID,
            filter={"property": "Complete",
                    "checkbox": {
                        "equals": False
                    }
                }
        )
        
        # 初始化三类任务列表
        tasks = {
            "today_due": [],
            "in_progress": [],
            "future": []
        }

        today = custom_date
        future_date = today + timedelta(days=30)

        for row in results["results"]:
            if 'date' in row['properties']['Date'] and row['properties']['Date']['date']:
                date_info = row['properties']['Date']['date']
                
                # 获取精确到分钟的开始和结束时间
                end_datetime = datetime.fromisoformat(date_info['end']) if 'end' in date_info and date_info['end'] else None
                start_datetime = datetime.fromisoformat(date_info['start']) if 'start' in date_info and date_info['start'] else None

                end_time_str = end_datetime.strftime('%Y-%m-%d %H:%M') if end_datetime else None
                start_time_str = start_datetime.strftime('%Y-%m-%d %H:%M') if start_datetime else None

                # 获取紧急程度
                urgency_level = row['properties']['紧急程度']['select']['name'] if '紧急程度' in row['properties'] and row['properties']['紧急程度']['select'] else 'NA'

                # 提取并清理Description富文本内容
                description = ''
                if 'rich_text' in row['properties']['Description'] and row['properties']['Description']['rich_text']:
                    description = ''.join([part['text']['content'] for part in row['properties']['Description']['rich_text']])
                    # 清理特殊字符
                    description = description.replace('\n', ' ').replace('\xa0', ' ').strip()

                task = {
                    'Name': ''.join([part['text']['content'] for part in row['properties']['Name']['title']]) if row['properties']['Name']['title'] else 'NA',
                    'Description': description if description else 'NA',
                    'Urgency Level': urgency_level,
                    'Start Time': start_time_str if start_time_str else 'N/A',
                    'End Time': end_time_str if end_time_str else 'N/A'
                }

                # 分类任务
                if end_datetime and end_datetime.date() < today:
                    tasks["today_due"].append(task)
                elif end_datetime and end_datetime.date() == today:
                    tasks["today_due"].append(task)
                elif start_datetime and start_datetime.date() <= today and (not end_datetime or end_datetime.date() > today):
                    tasks["in_progress"].append(task)
                elif start_datetime and today < start_datetime.date() <= future_date:
                    tasks["future"].append(task)

        # 如果某一类任务为空，添加提示信息
        if not tasks["today_due"]:
            tasks["today_due"].append({'Message': 'No tasks due today.'})
        if not tasks["in_progress"]:
            tasks["in_progress"].append({'Message': 'No tasks in progress.'})
        if not tasks["future"]:
            tasks["future"].append({'Message': 'No tasks starting in the next 30 days.'})

        print(tasks)
        print("Fetching success.")
        return tasks
    except Exception as e:
        print(f"Error fetching data from Notion: {e}")
        return {}

# Example usage
# custom_date = datetime.now().date()
# USER_NOTION_TOKEN = 'your_notion_token'
# USER_DATABASE_ID = 'your_database_id'
# fetch_tasks_from_notion(custom_date, USER_NOTION_TOKEN, USER_DATABASE_ID)
