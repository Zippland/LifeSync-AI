import openai  # Used for GPT models
from zhipuai import ZhipuAI  # Import ZhipuAI for GLM models
from config import AI_API_KEY
from src.ai_operations.ai_iterator import iterator
import re

def email_advice_with_ai(data, ai_version, present_location, user_career, local_time, schedule_prompt=""):
    print("\nGenerating advice with gpt...")
    try:

        prompt_info = f"""
        1. 基础信息：
        - 天气信息：{data['weather']}
        - 雇主职业：{user_career}
        - 雇主所在地：{present_location}
        - 现在的时间：{local_time}
        - 雇主的时间安排需求，任务安排必须遵守，日程不用遵守：{schedule_prompt}

        2. 已有时间安排的日程：
        - 日程：已规定时间并已经开始了的既定日程，只用放在既定时间段即可：{data['in_progress_events']}

        3. 必须安排在今天的任务
        - 任务：今日到期的紧急任务，必须今日内安排：{data['today_tasks']}

        4. 可选安排的任务
        - 任务：已经开始的任务，如果有空闲可安排（没空就算了）：{data['in_progress_tasks']}
        """

        prompt_for_iter = f"""
        私人秘书即将向用户汇报今天一整天的行程安排，每个事件分为“任务”和“日程”两种，需要你做两件事，来帮助他完成工作。“日程”是已有确定时间的任务，只用放在既定时间段即可。“任务”是你需要为雇主分析时间方案的任务。
        
        你要做的事情 一：
        对于每个“任务”，请详细分析4个部分：
        1. 每个任务是什么，怎么看待他们的紧急程度；
        2. 给出几个可安排的时间段落；
        3. 每个时间建议的理由。
        4. 并考虑事件前后的预留时间；

        你要做的事情 二：
        对每个任务的紧急程度进行排序。

        以下是相关信息：
        {prompt_info}
        """
        ai_schedule = iterator(prompt_for_iter, ai_version)

        # Construct the prompt 
        prompt = f"""
        请你作为私人秘书，根据以下信息生成一封当天的晨报邮件。邮件应包括3个部分，每个部分都用<h2>标签作为标题，内容用段落标签<p>包裹。邮件内容应使用中文，并且只要HTML格式的body部分，不要CSS，不要任何寒暄，不要任何称呼，不要任何问候语或开场白。

        1. 天气情况和建议：一句话简述今天天气情况，以及出当天的穿搭建议、出行建议及注意事项（可能包括穿搭、防晒、雨具、防风等等）。
        2. 时间安排建议：根据现实作息和工作时间，提出任务时间安排建议，记得留时间出来吃饭休息。请提供具体、美观且详细的时间轴，同时把任务详情和注意事项用小字写在时间轴里面，并详细告诉我具体怎么做。
        3. 注意事项：为了完成这些任务，需要注意什么？只用一句话告诉我具体的注意事项，不要宽泛，不要出现已有内容。

        你的任务是生成一封包含以上3个部分的邮件。
        
        以下是相关信息：
        
        {prompt_info}

        整体事件的时间考虑已经由gpt迭代过一次，以下是gpt的想法，请据此安排时间：
        
        【{ai_schedule}】
        """

        system_content = f"GPT应当表现出作为私人秘书的能力，向雇主做当天内接下来时间的汇报，提醒他根据天气情况做相应的准备。对于end date不是今天的任务，如果时间安排不满足雇主作息要求，就不要安排在今天。请在汇报时体现出秘书的专业性和对他的家人般的关心，并使用中文。请用HTML格式（不要CSS），只要body部分，包括一个h2主标题和其余内容。不要任何寒暄，不要任何称呼，不要任何问候语或开场白。"
        print(system_content+"\n"+prompt)
        if "gpt" in ai_version.lower():
            openai.api_key = AI_API_KEY
            response = openai.ChatCompletion.create(
                model=ai_version,
                messages=[
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": prompt}
                ],
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
                temperature=0.3
            )
        print("Generated.\n")
        return re.sub(r'<body>|</body>|```html?|```', '', response['choices'][0]['message']['content'].strip() if response['choices'] else "No guidance provided.")
    except Exception as e:
        print(f"Error interacting with model: {e}")
        return "There was an error generating advice."
