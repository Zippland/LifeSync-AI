# SecondBrain: Your Personal Assistant

- [English README](README_EN.md)
- [中文 README](README.md)

## Overview
**SecondBrain** goes beyond traditional task management to provide a dynamic, AI-powered personal assistant designed to enhance life management and decision-making. Integrating tools like Notion for data management, OpenAI GPT for intelligent advice, and real-time environmental data feeds, SecondBrain helps users handle daily tasks with unprecedented efficiency and insight.

## Key Features
- [X] **Notion Integration**: Automatically fetch and manage tasks from Notion databases.
- [X] **Intelligent Advice Generation**: Use OpenAI GPT to generate prioritized task lists and strategic advice.
- [X] **Weather Insights**: Receive real-time weather updates and tailored recommendations according to your schedule.
- [X] **Email Notifications**: Send daily summaries and task alerts directly to your inbox, ensuring you're always prepared.
- [X] **Flexible Task Scheduling**: Adapt your task management intelligently based on real-time data and personalized advice.
- [ ] **Route Recommendations**: Provide daily commuting recommendations based on users' travel purposes and environmental factors.
- [ ] **Bill Monitoring and Summary**: Monitor users' bill transactions and dynamically summarize and chart them.
- [ ] **Automated Calendar and Task Management**: Automatically manage calendar schedules and daily tasks through mainstream calendar and task management tools.

## Getting Started

### Prerequisites
- Python 3.8+
- A Notion account with API access
- OpenAI API key
- OpenWeather API key (free for personal use)

### Installation
Clone the repository and install the required dependencies:
```bash
git clone https://github.com/Zippland/SecondBrain.git
cd SecondBrain
pip install -r requirements.txt
```

### Configuration
Edit `config.py` to set your Notion credentials, OpenAI key, and other preferences such as your preferred SMTP settings for email notifications.

### Usage
Run the following command to activate your personal assistant:
```bash
python main.py
```
Ensure all configurations in `config.py` are correct before launching the application.

## Contribution
We welcome contributions of all forms. To contribute:
1. Fork the repository.
2. Create your feature branch.
3. Add tests if you're adding functionality.
4. Ensure your changes adhere to the project's coding style.
5. Submit a pull request.

## License
Licensed under the [Apache License](LICENSE).

## Contact
For support or inquiries, please email me at [zihan.jian@outlook.com](mailto:zihan.jian@outlook.com).