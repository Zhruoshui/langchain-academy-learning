# Module 2: 状态管理与记忆
## 概览

### 1. `state-schema.ipynb` - 状态结构定义
学习使用 TypedDict 和 Pydantic 定义状态模式，理解如何设计图的数据结构。

### 2. `state-reducers.ipynb` - 状态归约器
掌握 `add_messages` reducer 和自定义 reducer，学习如何控制状态更新逻辑。

### 3. `multiple-schemas.ipynb` - 多状态设计
了解不同节点使用不同状态结构的高级用法，实现更灵活的工作流。

### 4. `trim-filter-messages.ipynb` - 消息管理
学习裁剪和过滤消息的技术，避免超出 token 限制。

### 5. `chatbot-summarization.ipynb` - 消息总结
实现滚动摘要机制：当消息过多时自动总结并删除旧消息。

### 6. `chatbot-external-memory.ipynb`  - 持久化存储
使用 SQLite 数据库实现状态持久化，支持跨会话记忆和多用户管理。

---

## 顺序

```
1. state-schema.ipynb          → 理解状态是什么
2. state-reducers.ipynb        → 学习状态如何更新
3. trim-filter-messages.ipynb  → 掌握消息处理技巧
4. chatbot-summarization.ipynb → 实现消息总结
5. chatbot-external-memory.ipynb → 添加持久化存储 
6. multiple-schemas.ipynb      → (可选) 高级用法
```

---

## 核心概念

- **MessagesState** - 预定义的消息状态类型，自动管理消息列表
- **add_messages** - 消息 reducer，支持追加、更新和删除
- **RemoveMessage** - 删除指定消息的标记类型
- **Checkpointer** - 状态持久化组件（MemorySaver / SqliteSaver / PostgresSaver）

