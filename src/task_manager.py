from notion_client import Client
from datetime import datetime
from config import NOTION_TOKEN, DATABASE_ID, DEFINE_DATE

notion = Client(auth=NOTION_TOKEN)

def fetch_tasks_from_notion():
    print("fetching from notion...\n")
    try:
        results = notion.databases.query(database_id=DATABASE_ID)
        tasks = []
        
        # 判断 DEFINE_DATE 是否为空，如果为空则默认为今天的日期，否则使用自定义日期
        if DEFINE_DATE:
            try:
                custom_date = datetime.strptime(DEFINE_DATE, '%Y-%m-%d').date()
            except ValueError:
                print("Invalid date format in DEFINE_DATE. It should be 'YYYY-MM-DD'. Using today's date instead.")
                custom_date = datetime.now().date()
        else:
            custom_date = datetime.now().date()

        for row in results["results"]:
            if 'date' in row['properties']['Date'] and row['properties']['Date']['date']:
                task_date = datetime.strptime(row['properties']['Date']['date']['start'], '%Y-%m-%d').date()
                if task_date == custom_date:
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

