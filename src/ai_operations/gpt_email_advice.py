import openai  # Used for GPT models
from zhipuai import ZhipuAI  # Import ZhipuAI for GLM models
from config import AI_API_KEY
import re

def email_advice_with_ai(advice_part, data, ai_version, present_location, user_career, local_time, schedule_prompt=""):
    print("\nGenerating advice with gpt...")
    try:
        # Determine the part of the advice to generate
        parts = {
            "1": f"请在一个h2段落内总结：一句话简述今天天气情况，然后给我当天的穿搭建议、出行建议及注意事项（可能包括穿搭、防晒、雨具、防风等等）。",
            "2": f"请在一句话内总结我的今日任务，不用出现任务细节",
            "3": f"请结合现实作息和工作时间，提出任务时间安排建议。现在时间是{local_time}, 我只需要你接下来提供具体、美观且详细的时间轴。同时，请把任务详情和注意事项用小字写在时间轴里面，并详细告诉我具体怎么做。",
            "4": f"请在一个h2段落内总结：如果未来有需要提前花时间准备的任务，而且预计今天已经在准备周期中，请提醒我并告诉我怎么做。反之，如果今天不在准备周期，就不用说。",
            "5": f"请在一个h2段落内总结：你觉得为了完成这些任务，我需要注意什么？只用一句话告诉我具体的注意事项，不要宽泛，不要出现已有内容。"
        }
        prompt = parts[advice_part] + "\n\n"
        # Add related data
        if advice_part == "1":
            system_content = f"GPT应当表现出作为私人秘书的能力，向雇主做当天内接下来时间的汇报，提醒他根据天气情况做相应的准备。雇主是的职业是{user_career}，住在{present_location}，现在时间是{local_time}。请在汇报时体现出秘书的专业性和对他的家人般的关心，并使用中文。请用HTML格式（不要CSS），只要body部分，包括一个h2主标题和其余内容。不要任何寒暄，不要任何称呼，不要任何问候语或开场白。"
            prompt += f"以下是当日天气：\n{data}。\n\n"
        elif advice_part == "2":
            system_content = f"GPT应当表现出作为私人秘书的能力，根据现在的时间和未完成的工作，向雇主做当天内接下来时间的汇报，提醒他当日需要做的任务。雇主是的职业是{user_career}，住在{present_location}，现在时间是{local_time}。请在汇报时体现出秘书的专业性和概括能力，并使用中文。请用HTML格式（不要CSS），只要body部分，包括一个h2主标题和其余内容。不要任何寒暄，不要任何称呼，不要任何问候语或开场白。"
            prompt += f"以下是今天的任务安排（可能包含以前没完成的任务）：\n{data}。\n"
        elif advice_part == "3":
            system_content = f"GPT应当表现出作为私人秘书的能力，根据现在的时间和未完成的工作，向雇主做当天内接下来时间的汇报，协助他规划一整天的时间安排。雇主是的职业是{user_career}，住在{present_location}，现在时间是{local_time}。请在汇报时体现出秘书的专业性和对任务细节的理解能力，并使用中文。请用HTML格式（不要CSS），只要body部分，包括一个h2主标题和其余内容。不要任何寒暄，不要任何称呼，不要任何问候语或开场白。"
            prompt += f"以下是今天的任务安排（可能包含以前没完成的任务）：\n未来的event如果需要提前准备，也放进来：\n{data}。\n"
            prompt += f"此外，如果没有被上述安排打断的话，{schedule_prompt}，如果和上述时间冲突就作废。\n\n"
        elif advice_part == "4":
            system_content = f"GPT应当表现出作为私人秘书的能力，向雇主做当天内接下来时间的汇报。根据未来任务距离现在的时间，判断是否需要现在提醒雇主某些任务是否需要做准备。雇主是的职业是{user_career}，住在{present_location}，现在时间是{local_time}。请在汇报时体现出秘书的专业性和对任务优先级和时间紧迫性的计算能力，并使用中文。请用HTML格式（不要CSS），只要body部分，包括一个h2主标题和其余内容。不要任何寒暄，不要任何称呼，不要任何问候语或开场白。"
            prompt += f"以下是未来任务安排：\n{data}。\n\n"
        elif advice_part == "5":
            system_content = f"GPT应当表现出作为私人秘书的能力，根据雇主的安排提醒他注意事项。现在时间是{local_time}。请在汇报时把所有内容浓缩为一句话，不要让雇主今天做，只用提醒他注意，并使用中文。请用HTML格式（不要CSS），只要body部分，包括一个h2主标题和其余内容。不要任何寒暄，不要任何称呼，不要任何问候语或开场白。"
            prompt += f"\n{data}。\n\n"
        
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
