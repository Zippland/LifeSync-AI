from notion_client import Client
from datetime import datetime, timedelta
from config import NOTION_TOKEN, DATABASE_ID, DEFINE_DATE

notion = Client(auth=NOTION_TOKEN)

def fetch_tasks_from_notion(mode="today"):
    print("Fetching tasks from Notion...\n")
    try:
        results = notion.databases.query(database_id=DATABASE_ID)
        tasks = []

        # Determine the custom date; default to today if DEFINE_DATE is not set or invalid
        if DEFINE_DATE:
            try:
                custom_date = datetime.strptime(DEFINE_DATE, '%Y-%m-%d').date()
            except ValueError:
                print("Invalid date format in DEFINE_DATE. It should be 'YYYY-MM-DD'. Using today's date instead.")
                custom_date = datetime.now().date()
        else:
            custom_date = datetime.now().date()

        # Define the date range based on the mode
        if mode == "today":
            date_end = custom_date
        elif mode == "future":
            date_end = custom_date + timedelta(days=30)
        else:
            print(f"Invalid mode: {mode}. Use 'today' for today's tasks or 'future' for tasks within the next month.")
            return []

        for row in results["results"]:
            if 'date' in row['properties']['Date'] and row['properties']['Date']['date']:
                task_date = datetime.strptime(row['properties']['Date']['date']['start'], '%Y-%m-%d').date()
                # Check if the task date falls within the defined range
                if custom_date <= task_date <= date_end:
                    task = {
                        'Name': row['properties']['Name']['title'][0]['text']['content'] if row['properties']['Name']['title'] else 'No name',
                        'Location': row['properties']['Location']['rich_text'][0]['text']['content'] if 'rich_text' in row['properties']['Location'] and row['properties']['Location']['rich_text'] else 'No Location',
                        'Description': row['properties']['Description']['rich_text'][0]['text']['content'] if 'rich_text' in row['properties']['Description'] and row['properties']['Description']['rich_text'] else 'No description',
                        'Projects': row['properties']['Projects']['rich_text'][0]['text']['content'] if 'rich_text' in row['properties']['Projects'] and row['properties']['Projects']['rich_text'] else 'No Projects',
                    }
                    # Add date to the task info only for the "future" mode
                    if mode == "future":
                        task['Date'] = task_date.strftime('%Y-%m-%d')
                    tasks.append(task)
        print(tasks)
        print("Fetching success.")
        return tasks
    except Exception as e:
        print(f"Error fetching data from Notion: {e}")
        return []
