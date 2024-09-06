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
                end_datetime = datetime.fromisoformat(date_info['end']) if 'end' in date_info and date_info['end'] else None
                start_datetime = datetime.fromisoformat(date_info['start']) if 'start' in date_info and date_info['start'] else None

                end_date = end_datetime.date() if end_datetime else None
                start_date = start_datetime.date() if start_datetime else None

                # 获取紧急程度
                urgency_level = row['properties']['紧急程度']['select']['name'] if '紧急程度' in row['properties'] and row['properties']['紧急程度']['select'] else 'NA'

                # 获取完整页面信息
                page_id = row['id']
                page_details = notion.pages.retrieve(page_id=page_id)

                task = {
                    'Name': ''.join([part['text']['content'] for part in row['properties']['Name']['title']]) if row['properties']['Name']['title'] else 'NA',
                    'Description': row['properties']['Description']['rich_text'][0]['text']['content'] if 'rich_text' in row['properties']['Description'] and row['properties']['Description']['rich_text'] else 'NA',
                    'Urgency Level': urgency_level,
                    'Start Date': start_date.strftime('%Y-%m-%d') if start_date else 'N/A',
                    'End Date': end_date.strftime('%Y-%m-%d') if end_date else 'N/A'
                }

                # 分类任务
                if end_date and end_date < today:
                    tasks["today_due"].append(task)
                elif end_date == today:
                    tasks["today_due"].append(task)
                elif start_date and start_date <= today and (not end_date or end_date > today):
                    tasks["in_progress"].append(task)
                elif start_date and today < start_date <= future_date:
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
