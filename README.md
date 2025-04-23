> 2025年4月23日起，本项目被高阶项目 [Bubbles](https://github.com/Zippland/Bubbles) 取代，不再更新，如有兴趣可以前往[Bubbles](https://github.com/Zippland/Bubbles) 项目。
# LifeSync-AI

- [English README](README_EN.md)
- [中文 README](README.md)

## 概览
**LifeSync-AI** 超越了传统的任务管理功能，提供了一个动态的、由AI驱动的个人助理，旨在提高生活管理和决策能力。通过集成跨平台任务协同、AI智能建议、账单流水跟踪及实时环境数据反馈等一系列工具，帮助用户一键生成精确到小时的详细任务规划。

## 主要功能
- [X] **GHA自动化支持**：部署在github action中以全自动运行程序。
- [X] **任务获取**：自动获取并归类管理Notion数据库中的task。
- [X] **建议/时间轴生成**：利用AI生成计划列表和每日建议（支持ChatGPT和智谱清言）。
- [X] **天气信息**：获取实时天气更新和根据您的日程定制的建议。
- [X] **定时邮件通知**：每天清晨发送日常总结和任务提醒到您的邮箱，确保您始终准备就绪。
- [X] **用户信息自定义**：自动获取并管理多个用户情况下的环境变量。
- [ ] **路线建议**：根据用户的出行目的和环境因素，提供每日出行的路线建议。
- [ ] **账单监控与总结**：监控用户的账单流水，并动态地总结和绘制表单。
- [ ] **日历和任务自动化管理**：通过主流的日历和task管理工具自动增删改查日历日程和日常任务。

## 入门指南

### 先决条件
- Python 3.8+ （云端部署不需要）
- Notion API密钥（申请方式可见下方**用户信息配置界面**中所述）
- Mailgun API密钥（在 Mailgun 官网申请）
- OpenAI API密钥（在 OpenAI 官网申请，**这是唯一会产生费用的步骤**）
- OpenWeather API密钥（在 OpenWeather 官网申请）

### 配置
先打开下列两个页面并复制于notion：
1. [**Notion 模板**](https://ubiquitous-myth-d1f.notion.site/Second-Brain-dd7f04a080794073aad7834adb2e7e57?pvs=4)（非必须，可以用您自己的 notion 任务数据库（表格））
2. [**用户信息配置界面**](https://ubiquitous-myth-d1f.notion.site/74dc39a6d0fc41ae9c353d8f2ae734b9?v=b1487a20df1647f2b1cb33e3b61d80f2&pvs=4)（必须）

### 安装及运行 
#### 1. 本地运行（不推荐）
fork仓库并安装所需的依赖项：
```bash
git clone https://github.com/Zippland/LifeSync-AI.git
cd LifeSync-AI
pip install -r requirements.txt
```
配置 `.env` 文件以设置您用户信息配置界面的token、OpenAI密钥以及openweather API。

然后运行以下命令激活您的个人助理：
```bash
python main.py
```
启动应用程序前，请确保 `.env` 中的所有配置都是正确的。

#### 2. 云端运行（推荐）
在界面右上角fork本仓库。

修改`.github/workflows/deploy.yml`文件中的启动时间：
```yaml
on:
  schedule:
    - cron: '0 22 * * *'
  workflow_dispatch:
```
此处 `cron`代表每日定时启动时间，以UTC 时间算，如`cron: '0 22 * * *'`代表 `北京时间上午6点`。

然后进入 `Setting -> Security -> Secrets and Variables -> Repository secrets`

配置如下变量：
- `ENV_DATABASE_ID`
- `ENV_NOTION_TOKEN`
- `MAILGUN_API_KEY`
- `MAILGUN_DOMAIN`
- `AI_API_KEY` (支持智谱清言后有改动）
- `OPENWEATHER_API_KEY`

此程序将会在你设定的时间自动运行，也可手动进入 `Action -> Daily Report-> run  workflow` 点击运行

## 贡献
我们欢迎各种形式的贡献。要贡献，请：
1. Fork仓库。
2. 创建您的功能分支。
3. 如果您添加了功能，请添加测试。
4. 确保您的更改符合项目的编码风格。
5. 提交合并请求。

## 许可证
根据 [Apache 许可证](LICENSE) 许可。

## 联系方式
如需支持或查询，请通过[zihan.jian@outlook.com](mailto:zihan.jian@outlook.com)与我联系。
