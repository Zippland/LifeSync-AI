import openai  # 用于GPT模型
from zhipuai import ZhipuAI  # 导入ZhipuAI以使用GLM模型
from config import AI_API_KEY  # 导入API密钥

def iterator(prompt, ai_version):
    print("\nGenerating Iterative Information...")
    try:
        # 构建提示
        system_content = f"你应当尽可能完成用户的指令。你的回答应该越多越好，越详细越好。针对每一个事件给出尽可能多的信息和理由。"
        
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
            # 直接返回生成的内容部分
            return response['choices'][0]['message']['content'].strip()
        
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
            # 直接返回生成的内容部分
            return response['choices'][0]['message']['content'].strip()
        
    except Exception as e:
        print(f"Error interacting with model: {e}")
        return "There was an error generating advice."

