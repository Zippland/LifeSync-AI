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
        - 今日完成的日程（如果没有就忽略）：{data['completed_events']}
        - 今日完成的任务（如果没有就忽略）：{data['completed_tasks']}

        4. 今天还没做完的任务：
        - 任务：今日到期的紧急任务，必须今日内安排，但是还没做完的任务：{data['today_tasks']}

        5. 其他任务：
        - 任务：已经开始的任务，可以提醒要做：{data['in_progress_tasks']}
        - 任务：即将开始的任务，可以提醒要做：{data['future_tasks']}
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
        请你作为私人秘书，生成一封结构清晰的晚报邮件。请严格按照以下HTML结构输出：

        1. 今日总结：
        <div class="section">
            <div class="section-header">
                <h2><strong>📋 今日总结</strong></h2>
            </div>
            <div class="section-content">
                <div class="overview-card">
                    <h3>完成概述</h3>
                    <p>[简要总结今天的完成情况]</p>
                </div>
                
                <ul class="timeline">
                    <li class="timeline-item">
                        <div class="timeline-time">[完成时间(不写日期，只写时间)]</div>
                        <div class="timeline-content">
                            <h3 class="timeline-title">
                                [完成的事项]
                                <span class="task-label task-priority-low">已完成</span>
                            </h3>
                            <p class="timeline-desc">[完成情况评价和建议]</p>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
        注意：如果没有已完成事项，就不写后面的完成事项timeline的block。

        2. 待处理事项：
        <div class="section">
            <div class="section-header">
                <h2><strong>📝 待处理事项</strong></h2>
            </div>
            <div class="section-content">
                <div class="overview-card">
                    <h3>未完成事项说明</h3>
                    <p>[简要说明未完成原因和处理建议]</p>
                </div>
                
                <ul class="timeline">
                    <li class="timeline-item">
                        <div class="timeline-time">[预计时间]</div>
                        <div class="timeline-content">
                            <h3 class="timeline-title">
                                [未完成的事项]
                                <span class="task-label task-priority-high">待处理</span>
                            </h3>
                            <p class="timeline-desc">[具体的后续处理建议]</p>
                        </div>
                    </li>
                </ul>
            </div>
        </div>

        3. 明日预览：
        <div class="section">
            <div class="section-header">
                <h2><strong>🌅 明日预览</strong></h2>
            </div>
            <div class="section-content">
                <div class="weather-info">
                    <h3>天气提醒</h3>
                    <p class="weather-summary">[明天的天气概况]</p>
                    <p class="weather-advice">[基于天气的建议]</p>
                </div>

                <ul class="timeline">
                    <li class="timeline-item">
                        <div class="timeline-time">[具体时间(没有规定时间可写待定)]</div>
                        <div class="timeline-content">
                            <h3 class="timeline-title">
                                [安排内容]
                                <span class="task-label task-priority-medium">待办</span>
                            </h3>
                            <p class="timeline-desc">[需要提前准备的事项]</p>
                        </div>
                    </li>
                </ul>
            </div>
        </div>

        4. 建议事项：
        <div class="section">
            <div class="section-header">
                <h2><strong>💡 建议事项</strong></h2>
            </div>
            <div class="section-content">
                <ul class="important-notes">
                    <li>[基于今日完成情况的改进建议]</li>
                    <li>[明天需要特别注意的事项]</li>
                </ul>
            </div>
        </div>

        注意要点：
        1. 今日总结要客观公正，既肯定成绩也指出不足
        2. 待处理事项要给出具体可行的建议
        3. 明日预览要突出重点，并给出准备建议
        4. 根据事项状态使用不同的标签：
           - task-priority-low：已完成的事项
           - task-priority-high：待处理的紧急事项
           - task-priority-medium：明日待办事项
        5. 所有建议要具体且可执行
        6. 语气要专业、积极、鼓励

        相关信息：
        {prompt_info}

        之前的分析建议：
        {ai_schedule}
        """

        system_content = """作为私人秘书，你需要生成一份全面的晚间总结报告。要求：
        1. 严格遵循提供的HTML结构
        2. 客观评价今日完成情况
        3. 对未完成事项提供建设性建议
        4. 做好明日工作的预判和建议
        5. 保持专业、积极、鼓励的语气
        6. 所有建议要具体且可执行
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