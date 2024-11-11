import openai
from zhipuai import ZhipuAI
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
        - 雇主的时间安排需求，如有冲突可适当调整：{schedule_prompt}

        2. 时间安排：
        - 今日进行中的日程：{data['in_progress_events']}
        - 明天的日程：{data['tomorrow_events']}
        - 后天及以后的日程：{data['upcoming_events']}

        3. 今天完成的日程和任务：
        - 今日完成的日程：{data['completed_events']}
        - 今日完成的任务：{data['completed_tasks']}

        4. 今天还没做完的任务：
        - 任务：今日到期的紧急任务，必须今日内安排，但是还没做完的任务：{data['today_tasks']}

        5. 其他任务：
        - 任务：已经开始的任务，可以提醒我要做：{data['in_progress_tasks']}
        - 任务：即将开始的任务，可以提醒我要做：{data['future_tasks']}
        """

        prompt_for_iter = f"""
        私人秘书即将向用户总结今天的任务进展，并提前告知明天（或未来）的安排（分析越详细越好，"日程"可以告诉我时间，"任务"和其他的东西不用告诉我具体时间）。请根据以下要求进行分析：
        
        你要做的事情 一：
        1. 总结今天完成了哪些事情（包括日程和任务）
        2. 对每个已完成的事项进行简要点评，表扬完成得好的，对未完全达标的给出改进建议
        3. 如果今天没有完成任何事项，直接说明"今天暂无完成的事项（任务）"

        你要做的事情 二：
        判断还有没有未完成的任务，如果有，就对于每个任务详细分析：
        1. 每个任务是什么，详细解析一下
        2. 怎么看待该任务的紧急程度
        3. 任务的实际执行建议
        如果没有未完成的任务，直接说明"暂无未完成的任务"

        你要做的事情 三：
        如果有明天的日程安排，列出具体安排；如果没有，直接说明"明天暂无已安排的日程"

        你要做的事情 四：
        如果有未来任务，根据紧急程度排序；如果没有，直接说明"暂无未来待办任务"

        以下是相关信息：
        {prompt_info}
        """
        
        ai_schedule = iterator(prompt_for_iter, ai_version)

        prompt = f"""
        请你作为私人秘书，根据以下信息，为我生成一封当天的晚报汇报邮件。邮件应包括4个部分，每个部分都用<h2>标签作为标题，内容用段落标签<p>包裹。如果某个部分没有内容，请直接说明没有。邮件内容应使用中文，并且只要HTML格式的body部分，不要CSS，不要任何寒暄，不要任何称呼，不要任何问候语或开场白。

        1. 天气情况和建议：简要描述明天的天气情况及变化（不要写成流水账），然后生成明天的穿搭建议、出行建议及注意事项（可能包括穿搭、防晒、雨具、防风等等）。
        
        2. 今日完成事项总结：如果今天完成了事项，请列出并用表格形式展示，在每个事项后用一句话点评。如果没有完成的事项，直接说明"今天暂无完成的事项"。
        
        3. 未完成事项和建议：如果有未完成的任务，总结并解释未完成的原因（如果能推测的话），并提供改进建议。如果没有未完成的任务，直接说明"暂无未完成的任务"。

        4. 未来任务和日程提醒：如果有未来任务或日程，按照时间顺序列出。如果都没有，直接说明"暂无未来任务和日程安排"。
        
        请确保每个部分都有明确的内容或明确说明没有内容，避免模糊的表述。
        
        以下是相关信息：
        
        {prompt_info}

        整体事件的时间考虑已经由gpt迭代过一次，以下是gpt的一些建议，请根据这些建议制定一个最终版本的时间安排出来（不要征求意见，只用强制安排时间）：
        
        【{ai_schedule}】
        """

        system_content = "GPT应当表现出作为私人秘书的能力，向我总结当天的完成情况，提醒明天的安排，提醒我根据天气情况和任务日程情况做相应的准备。请在汇报时体现出秘书的专业性和对我的关心，使用中文。请用HTML格式（不要CSS），只要body部分，明确说明有或没有内容，避免模糊的表述。不要任何寒暄，不要任何称呼，不要任何问候语或开场白。"
        
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