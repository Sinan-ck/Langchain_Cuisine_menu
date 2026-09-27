from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
llm = ChatOllama(model="llama3.2",
                 temperature=0.97)


def cuisine_name(cuisine):
    prompt1 = PromptTemplate(input_variables=["cuisine"],
                             template="suggest one  {cuisine} restaurant ,only name in one line no need more explanation")

    chain1 = prompt1 | llm
    response1 = chain1.invoke({"cuisine":cuisine})
    return response1
def  menu_items(response):
    prompt2 = PromptTemplate(input_variables=["respones1"],template="give the top 10 menus   name only from {response1} restuarant , and print menue items with sub heading MENU ITEMS" )
    chain2 = prompt2 | llm
    response2 = chain2.invoke({"response1":response})
    return response2


 