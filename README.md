# SecondBrain

- [English README](README_EN.md)
- [日本語のREADME](README_JP.md)
- [한국어 README](README_KR.md)
- [中文 README](README.md)

## 简介
SecondBrain 是一款高效的人生规划及管理工具，旨在帮助用户对个人事务和个人资源进行优先排序和有效管理。它集成了Notion 数据库管理、OpenAI GPT 支持、智能时间安排、天气查询功能、个人现金流水查询、电子邮件交互等等功能，以提高个人生活效率。

## Roadmap
- [ ] 监控微信的账单流水并绘制收支表单。
- [ ] 通过ms to-do和outlook自动添加和删除日历和日常任务。
- [X] 使用 Openweather 提供的准确的每日天气数据提供出行建议。
- [X] 从 Notion 数据库动态获取任务信息。
- [X] 使用 OpenAI GPT 生成任务执行的优先级和建议。
- [X] 通过电子邮件自动发送每日任务和建议。

## 安装指南

### 环境要求
- Python 3.8 或更高版本
- Notion 账号和相关 API 访问权限
- OpenAI API 密钥

### 步骤
1. 克隆仓库：
   ```
   git clone https://github.com/Zippland/SecondBrain.git
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
该项目采用 [Apache 许可证](LICENSE)。

## 联系方式
如果你有任何问题，请通过 [email](mailto:zihan.jian@outlook.com) 联系我们。
