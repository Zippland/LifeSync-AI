import openai
from config import OPENAI_API_KEY, GPT_VERSION, USERNAME, SCHEDUAL_PROMPT, PRESENT_LOCATION

def generate_advice_with_gpt(wheather, tasks):
    print("\nGenerating advice with gpt...\n")
    try:
        openai.api_key = OPENAI_API_KEY
        task_descriptions = "\n".join([f"- {task['Name']}: {task['Location'] }，{task['Description'] }" for task in tasks])
        # 提示词前缀
        prompt = f"我是{USERNAME}，住在{PRESENT_LOCATION}，你是我的时间管理助手，接下来我会发给你今天的天气和任务安排，请严格遵循4个要求：\n"
        prompt += f"1.先用一段话复述当日天气情况，并据此给我当天的穿搭建议、出行建议及注意事项（可能包括穿搭、防晒、雨具、防风等等）。"
        prompt += f"2.再简单描述我的任务（仅包含必须参加的外部事件的名字，不用描述详情）\n"
        prompt += f"3.最后请结合现实作息和工作时间，确定这些任务的优先次序并提出任务时间安排建议及任务详情（请提供具体且详细的时间轴，并标明任务详情）。\n"
        # 当日天气
        prompt += f"以下是当日天气：\n{wheather}。\n"
        prompt += f"请在同一段内，先简单描述当日天气情况，然后据此给我当天的出行建议及注意事项。\n"
        # 任务安排
        prompt += f"以下是任务安排：\n{task_descriptions}。\n"
        prompt += f"此外，如果没有被上述安排打断的话，{SCHEDUAL_PROMPT}，如果和上述时间冲突就作废。"
        prompt += f"请分两段，先简单描述我的任务，然后给我一整天的从起床到睡觉的详细时间轴安排并包含详情。\n\n"
        print(prompt)
        print("Waiting for response...\n")
        # 系统提示词
        response = openai.ChatCompletion.create(
            model=GPT_VERSION, 
            messages=[
                {"role": "system", "content": "你是{USERNAME}的专业时间管理助手，请在回复时保持专业。并且禁止使用包括markdown在内的任何编码的富文本格式，只回答精心组织好的邮件格式plain文本（只要邮件正文,包含打招呼和结束语）。"},
                {"role": "user", "content": prompt}
            ]
        )
        print("Generated.\n")
        print(response['choices'][0]['message']['content'].strip() if response['choices'] else "No guidance provided.")
        return response['choices'][0]['message']['content'].strip() if response['choices'] else "No guidance provided."
    except Exception as e:
        print(f"Error interacting with OpenAI GPT: {e}")
        return "There was an error generating advice."