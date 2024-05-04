from notion_client import Client
from config import ENV_NOTION_TOKEN, ENV_DATABASE_ID

def get_user_env_vars():
    print("get users' enviroments' variables")
    # 查询数据库
    notion = Client(auth=ENV_NOTION_TOKEN)
    response = notion.databases.query(ENV_DATABASE_ID)

    # 存储用户环境变量的字典
    user_env_vars = {}

    # 遍历每个页面（数据库中的行）
    for page in response.get("results", []):
        user_id = page['properties']['USER_ID']['title'][0]['text']['content']
        # 假设数据库中有如下属性
        user_env_vars[user_id] = {
            # Aunthentication
            "USER_PASSWORD": page['properties']['USER_PASSWORD']['rich_text'][0]['text']['content'],
            # personal info
            "USER_NAME": page['properties']['USER_NAME']['rich_text'][0]['text']['content'],
            "USER_CAREER": page['properties']['USER_CAREER']['rich_text'][0]['text']['content'],
            "PRESENT_LOCATION": page['properties']['PRESENT_LOCATION']['rich_text'][0]['text']['content'],
            "SCHEDULE_PROMPT": page['properties']['SCHEDULE_PROMPT']['rich_text'][0]['text']['content'],
            # hyper parameter
            "GPT_VERSION": page['properties']['GPT_VERSION']['rich_text'][0]['text']['content'],
            "USER_NOTION_TOKEN": page['properties']['USER_NOTION_TOKEN']['rich_text'][0]['text']['content'],
            "USER_DATABASE_ID": page['properties']['USER_DATABASE_ID']['rich_text'][0]['text']['content'],
            "EMAIL_RECEIVER": page['properties']['EMAIL_RECEIVER']['rich_text'][0]['text']['content'],
            "TIME_ZONE": page['properties']['TIME_ZONE']['rich_text'][0]['text']['content'],
            "EMAIL_TITLE": page['properties']['EMAIL_TITLE']['rich_text'][0]['text']['content']
        }
    print("Enviroments' variables fetched.")
    print(user_env_vars)
    return user_env_vars

# # 假设已经运行了 get_user_env_vars 函数并保存了返回值
# user_data = get_user_env_vars()

# # 指定用户ID
# user_id = "user123"

# # 检查是否有这个用户的数据
# if user_id in user_data:
#     # 获取特定用户的用户名
#     username = user_data[user_id]["USERNAME"]
#     # 获取特定用户的时区
#     time_zone = user_data[user_id]["TIME_ZONE"]
    
#     print(f"Username for {user_id}: {username}")
#     print(f"Time Zone for {user_id}: {time_zone}")
# else:
#     print(f"No data available for user ID: {user_id}")
