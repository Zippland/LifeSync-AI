import openai
from config import OPENAI_API_KEY, GPT_VERSION, USERNAME, SCHEDUAL_PROMPT

def generate_advice_with_gpt(tasks):
    print("Generating advice with gpt...")
    try:
        openai.api_key = OPENAI_API_KEY
        task_descriptions = "\n".join([f"- {task['Name']}: {task['Location'] }，{task['Description'] }" for task in tasks])
        # 提示词前缀
        prompt = f"我是{USERNAME}，你是我的时间管理助手，接下来我会发给你今天的任务安排，请遵循3个要求：\n"
        prompt += f"1.先用完美的文字格式复述一遍我今天的任务及详情（未提供部分请省略不描述）；\n"
        prompt += f"2.再请结合现实作息和工作时间，确定这些任务的优先次序并提出任务时间安排建议（请提供具体且详细的时间轴）。\n"
        prompt += f"3.禁止使用包括markdown在内的任何编码的富文本格式，只回答精心组织好的邮件格式plain文本（只要邮件正文）。\n"
        prompt += f"具体内容应当为：\n先给我简略任务描述，然后给我精确到时段的详细时间轴安排。\n"
        # 任务安排
        prompt += f"以下是任务安排：\n{task_descriptions}。\n"
        prompt += f"此外，如果没有被上述安排打断的话，{SCHEDUAL_PROMPT}，如果和上述时间冲突就作废。"
        print(prompt)
        # 系统提示词
        response = openai.ChatCompletion.create(
            model=GPT_VERSION, 
            messages=[
                {"role": "system", "content": "你是{USERNAME}的专业时间管理助手"},
                {"role": "user", "content": prompt}
            ]
        )
        print(response['choices'][0]['message']['content'].strip() if response['choices'] else "No guidance provided.")
        return response['choices'][0]['message']['content'].strip() if response['choices'] else "No guidance provided."
    except Exception as e:
        print(f"Error interacting with OpenAI GPT: {e}")
        return "There was an error generating advice."