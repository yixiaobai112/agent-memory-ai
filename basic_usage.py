"""
Agent Memory AI - 基础使用示例

演示如何使用 Agent Memory AI 的核心功能
"""

from agent_memory import AgentMemory

def main():
    """基础使用示例"""
    
    print("=" * 60)
    print("Agent Memory AI - 基础使用示例")
    print("=" * 60)
    
    # 1. 创建记忆系统实例
    print("\n1️⃣  创建记忆系统实例...")
    agent = AgentMemory(
        user_id='demo_user',
        db_path='./demo_memory.db',
        use_vector_store=False  # 基础版不使用向量存储
    )
    print("✅ 实例创建成功！")
    
    # 2. 存储记忆
    print("\n2️⃣  存储记忆...")
    memories_to_store = [
        "我喜欢 Python 编程，它简洁优雅",
        "我使用 VSCode 作为主要编辑器",
        "我最近在学习机器学习，特别关注深度学习",
        "我每天早上 7 点起床，喜欢晨跑",
        "我的生日是 5 月 20 日"
    ]
    
    for text in memories_to_store:
        agent.memorize(text)
        print(f"  ✅ 已记忆: {text}")
    
    # 3. 检索记忆
    print("\n3️⃣  检索记忆...")
    queries = ['Python', '学习', '早上']
    
    for query in queries:
        print(f"\n  🔍 搜索: {query}")
        results = agent.recall(query, top_k=3)
        
        if results:
            for i, memory in enumerate(results, 1):
                print(f"     {i}. {memory.content}")
        else:
            print("     (未找到相关记忆)")
    
    # 4. 获取统计信息
    print("\n4️⃣  获取统计信息...")
    stats = agent.get_statistics()
    print(f"  📊 总记忆数: {stats.get('total_memories', 0)}")
    print(f"  📊 短期记忆: {stats.get('short_term', 0)}")
    print(f"  📊 长期记忆: {stats.get('long_term', 0)}")
    
    # 5. 获取所有记忆
    print("\n5️⃣  查看所有记忆...")
    all_memories = agent.get_all_memories(limit=10)
    print(f"  共有 {len(all_memories)} 条记忆：")
    for i, mem in enumerate(all_memories, 1):
        print(f"     {i}. {mem.content} (重要性: {mem.importance:.2f})")
    
    print("\n" + "=" * 60)
    print("示例运行完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()

