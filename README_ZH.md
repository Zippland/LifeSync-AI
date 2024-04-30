# TaskCopilot

- [English README](README.md)
- [中文 README](README_ZH.md)

## 简介
TaskPilot 是一个高效的项目管理工具，旨在帮助用户优先处理任务并有效管理多个项目。它结合了天气查询功能、Notion 数据库管理、OpenAI GPT 智能建议和自动邮件通知功能，以提高个人和团队的生产效率。

## 功能特点
- 从Openweather得到的每日精准天气数据。
- 从 Notion 数据库动态获取任务信息。
- 使用 OpenAI GPT 生成任务执行的优先级和建议。
- 通过电子邮件自动发送每日任务和建议。

## 安装指南

### 环境要求
- Python 3.8 或更高版本
- Notion 账号和相关 API 访问权限
- OpenAI API 密钥

### 步骤
1. 克隆仓库：
   ```
   git clone https://github.com/Zippland/TaskPilot.git
   ```
2. 进入项目目录：
   ```
   cd TaskPilot
   ```
3. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

## 使用说明
要启动项目，请运行以下命令：
```
python main.py
```
确保在 `config.py` 文件中正确设置了所有必要的配置信息，包括 Notion 的 token、数据库 ID、SMTP 服务器信息和 OpenAI 的 API 密钥。

## 贡献指南
我们欢迎所有形式的贡献，包括错误报告、功能请求和代码提交。请遵循以下步骤贡献你的力量：
1. Fork 仓库并创建你的分支。
2. 如果你添加了功能，请添加测试。
3. 确保你的代码符合现有代码风格。
4. 提交合并请求。

## 许可证
该项目采用 [MIT 许可证](LICENSE)。

## 联系方式
如果你有任何问题，请通过 [email](mailto:your.email@example.com) 联系我们。
