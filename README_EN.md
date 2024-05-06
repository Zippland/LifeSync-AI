# LifeSync-AI

- [English README](README_EN.md)
- [中文 README](README.md)

## Overview
**LifeSync-AI** goes beyond traditional task management features, offering a dynamic, AI-driven personal assistant designed to enhance life management and decision-making capabilities. By integrating a range of tools including cross-platform task collaboration, AI-generated intelligent suggestions, bill tracking, and real-time environmental data feedback, LifeSync-AI helps users tackle daily tasks with unprecedented efficiency and insight.

## Main Features
- [X] **GHA Automation Support**: Deployed in GitHub Actions for fully automated operation.
- [X] **Task Integration**: Automatically fetches and manages tasks from the Notion database.
- [X] **Intelligent Suggestion Generation**: Uses OpenAI GPT to generate priority task lists and strategic recommendations.
- [X] **Weather Information**: Provides real-time weather updates and tailored suggestions based on your schedule.
- [X] **Daily Email Notifications**: Sends daily summaries and task reminders to your email every morning to ensure you are always prepared.
- [X] **Flexible Task Scheduling**: Adjusts your task management intelligently based on real-time data and personalized suggestions.
- [X] **Environmental Variable Management**: Automatically fetches and manages multiuser's environmental variables from the Notion database.
- [ ] **Route Suggestions**: Provides daily commuting route suggestions based on user's travel destinations and environmental factors.
- [ ] **Bill Monitoring and Summary**: Monitors user's bill transactions and dynamically summarizes and charts them.
- [ ] **Calendar and Task Automation Management**: Automatically adds, deletes, and modifies calendar events and daily tasks through mainstream calendar and task management tools.

## Getting Started

### Prerequisites
- Python 3.8+ (not required for cloud deployment)
- Notion account with API access (integration configuration required)
- Mailgun API key
- OpenAI API key
- OpenWeather API key

### Configuration
First, open the following two pages and copy them to Notion:
1. [Notion Second Brain Template](https://ubiquitous-myth-d1f.notion.site/Second-Brain-dd7f04a080794073aad7834adb2e7e57?pvs=4)
2. [User Information Configuration Interface](https://ubiquitous-myth-d1f.notion.site/1604cf736e5248cab549aefc2d7239b9?v=29ad555af9f3424da9a78fd46ce6dc96&pvs=4)

### Installation and Running 
#### 1. Local Running (Not Recommended)
Fork the repository and install the required dependencies:
```bash
git clone https://github.com/Zippland/LifeSync-AI.git
cd LifeSync-AI
pip install -r requirements.txt
```
Configure the `config.py` file to set your user information configuration interface token, OpenAI key, and OpenWeather API.

Then run the following command to activate your personal assistant:
```bash
python main.py
```
Before starting the application, make sure all configurations in `config.py` are correct.

#### 2. Cloud Running (Recommended)
Fork the repository from the top right corner of the interface.

Modify the `.github/workflows/deploy.yml` file:
```yaml
on:
  schedule:
    - cron: '0 22 * * *'  # Every day at 22:00 UTC
  workflow_dispatch:
```
Then go to `Setting -> Security -> Secrets and Variables -> Repository secrets`

Configure the following variables:
- `ENV_DATABASE_ID`
- `ENV_NOTION_TOKEN`
- `MAILGUN_API_KEY`
- `MAILGUN_DOMAIN`
- `OPENAI_API_KEY`
- `OPENWEATHER_API_KEY`

This program will run automatically at a fixed time, or you can manually go to `Action -> Daily Report -> run workflow` and click to run.

## Contribution
We welcome contributions in various forms. To contribute, please:
1. Fork the repository.
2. Create your feature branch.
3. If you add a feature, please add tests.
4. Ensure your changes adhere to the project's coding style.
5. Submit a pull request.

## License
Licensed under the [Apache License](LICENSE).

## Contact
For support or inquiries, please contact [zihan.jian@outlook.com](mailto:zihan.jian@outlook.com).
