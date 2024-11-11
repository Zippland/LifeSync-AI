from notion_client import Client
from datetime import datetime, timedelta
import pytz

def fetch_event_from_notion(custom_date, USER_NOTION_TOKEN, USER_DATABASE_ID, timezone_offset=8, include_completed=False):
    """
    从Notion获取事件数据，并根据日期精确分类
    
    Parameters:
    - custom_date: 指定日期 (datetime.date)
    - USER_NOTION_TOKEN: Notion API Token
    - USER_DATABASE_ID: 数据库ID
    - timezone_offset: 时区偏移量（小时）
    - include_completed: 是否包含已完成事件
    """
    notion = Client(auth=USER_NOTION_TOKEN)
    print("\nFetching events from Notion...\n")
    
    try:
        # 创建时区对象
        tz = pytz.FixedOffset(timezone_offset * 60)  # 转换为分钟
        
        # 设置关键时间点
        today = custom_date  # 这是一个 date 对象
        tomorrow = today + timedelta(days=1)  # 这也是一个 date 对象
        future_date = today + timedelta(days=30)  # 这也是一个 date 对象
        current_time = datetime.now(tz)

        # 获取今天的开始和结束时间点
        today_start = datetime.combine(today, datetime.min.time()).replace(tzinfo=tz)
        today_end = datetime.combine(tomorrow, datetime.min.time()).replace(tzinfo=tz)
        
        # 初始化事件字典
        events = {
            "in_progress": [],     # 今天正在进行的事件
            "tomorrow": [],        # 明天的事件
            "upcoming": [],        # 未来（后天及以后）的事件
            "completed": []        # 已完成的事件（仅限今天）
        }

        results = notion.databases.query(
            database_id=USER_DATABASE_ID,
            filter={
                "property": "Date",
                "date": {
                    "is_not_empty": True
                }
            }
        )

        for row in results["results"]:
            if 'Date' in row['properties'] and row['properties']['Date']['date']:
                date_info = row['properties']['Date']['date']
                
                try:
                    # 解析开始和结束时间
                    start_date = date_info.get('start')
                    end_date = date_info.get('end')
                    
                    start_datetime = datetime.fromisoformat(start_date).astimezone(tz) if start_date else None
                    end_datetime = datetime.fromisoformat(end_date).astimezone(tz) if end_date else (start_datetime + timedelta(hours=1) if start_datetime else None)

                    event = {
                        'Name': ''.join([part['text']['content'] for part in row['properties']['Name']['title']]) if row['properties']['Name']['title'] else 'NA',
                        'Description': row['properties']['Description']['rich_text'][0]['text']['content'] if 'rich_text' in row['properties']['Description'] and row['properties']['Description']['rich_text'] else 'NA',
                        'Location': row['properties']['Location']['rich_text'][0]['text']['content'] if 'rich_text' in row['properties']['Location'] and row['properties']['Location']['rich_text'] else 'NA',
                        'Start Date': start_datetime.strftime('%Y-%m-%d') if start_datetime else 'NA',
                        'Start Time': start_datetime.strftime('%H:%M') if start_datetime else 'NA',
                        'End Date': end_datetime.strftime('%Y-%m-%d') if end_datetime else 'NA',
                        'End Time': end_datetime.strftime('%H:%M') if end_datetime else 'NA',
                        'Status': 'Completed' if end_datetime and end_datetime < current_time else 'In Progress'
                    }

                    # 更精确的时间分类
                    if include_completed and end_datetime and today_start <= end_datetime < today_end:
                        # 今天已完成的事件
                        events["completed"].append(event)
                        continue

                    if start_datetime:
                        event_date = start_datetime.date()  # 获取日期部分
                        
                        if event_date == today:
                            # 今天的事件
                            if not end_datetime or end_datetime >= current_time:
                                events["in_progress"].append(event)
                        elif event_date == tomorrow:  # 直接比较date对象
                            # 明天的事件
                            events["tomorrow"].append(event)
                        elif tomorrow < event_date <= future_date:  # 直接比较date对象
                            # 后天及以后的事件
                            events["upcoming"].append(event)

                except Exception as e:
                    print(f"Error processing event: {row.get('properties', {}).get('Name', {}).get('title', [{'text': {'content': 'Unknown'}}])[0]['text']['content']}")
                    print(f"Error details: {str(e)}")
                    continue

        print("Events fetched successfully with date categorization.")
        
        # 打印调试信息
        print(f"\nToday's date: {today}")
        print(f"Tomorrow's date: {tomorrow}")
        for key in events:
            if events[key]:
                print(f"\n{key} events:")
                for event in events[key]:
                    print(f"- {event['Name']} ({event['Start Date']})")
            else:
                print(f"\nNo {key} events found.")

        return events
        
    except Exception as e:
        print(f"Error fetching data from Notion: {e}")
        return {
            "in_progress": [],
            "tomorrow": [],
            "upcoming": [],
            "completed": []
        }