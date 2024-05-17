from notion_client import Client
from datetime import datetime, timedelta

def fetch_tasks_from_notion(custom_date, USER_NOTION_TOKEN, USER_DATABASE_ID, mode="today"):
    notion = Client(auth=USER_NOTION_TOKEN)
    print("\nFetching [ " + mode + " ] tasks from Notion...\n")
    
    try:
        results = notion.databases.query(
            database_id=USER_DATABASE_ID,
            filter={"property": "Complete",
                    "checkbox": {
                        "equals": False
                    }
                }
        )
        tasks = []

        # Define the date range based on the mode
        if mode == "today":
            date_end = custom_date
        elif mode == "future":
            date_end = custom_date + timedelta(days=30)
            custom_date += timedelta(days=1)
        else:
            print(f"Invalid mode: {mode}. Use 'today' for today's tasks or 'future' for tasks within the next month.")
            return []

        for row in results["results"]:
            if 'date' in row['properties']['Date'] and row['properties']['Date']['date']:
                date_info = row['properties']['Date']['date']
                end_datetime = datetime.fromisoformat(date_info['end']) if 'end' in date_info and date_info['end'] else None
                start_datetime = datetime.fromisoformat(date_info['start']) if 'start' in date_info and date_info['start'] else None

                end_date = end_datetime.date() if end_datetime else None
                end_time = end_datetime.time() if end_datetime else None

                start_date = start_datetime.date() if start_datetime else None
                start_time = start_datetime.time() if start_datetime else None

                task_dates = {
                    'start_date': start_date.strftime('%Y-%m-%d') if start_date else 'N/A',
                    'start_time': None if not start_time or start_time.strftime('%H:%M:%S') == '00:00:00' else start_time.strftime('%H:%M:%S'),
                    'end_date': end_date.strftime('%Y-%m-%d') if end_date else 'N/A',
                    'end_time': None if not end_time or end_time.strftime('%H:%M:%S') == '00:00:00' else end_time.strftime('%H:%M:%S')
                }

                # Check if the task date falls within the defined range
                if mode == "future":
                    if (end_date and custom_date <= end_date <= date_end) or (start_date and custom_date <= start_date <= date_end):
                        task = {
                            'Name': ''.join([part['text']['content'] for part in row['properties']['Name']['title']]) if row['properties']['Name']['title'] else 'NA',
                            'Description': row['properties']['Description']['rich_text'][0]['text']['content'] if 'rich_text' in row['properties']['Description'] and row['properties']['Description']['rich_text'] else 'NA',
                            **task_dates  # Add the date and time information to each task
                        }
                        tasks.append(task)
                else:
                    if (end_date and end_date <= date_end) or (start_date and start_date <= date_end):
                        task = {
                            'Name': ''.join([part['text']['content'] for part in row['properties']['Name']['title']]) if row['properties']['Name']['title'] else 'NA',
                            'Description': row['properties']['Description']['rich_text'][0]['text']['content'] if 'rich_text' in row['properties']['Description'] and row['properties']['Description']['rich_text'] else 'NA',
                            **task_dates  # Add the date and time information to each task
                        }
                        tasks.append(task)

        if not tasks:
            tasks.append({'Message': 'No compulsory task to do today'})

        print(tasks)
        print("Fetching success.")
        return tasks
    except Exception as e:
        print(f"Error fetching data from Notion: {e}")
        return []

# Example usage
# custom_date = datetime.now().date()
# USER_NOTION_TOKEN = 'your_notion_token'
# USER_DATABASE_ID = 'your_database_id'
# fetch_tasks_from_notion(custom_date, USER_NOTION_TOKEN, USER_DATABASE_ID)
