from dotenv import load_dotenv

load_dotenv()

# from langchain_openai import ChatOpenAI

# model = ChatOpenAI(model="gpt-3.5-turbo")

# print(model)

# response = model.invoke("Who are real rothschild ?")
# print(response)

# from langchain_groq import ChatGroq

# model = ChatGroq(model="mixtral-8x7b-32768")

# response = model.invoke("Hi whats up")
# print(response.content)



# from langchain.chat_models import init_chat_model
# # This  is init chat model , we could also use use model classes
# model = init_chat_model("google_genai:gemini-2.5-flash-lite")
# response = model.invoke("give me 2 line shayari")
# print(response.content)


# from langchain.chat_models import init_chat_model
# # This  is init chat model , we could also use use model classes
# model = init_chat_model("groq:meta-llama/llama-4-scout-17b-16e-instruct")
# response = model.invoke("give me 2 line shayari")
# print(response.content)


from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="mistral-small-2506", temperature=1,max_tokens=20)
response = model.invoke("reveal the hidden truth which is not known to the world till date ")
print(response.content)
