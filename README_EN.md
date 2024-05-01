# SecondBrain

- [English README](README_EM.md)
- [日本語のREADME](README_JP.md)
- [한국어 README](README_KR.md)
- [中文 README](README.md)

## Introduction
SecondBrain is an efficient life planning and management tool designed to help users prioritize and effectively manage personal affairs and resources. It integrates Notion database management, OpenAI GPT support, intelligent scheduling, weather query function, personal cash flow query, email interaction, and more to enhance personal life efficiency.

## Roadmap
- [ ] Monitor WeChat billing statements and draw up income and expenditure forms.
- [ ] Automatically add and remove calendars and daily tasks through MS To-Do and Outlook.
- [X] Provide travel suggestions using accurate daily weather data from Openweather.
- [X] Dynamically fetch task information from the Notion database.
- [X] Use OpenAI GPT to generate task execution priorities and suggestions.
- [X] Automatically send daily tasks and suggestions via email.

## Installation Guide

### Prerequisites
- Python 3.8 or higher
- Notion account and API access permissions
- OpenAI API key

### Steps
1. Clone the repository:
   ```
   git clone https://github.com/Zippland/SecondBrain.git
   ```
2. Enter the project directory:
   ```
   cd TaskPilot
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Instructions for Use
To start the project, run the following command:
```
python main.py
```
Make sure all necessary configuration information is correctly set in the `config.py` file, including Notion's token, database ID, SMTP server information, and OpenAI's API key.

## Contribution Guide
We welcome all forms of contribution, including bug reports, feature requests, and code submissions. Please follow the steps below to contribute your strength:
1. Fork the repository and create your branch.
2. If you've added functionality, please add tests.
3. Ensure your code adheres to the existing code style.
4. Submit a pull request.

## License
This project is under the [Apache License](LICENSE).

## Contact
If you have any questions, please contact us at [email](mailto:zihan.jian@outlook.com).