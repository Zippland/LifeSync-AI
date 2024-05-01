# SecondBrain / 第二大脑

## Introduction / 简介
SecondBrain is an efficient life management tool designed to help users prioritize and effectively manage their daily tasks. It integrates weather query function, Notion database management, OpenAI GPT supported suggestions, automatic email notifications, personal cash flow, and other ALL-IN-ONE features to improve personal productivity. / SecondBrain 是一款高效的人生管理工具，旨在帮助用户对日常任务进行优先排序和有效管理。它集成了天气查询功能、Notion 数据库管理、OpenAI GPT 支持的建议、自动电子邮件通知、个人现金流水等 ALL-IN-ONE 功能，以提高个人工作效率。

## Roadmap / 
- [ ] Monitor Wechat's bill flow and chart income and expenses / 监控 Wechat 的账单流水并绘制收支表单。
- [ ] Automatically add and remove calendar items and daily tasks through the Outlook REST API / 通过 Outlook REST API 自动添加和删除日历和日常任务。
- [X] Provide travel advice using accurate daily weather data from Openweather / 使用 Openweather 提供的准确的每日天气数据提供出行建议。
- [X] Dynamically fetches task information from the Notion database / 从 Notion 数据库动态获取任务信息。
- [X] Generates priorities and advice for task execution using OpenAI GPT / 使用 OpenAI GPT 生成任务执行的优先级和建议。
- [X] Automatically sends daily tasks and advice through email / 通过电子邮件自动发送每日任务和建议。

## Installation Guide / 安装指南

### Prerequisites / 环境要求
- Python 3.8 or higher / Python 3.8 或更高版本。
- Notion account and API access / Notion 账号和相关 API 访问权限
- OpenAI API key / OpenAI API 密钥
- OpenWeatherMap API key / OpenWeatherMap API 密钥.
- mailbox account / 邮箱账号。

### Steps / 步骤
1. Clone the repository/克隆仓库:
   ```
   git clone https://github.com/Zippland/SecondBrain.git
   ```
2. Navigate to the project directory / 进入项目目录:
   ```
   cd TaskPilot
   ```
3. Install dependencies / 安装依赖:
   ```
   pip install -r requirements.txt
   ```

## Usage Instructions / 使用说明
To start the project, run the following command / 要启动项目，请运行以下命令:
```
python main.py
```
Ensure all necessary configuration information, including the Notion token, database ID, SMTP server details, and OpenAI API key, is correctly set in `config.py` / 确保在 `config.py` 文件中正确设置了所有必要的配置信息，包括 Notion 的 token、数据库 ID、SMTP 服务器信息和 OpenAI 的 API 密钥。

## Contribution Guidelines / 贡献指南
We welcome all types of contributions, including bug reports, feature requests, and code contributions. Please follow these steps to contribute / 我们欢迎所有形式的贡献，包括错误报告、功能请求和代码提交。请遵循以下步骤贡献你的力量：:
1. Fork the repository and create your branch / Fork 仓库并创建你的分支。
2. If you add functionality, add tests / 如果你添加了功能，请添加测试。
3. Ensure your code adheres to the existing style / 确保你的代码符合现有代码风格。
4. Submit a pull request / 提交合并请求。

## License / 许可证
This project is licensed under the [Apache License](LICENSE) / 该项目采用 [Apache 许可证](LICENSE)。

## Contact Information / 联系方式
If you have any questions, please contact me via [email](mailto:zihan.jian@outlook.com) / 如果你有任何问题，请通过 [email](mailto:zihan.jian@outlook.com) 联系我。
