from notion_client import Client
from datetime import datetime, timedelta
from config import NOTION_TOKEN, DATABASE_ID

notion = Client(auth=NOTION_TOKEN)

def fetch_tasks_from_notion(custom_date, mode="today"):
    print("\nFetching [ "+mode+" ] tasks from Notion...\n")
    try:
        results = notion.databases.query(
            database_id=DATABASE_ID,
            filter={
                "property": " Complete",  
                "checkbox": {
                    "equals": False 
                }
            }
        )
        tasks = []

        # Define the date range based on the mode
        if mode == "today":
            date_end = custom_date
            custom_date -= timedelta(days=1)  # Adjusted to include today's date
        elif mode == "future":
            date_end = custom_date + timedelta(days=30)
            custom_date += timedelta(days=1)
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
                        'Date': task_date.strftime('%Y-%m-%d')  # Date added to each task
                    }
                    tasks.append(task)
        #print(tasks)
        print("Fetching success.")
        return tasks
    except Exception as e:
        print(f"Error fetching data from Notion: {e}")
        return []
