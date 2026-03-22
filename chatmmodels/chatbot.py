from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


model = ChatMistralAI(model="mistral-small-2506", temperature=1,max_tokens=20)

# List to store the message, chat history
messages= [ 
        SystemMessage(content="you are a serious philosopher")  
]

print("---------------Welcome, Type 0 to exit the application---------")
while True:
    prompt = input("You: ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot: ", response.content)