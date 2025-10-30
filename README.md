# 📚 使用示例

本目录包含 Agent Memory AI 的各种使用示例。

---

## 🚀 快速开始

### 安装

```bash
pip install agent-memory-ai
```

### 运行示例

```bash
# 基础使用
python basic_usage.py

# 高级检索
python advanced_retrieval.py

# 商业场景
python commercial_scenarios.py
```

---

## 📋 示例列表

### 1. [basic_usage.py](basic_usage.py)

**基础使用示例**

演示核心功能：
- ✅ 创建记忆系统实例
- ✅ 存储记忆
- ✅ 检索记忆
- ✅ 获取统计信息
- ✅ 查看所有记忆

**适合**：初学者快速入门

```bash
python basic_usage.py
```

---

### 2. [advanced_retrieval.py](advanced_retrieval.py)

**高级检索示例**

演示多种检索方式：
- 🔍 关键词检索
- 📊 按重要性筛选
- 📅 按时间筛选
- 🎯 组合检索
- 📈 统计分析

**适合**：了解高级检索功能

```bash
python advanced_retrieval.py
```

---

### 3. [commercial_scenarios.py](commercial_scenarios.py)

**商业应用场景示例**

演示三大商业场景：
- 🤖 智能客服机器人
- 👤 个人 AI 助手
- 📚 企业知识库

**适合**：了解实际应用场景

```bash
python commercial_scenarios.py
```

---

## 💡 使用建议

### 学习路径

```
1. basic_usage.py        →  掌握基础功能
2. advanced_retrieval.py →  学习高级检索
3. commercial_scenarios.py → 了解商业应用
```

### 修改示例

欢迎修改这些示例以适应您的需求：

```python
# 修改用户ID
agent = AgentMemory('your_user_id', db_path='./your_db.db')

# 修改测试数据
test_data = [
    "您的测试数据1",
    "您的测试数据2"
]
```

---

## 🎯 更多场景

### 智能对话系统

```python
from agent_memory import AgentMemory

class ChatBot:
    def __init__(self, user_id):
        self.memory = AgentMemory(user_id, db_path=f'./{user_id}.db')
    
    def chat(self, user_input):
        # 记住对话
        self.memory.memorize(f"用户说: {user_input}")
        
        # 回忆上下文
        context = self.memory.recall(user_input, top_k=3)
        
        # 生成回复...
        return "基于上下文的回复"
```

### 学习助手

```python
class StudyAssistant:
    def __init__(self, student_id):
        self.memory = AgentMemory(student_id, db_path=f'./{student_id}_study.db')
    
    def remember_concept(self, concept, explanation):
        self.memory.memorize(f"概念: {concept} - {explanation}")
    
    def review(self, topic):
        return self.memory.recall(topic, top_k=5)
```

### 工作日志

```python
class WorkLogger:
    def __init__(self, user_id):
        self.memory = AgentMemory(user_id, db_path='./work_log.db')
    
    def log_task(self, task):
        self.memory.memorize(f"任务: {task}")
    
    def daily_summary(self):
        today_tasks = self.memory.get_all_memories(limit=20)
        return [task.content for task in today_tasks]
```

---

## 📖 文档链接

- [快速开始](../docs/QUICKSTART.md)
- [完整文档](../README.md)
- [商业合作](../COMMERCIAL.md)

---

## ❓ 常见问题

### Q: 示例运行失败？

A: 确保已安装最新版本：
```bash
pip install --upgrade agent-memory-ai
```

### Q: 如何清理示例数据？

A: 删除生成的 `.db` 文件：
```bash
rm *.db
```

### Q: 可以在生产环境使用吗？

A: 可以！这些示例可以作为生产代码的基础，但建议：
- 添加错误处理
- 配置日志记录
- 实现数据备份
- 添加监控告警

---

## 💼 需要定制开发？

如果您需要：
- 🔧 定制功能开发
- 📊 性能优化
- 🏢 企业级部署
- 🎓 技术培训

**请联系我们**：
- 📧 邮箱: yixiaobai1102@gmail.com
- 📄 详情: [商业合作说明](../COMMERCIAL.md)

---

**祝您使用愉快！** 🎉

