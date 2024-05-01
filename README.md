# TaskCopilot

- [English README](README.md)
- [中文 README](README_ZH.md)

## Introduction
TaskCopilot is an efficient personal task management tool designed to help users prioritize and effectively manage daily tasks. It integrates weather lookup functionality, Notion database management, OpenAI GPT-supported suggestions, automated email notifications, and automatic timetable generation to improve personal productivity.

## Roadmap
- [ ] Monitor Wechat's bill flow and chart income and expenses.
- [ ] Automatically add and remove calendar items and daily tasks through the Outlook REST API
- [ ] Provide travel advice using accurate daily weather data from Openweather.
- [X] Dynamically fetches task information from the Notion database.
- [X] Generates priorities and advice for task execution using OpenAI GPT.
- [X] Automatically sends daily tasks and advice through email.

## Installation Guide

### Prerequisites
- Python 3.8 or higher
- Notion account and API access
- OpenAI API key

### Steps
1. Clone the repository:
   ```
   git clone https://github.com/Zippland/TaskPilot.git
   ```
2. Navigate to the project directory:
   ```
   cd TaskPilot
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage Instructions
To start the project, run the following command:
```
python main.py
```
Ensure all necessary configuration information, including the Notion token, database ID, SMTP server details, and OpenAI API key, is correctly set in `config.py`.

## Contribution Guidelines
We welcome all types of contributions, including bug reports, feature requests, and code contributions. Please follow these steps to contribute:
1. Fork the repository and create your branch.
2. If you add functionality, add tests.
3. Ensure your code adheres to the existing style.
4. Submit a pull request.

## License
This project is licensed under the [Apache License](LICENSE).

## Contact Information
If you have any questions, please contact us via [email](mailto:zihan.jian@example.com).
