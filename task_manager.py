from notion_client import Client
from datetime import datetime
from config import NOTION_TOKEN, DATABASE_ID

notion = Client(auth=NOTION_TOKEN)

def fetch_tasks_from_notion():
    print("fetching from notion...")
    try:
        results = notion.databases.query(database_id=DATABASE_ID)
        tasks = []
        today = datetime.now().date()
        for row in results["results"]:
            if 'date' in row['properties']['Date'] and row['properties']['Date']['date']:
                task_date = datetime.strptime(row['properties']['Date']['date']['start'], '%Y-%m-%d').date()
                if task_date == today:
                    task = {
                        'Name': row['properties']['Name']['title'][0]['text']['content'] if row['properties']['Name']['title'] else 'No name',
                        'Location': row['properties']['Location']['rich_text'][0]['text']['content'] if 'rich_text' in row['properties']['Location'] and row['properties']['Location']['rich_text'] else 'No Location',
                        'Description': row['properties']['Description']['rich_text'][0]['text']['content'] if 'rich_text' in row['properties']['Description'] and row['properties']['Description']['rich_text'] else 'No description',
                    }
                    tasks.append(task)
        print(tasks)
        print("fetching success.")
        return tasks
    except Exception as e:
        print(f"Error fetching data from Notion: {e}")
        return []
