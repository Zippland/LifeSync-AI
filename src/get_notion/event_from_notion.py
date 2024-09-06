from notion_client import Client
from datetime import datetime, timedelta

def fetch_event_from_notion(custom_date, USER_NOTION_TOKEN, USER_DATABASE_ID):
    notion = Client(auth=USER_NOTION_TOKEN)
    print("\nFetching events from Notion...\n")
    
    try:
        results = notion.databases.query(
            database_id=USER_DATABASE_ID,
        )
        
        # 初始化两类事件列表
        events = {
            "in_progress": [],
            "upcoming": []
        }

        today = custom_date
        date_end = custom_date + timedelta(days=30)

        for row in results["results"]:
            if 'Date' in row['properties'] and row['properties']['Date']['date']:
                date_info = row['properties']['Date']['date']
                start_date = date_info.get('start')
                end_date = date_info.get('end')

                start_datetime = datetime.fromisoformat(start_date) if start_date else None
                end_datetime = datetime.fromisoformat(end_date) if end_date else None

                event_start_date = start_datetime.date() if start_datetime else None
                event_end_date = end_datetime.date() if end_datetime else None

                event = {
                    'Name': ''.join([part['text']['content'] for part in row['properties']['Name']['title']]) if row['properties']['Name']['title'] else 'NA',
                    'Description': row['properties']['Description']['rich_text'][0]['text']['content'] if 'rich_text' in row['properties']['Description'] and row['properties']['Description']['rich_text'] else 'NA',
                    'Location': row['properties']['Location']['rich_text'][0]['text']['content'] if 'rich_text' in row['properties']['Location'] and row['properties']['Location']['rich_text'] else 'NA',
                    'Start Date': start_date.split('T')[0] if start_date else 'NA',
                    'Start Time': start_datetime.time() if start_datetime and 'T' in start_date else 'NA',
                    'End Date': end_date.split('T')[0] if end_date else 'NA',
                    'End Time': end_datetime.time() if end_datetime and 'T' in end_date else 'NA'
                }

                # 分类事件
                if event_start_date and event_start_date <= today and (not event_end_date or event_end_date >= today):
                    # 没有结束日期，且开始日期是今天的事件也算作 "in_progress"
                    if not event_end_date and event_start_date == today:
                        events["in_progress"].append(event)
                    elif event_end_date and event_end_date >= today:
                        events["in_progress"].append(event)
                elif event_start_date and today < event_start_date <= date_end:
                    events["upcoming"].append(event)

        # 如果某一类事件为空，添加提示信息
        if not events["in_progress"]:
            events["in_progress"].append({'Message': 'No events currently in progress.'})
        if not events["upcoming"]:
            events["upcoming"].append({'Message': 'No upcoming events within the next 30 days.'})

        print(events)
        print("Fetching success.")
        return events
    except Exception as e:
        print(f"Error fetching data from Notion: {e}")
        return {"in_progress": [], "upcoming": []}

# Example usage
# custom_date = datetime.now().date()
# USER_NOTION_TOKEN = 'your_notion_token'
# USER_DATABASE_ID = 'your_database_id'
# fetch_event_from_notion(custom_date, USER_NOTION_TOKEN, USER_DATABASE_ID)
