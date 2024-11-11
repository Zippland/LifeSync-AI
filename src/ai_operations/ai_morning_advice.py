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

        2. 已有时间安排的日程：
        - 日程：已规定时间并已经开始了的既定日程，只用放在既定时间段即可：{data['in_progress_events']}

        3. 必须安排在今天的任务
        - 任务：今日到期的紧急任务，必须今日内安排：{data['today_tasks']}

        4. 可选安排的任务
        - 任务：已经开始的任务，如果有空闲可安排（没空就算了）：{data['in_progress_tasks']}
        """

        prompt_for_iter = f"""
        私人秘书即将向用户汇报今天一整天的行程安排。请分析：

        1. 固定日程：已确定时间的事项
        2. 必要任务：必须今天完成的任务，按重要性排序
        3. 可选任务：如果有时间可以处理的事项
        4. 预留时间：用餐、休息、通勤等必要时间
        5. 紧急程度：紧急且重要、重要但不紧急、其他普通任务

        所有分析都只针对今天，不要考虑明天的安排。

        以下是相关信息：
        {prompt_info}
        """
        
        ai_schedule = iterator(prompt_for_iter, ai_version)

        prompt = f"""
        请你作为私人秘书，生成一封结构清晰的晨报邮件。请严格按照以下HTML结构输出：

        1. 今日概览：
        <div class="section">
            <div class="section-header">
                <h2>📅 今日概览</h2>
            </div>
            <div class="section-content">
                <div class="overview-card">
                    <h3>今日重点关注</h3>
                    <p>[一句话概述今天最重要的1-2件事，务必简洁有力]</p>
                </div>
                
                <div class="weather-info">
                    <h3>天气提醒</h3>
                    <p class="weather-summary">[简要天气描述，包括天气现象、温度、风速及其他重要内容等，最前面用天气emoji标识]</p>
                    <p class="weather-advice">[根据天气给出的具体建议，如需要带伞或需要穿什么衣物等]</p>
                </div>
            </div>
        </div>

        2. 时间安排：
        <div class="section">
            <div class="section-header">
                <h2>⏰ 时间安排</h2>
            </div>
            <div class="section-content">
                <ul class="timeline">
                    <li class="timeline-item">
                        <div class="timeline-time">[具体时间（HH:MM）]</div>
                        <div class="timeline-content">
                            <h3 class="timeline-title">
                                <strong>[事项名称]</strong>
                                <span class="task-label task-priority-high">紧急</span>
                            </h3>
                            <p class="timeline-desc">
                                [具体执行建议和注意事项（如有）]
                            </p>
                        </div>
                    </li>
                </ul>
            </div>
        </div>

        3. 注意事项：
        <div class="section">
            <div class="section-header">
                <h2>⚠️ 注意事项</h2>
            </div>
            <div class="section-content">
                <ul class="important-notes">
                    <li>[重要提醒1：具体且可执行的建议]</li>
                    <li>[重要提醒2（如有）：具体且可执行的建议]</li>
                    <!-- 最多不超过3条重要提醒 -->
                </ul>
            </div>
        </div>

        注意要点：
        1. 时间安排要按时间顺序排列，并注意合理安排间隔
        2. 每个时间段的描述要包含具体的行动建议
        3. 根据任务紧急程度，准确使用不同的task-label样式（按照上文给你的紧急程度来，没有给你标识的不能标识为紧急）：
           - task-priority-high：紧急且重要的任务
           - task-priority-medium：重要但不紧急的任务
           - task-priority-low：普通任务
        4. 重要提醒最多3条，每条都要具体且可执行
        5. 天气建议要与具体活动相关联

        相关信息：
        {prompt_info}

        之前的分析建议：
        {ai_schedule}
        """

        system_content = """作为私人秘书，你需要生成一份结构清晰、重点突出的晨报。要求：
        1. 严格遵循提供的HTML结构
        2. 确保时间安排的逻辑性和可执行性
        3. 准确使用优先级标签
        4. 所有建议要具体且实用
        5. 通过视觉层级突出重要信息
        直接输出HTML内容，不要添加任何额外的开场白或结束语。"""

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