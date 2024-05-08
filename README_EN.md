# LifeSync-AI

- [English README](README_EN.md)
- [Chinese README](README.md)

## Overview
**LifeSync-AI** goes beyond traditional task management features, offering a dynamic, AI-driven personal assistant aimed at enhancing life management and decision-making skills. By integrating cross-platform task collaboration, AI-powered suggestions, bill tracking, and real-time environmental feedback, it helps users generate detailed hourly task plans with a single click.

## Key Features
- [X] **GHA Automation Support**: Deployed in GitHub Actions for fully automated program execution.
- [X] **Task Retrieval**: Automatically retrieves and categorizes tasks from the Notion database.
- [X] **Suggestions/Timeline Generation**: Uses AI to generate a list of plans and daily suggestions (supports ChatGPT and ZhiPu QingYan).
- [X] **Weather Information**: Provides real-time weather updates and customized suggestions based on your schedule.
- [X] **Scheduled Email Notifications**: Sends a daily summary and task reminders to your inbox every morning, ensuring you're always prepared.
- [X] **User Information Customization**: Automatically retrieves and manages environmental variables for multiple users.
- [ ] **Route Suggestions**: Offers daily route suggestions based on the user's travel destinations and environmental factors.
- [ ] **Bill Monitoring and Summarization**: Monitors user's bill transactions and dynamically summarizes and charts them.
- [ ] **Calendar and Task Automation Management**: Automatically adds, deletes, modifies, and queries calendar events and daily tasks through mainstream calendar and task management tools.

## Getting Started

### Prerequisites
- Python 3.8+ (not needed for cloud deployment)
- Notion API key (see **User Information Configuration Interface** below for how to apply)
- Mailgun API key (apply on the Mailgun official website)
- OpenAI API key (apply on the OpenAI official website, **this is the only step that will incur a cost**)
- OpenWeather API key (apply on the OpenWeather official website)

### Configuration
First, open the following two pages and copy them to Notion:
1. [**Notion Template**](https://ubiquitous-myth-d1f.notion.site/Second-Brain-dd7f04a080794073aad7834adb2e7e57?pvs=4) (not mandatory, you can use your own Notion task database (table))
2. [**User Information Configuration Interface**](https://ubiquitous-myth-d1f.notion.site/1604cf736e5248cab549aefc2d7239b9?v=29ad555af9f3424da9a78fd46ce6dc96&pvs=4) (mandatory)

### Installation and Running
#### 1. Local Execution (Not Recommended)
Fork the repository and install the required dependencies:
```bash
git clone https://github.com/Zippland/LifeSync-AI.git
cd LifeSync-AI
pip install -r requirements.txt
```
Configure the `.env` file to set your user information configuration interface token, OpenAI key, and OpenWeather API.

Then run the following command to activate your personal assistant:
```bash
python main.py
```
Before starting the application, make sure all configurations in `.env` are correct.

#### 2. Cloud Execution (Recommended)
Fork the repository in the upper right corner of the interface.

Modify the startup time in the `.github/workflows/deploy.yml` file:
```yaml
on:
  schedule:
    - cron: '0 22 * * *'
  workflow_dispatch:
```
Here `cron` represents the daily scheduled start time in UTC. For example, `cron: '0 22 * * *'` corresponds to `6 AM Beijing time`.

Then go to `Setting -> Security -> Secrets and Variables -> Repository secrets`

Configure the following variables:
- `ENV_DATABASE_ID`
- `ENV_NOTION_TOKEN`
- `MAILGUN_API_KEY`
- `MAILGUN_DOMAIN`
- `AI_API_KEY` (changed after supporting ZhiPu QingYan)
- `OPENWEATHER_API_KEY`

This program will run automatically at the time you set, or you can manually go to `Action -> Daily Report-> run workflow` and click to run.

## Contributions
We welcome contributions of all kinds. To contribute, please:
1. Fork the repository.
2. Create your feature branch.
3. If you've added a feature, please add tests.
4. Ensure your changes adhere to the project's coding style.
5. Submit a pull request.

## License
Licensed under the [Apache License](LICENSE).

## Contact
For support or inquiries, please contact me at [zihan.jian@outlook.com](mailto:zihan.jian@outlook.com).
