import openai  # Used for GPT models
from zhipuai import ZhipuAI  # Import ZhipuAI for GLM models
from config import AI_API_KEY
import re

def email_advice_with_ai(advice_part, data, ai_version, present_location, user_career, schedule_prompt=""):
    print("\nGenerating advice with gpt...")
    try:
        # Determine the part of the advice to generate
        parts = {
            "1": "请在一个h2段落内总结：一句话简述今天天气情况，然后给我当天的穿搭建议、出行建议及注意事项（可能包括穿搭、防晒、雨具、防风等等）。",
            "2": "请在一句话内总结我的今日任务，不用出现任务细节",
            "3": "请结合现实作息和工作时间，提出任务时间安排建议。我只需要你提供具体、美观且详细的时间轴。同时，请把任务详情和注意事项用小字写在时间轴里面，并详细告诉我具体怎么做。",
            "4": "请在一个h2段落内总结：如果未来有需要提前花时间准备的任务，而且预计今天已经在准备周期中，请提醒我并告诉我怎么做。反之，如果今天不在准备周期，就不用说。",
            "5": "请在一个h2段落内总结：你觉得为了完成这些任务，我需要注意什么？只用一句话告诉我具体的注意事项，不要宽泛，不要出现已有内容。"
        }
        prompt = parts[advice_part] + "\n\n"
        # Add related data
        if advice_part == "1":
            prompt += f"以下是当日天气：\n{data}。\n\n"
        elif advice_part in ["2", "3"]:
            prompt += f"以下是今天的任务安排（可能包含以前没完成的任务）：\n{data}。\n"
            if advice_part == "3":
                prompt += f"此外，如果没有被上述安排打断的话，{schedule_prompt}，如果和上述时间冲突就作废。\n\n"
        elif advice_part == "4":
            prompt += f"以下是未来任务安排：\n{data}。\n\n"
        elif advice_part == "5":
            prompt += f"\n{data}。\n\n"
        system_content = f"你是秘书，你正在向雇主做早晨的汇报，协助他规划一整天的时间安排。雇主是的职业是{user_career}，住在{present_location}。请据此在汇报时体现出秘书的专业性和对他的关心，并使用中文。请用HTML格式（不要CSS），只要body部分，包括一个h2主标题和其余内容。不要任何寒暄，不要任何称呼，不要任何问候语或开场白。"
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
