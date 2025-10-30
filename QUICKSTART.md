# 🚀 快速开始

本指南将帮助您在 5 分钟内开始使用 Agent Memory AI。

---

## 📦 安装

```bash
pip install agent-memory-ai
```

---

## ⚡ 第一个程序

创建一个新文件 `demo.py`：

```python
from agent_memory import AgentMemory

# 创建实例
agent = AgentMemory('demo_user', db_path='./memory.db')

# 存储记忆
agent.memorize('我喜欢 Python 编程')

# 检索记忆
results = agent.recall('Python')
for memory in results:
    print(memory.content)
```

运行：

```bash
python demo.py
```

输出：
```
我喜欢 Python 编程
```

恭喜！您已经成功使用了 Agent Memory AI！

---

## 🎯 核心概念

### 1. 创建实例

```python
from agent_memory import AgentMemory

agent = AgentMemory(
    user_id='your_user_id',      # 用户ID，用于隔离不同用户的记忆
    db_path='./memory.db',       # 数据库路径（推荐指定）
    use_vector_store=False       # 是否使用向量检索（可选）
)
```

### 2. 存储记忆

```python
# 简单存储
agent.memorize('我喜欢编程')

# 批量存储
texts = ['记忆1', '记忆2', '记忆3']
for text in texts:
    agent.memorize(text)
```

### 3. 检索记忆

```python
# 基础检索
results = agent.recall('编程')

# 指定返回数量
results = agent.recall('编程', top_k=5)

# 处理结果
for memory in results:
    print(f"内容: {memory.content}")
    print(f"重要性: {memory.importance}")
    print(f"创建时间: {memory.created_at}")
```

### 4. 管理记忆

```python
# 获取所有记忆
all_memories = agent.get_all_memories()

# 获取统计信息
stats = agent.get_statistics()
print(f"总记忆数: {stats['total_memories']}")

# 删除记忆
agent.forget_memory(memory_id)

# 按时间清理（删除 30 天前的记忆）
agent.forget_by_time(days_ago=30)
```

---

## 🔧 配置 LLM（可选）

### 方式 1：配置文件

创建 `config.json`：

```json
{
  "llm": {
    "api_key": "sk-您的密钥",
    "base_url": "https://api.openai.com/v1",
    "model": "gpt-3.5-turbo"
  },
  "database": {
    "path": "./memory.db"
  }
}
```

### 方式 2：环境变量

```bash
export OPENAI_API_KEY="sk-您的密钥"
export OPENAI_API_BASE="https://api.openai.com/v1"
```

### 方式 3：代码中配置

```python
import os
os.environ["OPENAI_API_KEY"] = "sk-您的密钥"
```

> **注意**：LLM 配置是可选的。不配置时，系统使用基于规则的策略，核心功能仍可正常使用。

---

## 📚 完整示例

```python
from agent_memory import AgentMemory

def main():
    # 1. 创建实例
    agent = AgentMemory('demo_user', db_path='./demo.db')
    
    # 2. 存储多条记忆
    memories = [
        "我是一名软件工程师",
        "我喜欢 Python 和机器学习",
        "我每天早上 7 点起床",
        "我的生日是 5 月 20 日"
    ]
    
    print("📝 存储记忆...")
    for text in memories:
        agent.memorize(text)
        print(f"  ✅ {text}")
    
    # 3. 搜索记忆
    print("\n🔍 搜索 'Python' 相关记忆:")
    results = agent.recall('Python', top_k=3)
    for i, mem in enumerate(results, 1):
        print(f"  {i}. {mem.content}")
    
    # 4. 查看统计
    print("\n📊 统计信息:")
    stats = agent.get_statistics()
    print(f"  总记忆数: {stats.get('total_memories', 0)}")
    
    # 5. 查看所有记忆
    print("\n📋 所有记忆:")
    all_mems = agent.get_all_memories()
    for i, mem in enumerate(all_mems, 1):
        print(f"  {i}. {mem.content} (重要性: {mem.importance:.2f})")

if __name__ == "__main__":
    main()
```

运行效果：

```
📝 存储记忆...
  ✅ 我是一名软件工程师
  ✅ 我喜欢 Python 和机器学习
  ✅ 我每天早上 7 点起床
  ✅ 我的生日是 5 月 20 日

🔍 搜索 'Python' 相关记忆:
  1. 我喜欢 Python 和机器学习

📊 统计信息:
  总记忆数: 4

📋 所有记忆:
  1. 我是一名软件工程师 (重要性: 0.50)
  2. 我喜欢 Python 和机器学习 (重要性: 0.60)
  3. 我每天早上 7 点起床 (重要性: 0.40)
  4. 我的生日是 5 月 20 日 (重要性: 0.70)
```

---

## 🎯 下一步

- 📖 查看 [完整文档](../README.md)
- 💻 运行 [示例代码](../examples/)
- 🔧 学习 [高级功能](ADVANCED.md)
- 💼 了解 [商业合作](../COMMERCIAL.md)

---

## ❓ 常见问题

### Q: 数据存储在哪里？
A: 默认存储在本地 SQLite 数据库中，您可以通过 `db_path` 参数指定路径。

### Q: 必须配置 LLM 吗？
A: 不需要。不配置时使用基于规则的策略，核心功能仍可正常使用。

### Q: 如何更新包？
A: 运行 `pip install --upgrade agent-memory-ai`

### Q: 支持哪些 Python 版本？
A: Python 3.8 及以上版本。

---

## 📧 需要帮助？

- **邮箱**: yixiaobai1102@gmail.com
- **PyPI**: https://pypi.org/project/agent-memory-ai/

---

**祝使用愉快！** 🎉

