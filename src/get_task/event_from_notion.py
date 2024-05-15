from notion_client import Client
from datetime import datetime, timedelta

def fetch_event_from_notion(custom_date, USER_NOTION_TOKEN, USER_DATABASE_ID):
    notion = Client(auth=USER_NOTION_TOKEN)
    print("\nFetching tasks from Notion...\n")
    
    try:
        results = notion.databases.query(
            database_id=USER_DATABASE_ID,
        )
        tasks = []

        # Define the date range based on the mode
        date_end = custom_date + timedelta(days=14)
        custom_date += timedelta(days=1)

        for row in results["results"]:
            if 'Date' in row['properties'] and row['properties']['Date']['date']:
                date_info = row['properties']['Date']['date']
                # Fetch the date and time properties
                start_date = date_info.get('start')
                end_date = date_info.get('end')

                # Convert to datetime if time component is present
                start_datetime = datetime.fromisoformat(start_date) if start_date else None
                end_datetime = datetime.fromisoformat(end_date) if end_date else None
                
                event_date = start_datetime.date() if start_datetime else None
                
                # Check if the task date falls within the defined range
                if custom_date <= event_date <= date_end:
                    task = {
                        'Name': ''.join([part['text']['content'] for part in row['properties']['Name']['title']]) if row['properties']['Name']['title'] else 'NA',
                        'Description': row['properties']['Description']['rich_text'][0]['text']['content'] if 'rich_text' in row['properties']['Description'] and row['properties']['Description']['rich_text'] else 'NA',
                        'Start Date': start_date.split('T')[0] if start_date else 'NA',
                        'End Date': end_date.split('T')[0] if end_date else 'NA',
                        'Start Time': start_datetime.time() if start_datetime and 'T' in start_date else 'NA',
                        'End Time': end_datetime.time() if end_datetime and 'T' in end_date else 'NA'
                    }
                    tasks.append(task)
        if not tasks:
            tasks = [{'Name': 'No compulsory event in a month', 'Description': 'NA', 'Start Date': 'NA', 'End Date': 'NA', 'Start Time': 'NA', 'End Time': 'NA'}]
            
        print(tasks)
        print("Fetching success.")
        return tasks
    except Exception as e:
        print(f"Error fetching data from Notion: {e}")
        return []
