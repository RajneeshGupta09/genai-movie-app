from dotenv import load_dotenv

load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta"
)

model = ChatHuggingFace(llm=llm)
response = model.invoke("who are they, does illuminati exists")
print(response.content)