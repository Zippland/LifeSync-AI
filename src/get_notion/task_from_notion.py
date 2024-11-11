from notion_client import Client
from datetime import datetime, timedelta
import pytz

def fetch_tasks_from_notion(custom_date, USER_NOTION_TOKEN, USER_DATABASE_ID, timezone_offset=8, include_completed=False):
    """
    从Notion获取任务数据
    
    Parameters:
    - custom_date: 指定日期
    - USER_NOTION_TOKEN: Notion API Token
    - USER_DATABASE_ID: 数据库ID
    - timezone_offset: 时区偏移量（小时）
    - include_completed: 是否包含已完成任务
    
    Returns:
    - tasks: 包含不同类型任务的字典，如果某类任务为空则返回空列表而不是消息
    """
    notion = Client(auth=USER_NOTION_TOKEN)
    print("\nFetching tasks from Notion...\n")
    
    try:
        # 创建时区对象
        tz = pytz.FixedOffset(timezone_offset * 60)  # 转换为分钟
        
        # 获取今天的开始和结束时间点
        today = custom_date
        tomorrow = today + timedelta(days=1)
        today_start = datetime.combine(today, datetime.min.time()).replace(tzinfo=tz)
        today_end = datetime.combine(tomorrow, datetime.min.time()).replace(tzinfo=tz)

        # 查询数据库
        filter_conditions = {
            "and": [
                {
                    "property": "Date",
                    "date": {
                        "is_not_empty": True
                    }
                }
            ]
        }

        results = notion.databases.query(
            database_id=USER_DATABASE_ID,
            filter=filter_conditions
        )
        
        # 初始化任务列表
        tasks = {
            "today_due": [],      # 今天到期的任务
            "in_progress": [],    # 正在进行的任务
            "future": [],         # 未来的任务
            "completed": []       # 已完成的任务（仅今天完成的）
        }

        future_date = today + timedelta(days=30)
        
        for row in results["results"]:
            if 'date' in row['properties']['Date'] and row['properties']['Date']['date']:
                # 获取任务的最后编辑时间，并转换为用户时区
                last_edited_time = datetime.fromisoformat(row['last_edited_time'].replace('Z', '+00:00')).astimezone(tz)
                
                date_info = row['properties']['Date']['date']
                
                # 获取开始和结束时间
                end_datetime = datetime.fromisoformat(date_info['end']).astimezone(tz) if date_info.get('end') else None
                start_datetime = datetime.fromisoformat(date_info['start']).astimezone(tz) if date_info.get('start') else None

                # 获取紧急程度
                urgency_level = row['properties']['紧急程度']['select']['name'] if '紧急程度' in row['properties'] and row['properties']['紧急程度']['select'] else 'NA'

                # 提取Description
                description = ''
                if 'rich_text' in row['properties']['Description'] and row['properties']['Description']['rich_text']:
                    description = ''.join([part['text']['content'] for part in row['properties']['Description']['rich_text']])
                    description = description.replace('\n', ' ').replace('\xa0', ' ').strip()

                # 获取完成状态
                is_completed = row['properties']['Complete']['checkbox']

                task = {
                    'Name': ''.join([part['text']['content'] for part in row['properties']['Name']['title']]) if row['properties']['Name']['title'] else 'NA',
                    'Description': description if description else 'NA',
                    'Urgency Level': urgency_level,
                    'Start Time': start_datetime.strftime('%Y-%m-%d %H:%M') if start_datetime else 'N/A',
                    'End Time': end_datetime.strftime('%Y-%m-%d %H:%M') if end_datetime else 'N/A',
                    'Completed': is_completed,
                    'Last Edited': last_edited_time.strftime('%Y-%m-%d %H:%M'),
                    'Status': 'Completed' if is_completed else 'In Progress'
                }

                # 根据完成状态和最后编辑时间分类任务
                if is_completed:
                    if include_completed and today_start <= last_edited_time < today_end:
                        tasks["completed"].append(task)
                else:
                    if end_datetime and end_datetime.date() == today:
                        tasks["today_due"].append(task)
                    elif start_datetime and start_datetime.date() <= today and (not end_datetime or end_datetime.date() > today):
                        tasks["in_progress"].append(task)
                    elif start_datetime and today < start_datetime.date() <= future_date:
                        tasks["future"].append(task)

        print("Tasks fetched successfully.")
        return tasks

    except Exception as e:
        print(f"Error fetching data from Notion: {e}")
        return {
            "today_due": [],
            "in_progress": [],
            "future": [],
            "completed": []
        }