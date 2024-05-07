from notion_client import Client
from config import ENV_NOTION_TOKEN, ENV_DATABASE_ID

def get_user_env_var(user_id):
    print("Fetching user's environment variables")
    # Initialize Notion client
    notion = Client(auth=ENV_NOTION_TOKEN)
    
    # Query for a specific user's data using their USER_ID
    response = notion.databases.query(
        **{
            "database_id": ENV_DATABASE_ID,
            "filter": {
                "property": "USER_ID",
                "title": {
                    "equals": user_id
                }
            }
        }
    )

    # Check if any pages are found
    pages = response.get("results", [])
    if pages:
        page = pages[0]  # Assume the first result is the desired one
        user_env_vars = {
            "USER_NAME": page['properties']['USER_NAME']['rich_text'][0]['text']['content'],
            "USER_CAREER": page['properties']['USER_CAREER']['rich_text'][0]['text']['content'],
            "PRESENT_LOCATION": page['properties']['PRESENT_LOCATION']['rich_text'][0]['text']['content'],
            "SCHEDULE_PROMPT": page['properties']['SCHEDULE_PROMPT']['rich_text'][0]['text']['content'],
            "GPT_VERSION": page['properties']['GPT_VERSION']['rich_text'][0]['text']['content'],
            "USER_NOTION_TOKEN": page['properties']['USER_NOTION_TOKEN']['rich_text'][0]['text']['content'],
            "USER_DATABASE_ID": page['properties']['USER_DATABASE_ID']['rich_text'][0]['text']['content'],
            "EMAIL_RECEIVER": page['properties']['EMAIL_RECEIVER']['rich_text'][0]['text']['content'],
            "TIME_ZONE": page['properties']['TIME_ZONE']['rich_text'][0]['text']['content'],
            "EMAIL_TITLE": page['properties']['EMAIL_TITLE']['rich_text'][0]['text']['content']
        }
        print("Environment variables fetched.")
        print(user_env_vars)
        return user_env_vars
    else:
        print("No data available for user ID:", user_id)
        return None
