Langchain Cuisine Menu

A small LangChain + Ollama pipeline that, given a cuisine type, suggests a restaurant and generates a sample menu for it using a local LLaMA 3.2 model.

How it works
cuisine_name(cuisine) — takes a cuisine (e.g. "Italian") and asks the LLM to suggest one restaurant name for that cuisine.
menu_items(response) — takes the restaurant name from step 1 and asks the LLM to generate the top 10 menu items for that restaurant, grouped under a "MENU ITEMS:" heading.

Both steps are built as LangChain PromptTemplate → LLM chains (prompt | llm) using ChatOllama.

Requirements
Python 3.10+
Ollama installed and running locally
The llama3.2 model pulled:
bash
  ollama pull llama3.2
Python packages:
bash
  pip install langchain langchain-community langchain-ollama
Project structure
genAi/
├── genai_1.py          # entry point, imports resto_cuisine
├── resto_cuisine.py    # cuisine_name() and menu_items() chain logic
├── requirements.txt    # (optional) pinned dependencies
└── README.md
Usage
bash
python genai_1.py

Or, if the entry point is a Streamlit app:

bash
streamlit run genai_1.py
Example
python
from resto_cuisine import cuisine_name, menu_items

restaurant = cuisine_name("Italian")
menu = menu_items(restaurant)
print(menu)
Notes
The LLM is configured with temperature=0.97 for more varied/creative suggestions — lower this for more consistent output.
Model runs entirely locally via Ollama; no API key required.
License

MIT
