import openai  # Used for GPT models
from zhipuai import ZhipuAI  # Import ZhipuAI for GLM models
from config import AI_API_KEY
import re

def email_advice_with_ai(data, ai_version, present_location, user_career, local_time, schedule_prompt=""):
    print("\nGenerating advice with gpt...")
    try:
        # Construct the prompt
        prompt = f"""
        请你作为私人秘书，根据以下信息生成一封当天的汇报邮件。邮件应包括以下五个部分，每个部分都用<h2>标签作为标题，内容用段落标签<p>包裹。邮件内容应使用中文，并且只要HTML格式的body部分，不要CSS，不要任何寒暄，不要任何称呼，不要任何问候语或开场白：

        1. 天气情况和建议：一句话简述今天天气情况，然后给出当天的穿搭建议、出行建议及注意事项（可能包括穿搭、防晒、雨具、防风等等）。
        2. 今日任务概述：一句话总结今日任务，不用出现任务细节。
        3. 时间安排建议：根据现实作息和工作时间，提出任务时间安排建议。现在时间是{local_time}，提供具体、美观且详细的时间轴，同时把任务详情和注意事项用小字写在时间轴里面，并详细告诉我具体怎么做。
        4. 未来任务提醒：如果未来有需要提前花时间准备的任务，而且预计今天已经在准备周期中，请提醒我。反之，如果今天不在准备周期，就不用说。
        5. 注意事项：为了完成这些任务，需要注意什么？只用一句话告诉我具体的注意事项，不要宽泛，不要出现已有内容。

        你的任务是生成一封包含以上五个部分的邮件。以下是相关信息：

        - 天气信息：{data['weather']}
        - 今日任务：{data['today_tasks']}
        - 未来任务和事件：{data['future_tasks']} {data['future_events']}
        - 其他信息：{data['other_advice']}
        - 用户职业：{user_career}
        - 用户所在地：{present_location}
        - 现在时间：{local_time}
        - 其他安排提示：{schedule_prompt}
        """

        system_content = f"GPT应当表现出作为私人秘书的能力，向雇主做当天内接下来时间的汇报，提醒他根据天气情况做相应的准备。雇主是{user_career}，住在{present_location}，现在时间是{local_time}。请在汇报时体现出秘书的专业性和对他的家人般的关心，并使用中文。请用HTML格式（不要CSS），只要body部分，包括一个h2主标题和其余内容。不要任何寒暄，不要任何称呼，不要任何问候语或开场白。"

        if "gpt" in ai_version.lower():
            openai.api_key = AI_API_KEY
            response = openai.ChatCompletion.create(
                model=ai_version,
                messages=[
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=4096,
                temperature=0.3
            )
        elif "glm" in ai_version.lower():
            client = ZhipuAI(AI_API_KEY)
            response = client.chat.completions.create(
                model=ai_version,
                messages=[
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=4096,
                temperature=0.3
            )
        print("Generated.\n")
        return re.sub(r'<body>|</body>|```html?|```', '', response['choices'][0]['message']['content'].strip() if response['choices'] else "No guidance provided.")
    except Exception as e:
        print(f"Error interacting with model: {e}")
        return "There was an error generating advice."
