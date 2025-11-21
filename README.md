# LangChain Academy 中文学习笔记

![LangChain Academy](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/66e9eba1020525eea7873f96_LCA-big-green%20(2).svg)

## 📖 关于本仓库

这是从 [LangChain Academy](https://github.com/langchain-ai/langchain-academy) 官方仓库 fork 的中文学习版本。

**主要改进：**
- ✅ 将所有 Jupyter Notebook 中的英文 Markdown 内容翻译为中文
- ✅ 保留所有代码块、链接和技术术语不变
- ✅ 便于中文开发者学习 LangGraph 和 LangChain 生态系统

**原始仓库：** https://github.com/langchain-ai/langchain-academy

## 📚 课程介绍

欢迎来到 LangChain Academy - LangGraph 入门课程！这是一套不断增长的模块，专注于 LangChain 生态系统中的基础概念。

- **Module 0**: 基础设置
- **Module 1-5**: 在 LangGraph 中构建，逐步添加更高级的主题
- **Module 6**: 部署你的 agents

每个模块文件夹中都有一组 notebook。每个 notebook 的顶部都有指向 LangChain Academy 课程的链接，引导你学习相关主题。每个模块还有一个 `studio` 子目录，其中包含一组相关的图���我们将使用 LangGraph API 和 Studio 进行探索。

## 📋 模块内容

### Module 0: 基础知识
- Jupyter Notebook 基础
- LangChain 生态系统概览

### Module 1: LangGraph 核心概念
- 简单图（Simple Graph）
- 链（Chain）
- 路由（Router）
- Agent 基础
- Agent 记忆
- 部署（Deployment）

### Module 2: 状态管理
- 状态模式（State Schema）
- 状态 Reducers
- 多模式（Multiple Schemas）
- 消息过滤与修剪
- Chatbot 外部记忆
- Chatbot 总结

### Module 3: 人机交互
- 断点（Breakpoints）
- 动态断点
- 编辑状态与人工反馈
- 流式传输与中断
- 时间旅行（Time Travel）

### Module 4: 高级模式
- 并行化（Parallelization）
- Map-Reduce 模式
- 子图（Sub-graphs）
- 研究助手（Research Assistant）

### Module 5: 长期记忆
- 记忆存储（Memory Store）
- 记忆 Agent
- 记忆模式：集合（Collection）
- 记忆模式：配置文件（Profile）

### Module 6: 部署
- ���建部署
- 连接到部署
- Assistants
- Double-texting 处理

## 🚀 快速开始

### Python 版本要求

请确保使用 Python 3.11、3.12 或 3.13（高于 3.11 但低于 3.14）。

```bash
python3 --version
```

### 克隆仓库

```bash
git clone https://github.com/your-username/langchain-academy-learning.git
cd langchain-academy-learning
```

或者，你也可以下载 [ZIP 文件](https://github.com/your-username/langchain-academy-learning/archive/refs/heads/main.zip)。

### 创建虚拟环境并安装依赖

#### Mac/Linux/WSL
```bash
python3 -m venv lc-academy-env
source lc-academy-env/bin/activate
pip install -r requirements.txt
```

#### Windows Powershell
```powershell
python3 -m venv lc-academy-env
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
lc-academy-env\scripts\activate
pip install -r requirements.txt
```

### 运行 Notebooks

如果你还没有安装 Jupyter，请按照[此处](https://jupyter.org/install)的安装说明进行操作。

```bash
jupyter notebook
```

### ���置环境变量

#### Mac/Linux/WSL
```bash
export API_ENV_VAR="your-api-key-here"
```

#### Windows Powershell
```powershell
$env:API_ENV_VAR = "your-api-key-here"
```

## 🔑 API 密钥配置

### OpenAI API Key
* 如果你没有 OpenAI API key，可以在[此处](https://openai.com/index/openai-api/)注册
* 在环境中设置 `OPENAI_API_KEY`

### LangSmith API
* 在[此处](https://docs.langchain.com/langsmith/create-account-api-key#create-an-account-and-api-key)注册 LangSmith
* 了解更多关于 LangSmith 的信息，请访问[这里](https://www.langchain.com/langsmith)
* 设置以下环境变量：
  - `LANGSMITH_API_KEY`
  - `LANGSMITH_TRACING_V2=true`
  - `LANGSMITH_PROJECT="langchain-academy"`
* 如果你在欧盟实例上，还需设置 `LANGSMITH_ENDPOINT="https://eu.api.smith.langchain.com"`

### Tavily Search API
* Tavily Search API 是一个为 LLM 和 RAG 优化的搜索引擎
* 你可以在[此处](https://tavily.com/)注册 API key
* 注册简单，提供非常慷慨的免费套餐
* Module 4 中的一些课程会使用 Tavily
* 在环境中设置 `TAVILY_API_KEY`

## 🎨 设置 LangGraph Studio

* Studio 是一个用于查看和测试 agents 的自定义 IDE
* Studio 可以在 Mac、Windows 和 Linux 上本地运行并在浏览器中打开
* 查看[此处](https://docs.langchain.com/langsmith/studio#local-development-server)的本地 Studio 开发服务器文档
* Module 1-5 的 LangGraph Studio 图位于 `module-x/studio/` 文件夹中

### 启动本地开发服务器

在每个模块的 `/studio` 目录中运行以下命令：

```bash
langgraph dev
```

你应该看到以下输出：
```
- 🚀 API: http://127.0.0.1:2024
- 🎨 Studio UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
- 📚 API Docs: http://127.0.0.1:2024/docs
```

打开浏览器并导航到 Studio UI: `https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024`

### 配置 .env 文件

从命令行运行以下命令为 module 1 到 5 创建 .env 文件：

```bash
for i in {1..5}; do
  cp module-$i/studio/.env.example module-$i/studio/.env
  echo "OPENAI_API_KEY=\"$OPENAI_API_KEY\"" > module-$i/studio/.env
done
echo "TAVILY_API_KEY=\"$TAVILY_API_KEY\"" >> module-4/studio/.env
```

## 📝 翻译说明

本仓库的翻译工作：
- 所有 Jupyter Notebook 的 Markdown 单元格已翻译为中文
- 代码块、代码注释保持英文不变
- 技术术语在首次出现时保留英文，后续使用中文
- 所有链接、图片引用保持不变

## 🤝 贡献

欢迎提交 Issue 和 Pull Request 来改进翻译质量！

## 📄 许可证

本项目遵循原始仓库的许可证。

## 🙏 致谢

- 感谢 [LangChain](https://www.langchain.com/) 团队提供优秀的课程内容
- 原始课程仓库: https://github.com/langchain-ai/langchain-academy

---

**Note**: 这是一个学习项目，翻译内容仅供学习参考。如有翻译错误或建议，欢迎提出 Issue。
