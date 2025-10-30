"""
Agent Memory AI - 高级检索示例

演示多种检索方式和高级功能
"""

from agent_memory import AgentMemory
from datetime import datetime, timedelta

def main():
    """高级检索示例"""
    
    print("=" * 60)
    print("Agent Memory AI - 高级检索示例")
    print("=" * 60)
    
    # 创建实例
    agent = AgentMemory(
        user_id='advanced_user',
        db_path='./advanced_memory.db'
    )
    
    # 准备测试数据
    print("\n📝 准备测试数据...")
    test_memories = [
        "我在 2024 年学习了 Python 编程",
        "我的工作是软件工程师，主要使用 Python",
        "我喜欢阅读技术博客，特别是关于 AI 的",
        "昨天我完成了一个机器学习项目",
        "我计划明年学习 Rust 语言",
        "我的生日是 5 月 20 日，最喜欢的颜色是蓝色",
        "我住在北京，喜欢这个城市的文化氛围",
        "我每周去健身房三次，保持健康很重要",
    ]
    
    for text in test_memories:
        agent.memorize(text)
    
    print(f"✅ 已存储 {len(test_memories)} 条记忆\n")
    
    # 1. 关键词检索
    print("1️⃣  关键词检索")
    print("-" * 60)
    keywords = ['Python', 'AI', '健康']
    for keyword in keywords:
        results = agent.recall(keyword, top_k=3)
        print(f"\n🔍 搜索: {keyword}")
        for i, mem in enumerate(results, 1):
            print(f"   {i}. {mem.content}")
    
    # 2. 按重要性筛选
    print("\n\n2️⃣  按重要性筛选")
    print("-" * 60)
    all_memories = agent.get_all_memories()
    important_memories = [m for m in all_memories if m.importance > 0.5]
    print(f"📊 重要记忆（重要性 > 0.5）: {len(important_memories)} 条")
    for i, mem in enumerate(important_memories[:5], 1):
        print(f"   {i}. {mem.content} (重要性: {mem.importance:.2f})")
    
    # 3. 按时间筛选
    print("\n\n3️⃣  按时间筛选")
    print("-" * 60)
    recent_time = datetime.now() - timedelta(hours=1)
    recent_memories = [m for m in all_memories 
                      if m.created_at > recent_time]
    print(f"📅 最近 1 小时的记忆: {len(recent_memories)} 条")
    for i, mem in enumerate(recent_memories[:5], 1):
        print(f"   {i}. {mem.content}")
    
    # 4. 组合检索
    print("\n\n4️⃣  组合检索（关键词 + 重要性）")
    print("-" * 60)
    results = agent.recall('学习', top_k=10)
    filtered = [m for m in results if m.importance > 0.3]
    print(f"🔍 搜索'学习'并筛选重要性 > 0.3: {len(filtered)} 条")
    for i, mem in enumerate(filtered, 1):
        print(f"   {i}. {mem.content} (重要性: {mem.importance:.2f})")
    
    # 5. 统计分析
    print("\n\n5️⃣  统计分析")
    print("-" * 60)
    stats = agent.get_statistics()
    print(f"📊 总记忆数: {stats.get('total_memories', 0)}")
    print(f"📊 平均重要性: {sum(m.importance for m in all_memories) / len(all_memories):.2f}")
    print(f"📊 最高重要性: {max(m.importance for m in all_memories):.2f}")
    print(f"📊 最低重要性: {min(m.importance for m in all_memories):.2f}")
    
    print("\n" + "=" * 60)
    print("高级检索示例完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()

