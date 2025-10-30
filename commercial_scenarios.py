"""
Agent Memory AI - 商业应用场景示例

演示在实际商业场景中的应用
"""

from agent_memory import AgentMemory
from datetime import datetime

class CustomerServiceBot:
    """智能客服机器人示例"""
    
    def __init__(self, customer_id: str):
        self.customer_id = customer_id
        self.memory = AgentMemory(
            user_id=f"customer_{customer_id}",
            db_path=f"./customer_{customer_id}_memory.db"
        )
    
    def handle_conversation(self, user_input: str) -> str:
        """处理用户对话"""
        # 1. 记住当前对话
        self.memory.memorize(f"客户说: {user_input}")
        
        # 2. 回忆相关历史
        history = self.memory.recall(user_input, top_k=3)
        
        # 3. 基于历史提供个性化回复
        if history:
            context = f"我记得您之前提到过: {history[0].content}"
            return f"您好！{context}。有什么可以帮您的吗？"
        else:
            return "您好！有什么可以帮您的吗？"
    
    def get_customer_profile(self) -> dict:
        """获取客户画像"""
        stats = self.memory.get_statistics()
        all_memories = self.memory.get_all_memories()
        
        return {
            "customer_id": self.customer_id,
            "total_interactions": stats.get('total_memories', 0),
            "recent_topics": [m.content for m in all_memories[:5]],
            "important_info": [m.content for m in all_memories if m.importance > 0.7]
        }


class PersonalAssistant:
    """个人 AI 助手示例"""
    
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.memory = AgentMemory(
            user_id=user_id,
            db_path=f"./{user_id}_assistant_memory.db"
        )
    
    def learn_preference(self, preference: str):
        """学习用户偏好"""
        self.memory.memorize(f"用户偏好: {preference}")
        print(f"✅ 已记住您的偏好: {preference}")
    
    def get_recommendations(self, context: str) -> list:
        """基于记忆给出建议"""
        # 回忆相关偏好
        preferences = self.memory.recall(f"偏好 {context}", top_k=5)
        
        recommendations = []
        for pref in preferences:
            recommendations.append(f"基于'{pref.content}'的建议")
        
        return recommendations
    
    def daily_summary(self) -> str:
        """每日总结"""
        today_memories = self.memory.get_all_memories(limit=20)
        
        summary = f"今日共有 {len(today_memories)} 条新记忆\n"
        summary += "重要事项:\n"
        
        important = [m for m in today_memories if m.importance > 0.6]
        for i, mem in enumerate(important[:5], 1):
            summary += f"  {i}. {mem.content}\n"
        
        return summary


class KnowledgeBase:
    """企业知识库示例"""
    
    def __init__(self, org_id: str):
        self.org_id = org_id
        self.memory = AgentMemory(
            user_id=f"org_{org_id}",
            db_path=f"./org_{org_id}_knowledge.db"
        )
    
    def add_knowledge(self, title: str, content: str, category: str):
        """添加知识条目"""
        knowledge_entry = f"[{category}] {title}: {content}"
        self.memory.memorize(knowledge_entry)
        print(f"✅ 已添加知识: {title}")
    
    def search_knowledge(self, query: str, top_k: int = 5) -> list:
        """搜索知识"""
        results = self.memory.recall(query, top_k=top_k)
        return [
            {
                "content": mem.content,
                "relevance": mem.importance,
                "created_at": mem.created_at
            }
            for mem in results
        ]
    
    def get_statistics(self) -> dict:
        """获取知识库统计"""
        stats = self.memory.get_statistics()
        all_knowledge = self.memory.get_all_memories()
        
        return {
            "total_entries": stats.get('total_memories', 0),
            "categories": self._extract_categories(all_knowledge),
            "most_important": max(all_knowledge, key=lambda x: x.importance).content if all_knowledge else None
        }
    
    def _extract_categories(self, knowledge_list: list) -> dict:
        """提取分类统计"""
        categories = {}
        for item in knowledge_list:
            if item.content.startswith('['):
                category = item.content.split(']')[0][1:]
                categories[category] = categories.get(category, 0) + 1
        return categories


def demo_customer_service():
    """演示客服场景"""
    print("\n" + "=" * 60)
    print("场景 1: 智能客服机器人")
    print("=" * 60)
    
    bot = CustomerServiceBot("CS001")
    
    # 模拟对话
    conversations = [
        "我想了解你们的产品",
        "价格是多少？",
        "有什么优惠活动吗？"
    ]
    
    for conv in conversations:
        print(f"\n客户: {conv}")
        response = bot.handle_conversation(conv)
        print(f"客服: {response}")
    
    # 获取客户画像
    profile = bot.get_customer_profile()
    print(f"\n📊 客户画像:")
    print(f"   交互次数: {profile['total_interactions']}")
    print(f"   最近话题: {profile['recent_topics'][:3]}")


def demo_personal_assistant():
    """演示个人助手场景"""
    print("\n" + "=" * 60)
    print("场景 2: 个人 AI 助手")
    print("=" * 60)
    
    assistant = PersonalAssistant("user_alice")
    
    # 学习偏好
    print("\n📚 学习用户偏好...")
    preferences = [
        "我喜欢早上喝咖啡",
        "我偏好简约风格的设计",
        "我关注科技新闻"
    ]
    
    for pref in preferences:
        assistant.learn_preference(pref)
    
    # 给出建议
    print("\n💡 基于偏好的建议:")
    recommendations = assistant.get_recommendations("早餐")
    for i, rec in enumerate(recommendations, 1):
        print(f"   {i}. {rec}")
    
    # 每日总结
    print("\n📅 每日总结:")
    summary = assistant.daily_summary()
    print(summary)


def demo_knowledge_base():
    """演示知识库场景"""
    print("\n" + "=" * 60)
    print("场景 3: 企业知识库")
    print("=" * 60)
    
    kb = KnowledgeBase("tech_company")
    
    # 添加知识
    print("\n📚 添加知识条目...")
    knowledge_items = [
        ("Python 最佳实践", "使用虚拟环境隔离项目依赖", "编程"),
        ("Git 工作流", "使用 feature 分支进行开发", "工具"),
        ("代码审查规范", "每个 PR 至少需要 2 人审核", "流程"),
        ("API 设计原则", "遵循 RESTful 规范，使用语义化命名", "架构")
    ]
    
    for title, content, category in knowledge_items:
        kb.add_knowledge(title, content, category)
    
    # 搜索知识
    print("\n🔍 搜索知识: 'Python'")
    results = kb.search_knowledge("Python", top_k=3)
    for i, result in enumerate(results, 1):
        print(f"   {i}. {result['content']}")
    
    # 统计信息
    print("\n📊 知识库统计:")
    stats = kb.get_statistics()
    print(f"   总条目数: {stats['total_entries']}")
    print(f"   分类统计: {stats['categories']}")


def main():
    """运行所有场景演示"""
    print("\n" + "=" * 60)
    print("Agent Memory AI - 商业应用场景演示")
    print("=" * 60)
    
    # 运行各场景
    demo_customer_service()
    demo_personal_assistant()
    demo_knowledge_base()
    
    print("\n" + "=" * 60)
    print("所有场景演示完成！")
    print("=" * 60)
    print("\n💼 这些只是基础示例，实际应用中可以：")
    print("   1. 集成更复杂的业务逻辑")
    print("   2. 添加更多个性化功能")
    print("   3. 接入企业级数据库")
    print("   4. 实现分布式部署")
    print("\n📧 商业合作请联系: yixiaobai1102@gmail.com")


if __name__ == "__main__":
    main()

