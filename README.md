# 🍽️ LangChain Cuisine Menu Generator

A simple **LangChain + Ollama + LLaMA 3.2** project that generates a restaurant name and a sample menu based on a selected cuisine.

The entire LLM pipeline runs **locally** using Ollama, so no OpenAI API key or cloud API is required.

---

## ✨ Features

- 🤖 Uses **LLaMA 3.2** locally through Ollama
- 🔗 Built with **LangChain**
- 🍜 Generates a restaurant name based on cuisine
- 📋 Generates the top 10 menu items for the generated restaurant
- 🔄 Uses a two-step LLM pipeline
- 🔐 No API key required
- 💻 Runs completely on your local machine
- 🎨 Creative restaurant suggestions using configurable temperature

---

## 🧠 How It Works

The project uses a simple two-step pipeline:

```text
User
 │
 │  Cuisine
 ▼
┌──────────────────────┐
│   cuisine_name()     │
│                      │
│ PromptTemplate       │
│        ↓             │
│     LLaMA 3.2        │
└──────────┬───────────┘
           │
           │ Restaurant Name
           ▼
┌──────────────────────┐
│    menu_items()      │
│                      │
│ PromptTemplate       │
│        ↓             │
│     LLaMA 3.2        │
└──────────┬───────────┘
           │
           ▼
      Menu Items
