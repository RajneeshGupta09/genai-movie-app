from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

from langchain_mistralai import ChatMistralAI


model = ChatMistralAI(model = "mistral-small-2506")

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are an expert movie analyst, film critic, and data summarizer. "
     "You provide structured, accurate, and detailed movie insights."
    ),

    ("human",
     """
Analyze the following movie description and generate a complete report:

🎬 1. Basic Information:
- Movie Title (if possible)
- Director
- Main Cast
- Genre
- Release Year (if possible)

🧠 2. Movie Summary:
- Short summary (2-3 lines)

📖 3. Detailed Plot:
- Clear but concise explanation of story

🎭 4. Characters:
- Main characters and their roles

🎯 5. Themes & Messages:
- Core ideas or moral of the movie

🔥 6. Key Highlights:
- Important scenes or turning points

💰 7. Box Office & Earnings:
- Budget (if known)
- Total collection / revenue (if known)

⭐ 8. Audience & Critic Reception:
- Public reviews summary
- Critic opinion (if known)
- IMDb/ratings (if possible)

👍👎 9. Pros and Cons:
- Strengths
- Weaknesses

🏁 10. Final Verdict:
- Short conclusion

⚠️ Important Instructions:
- If any information is not available, write "Not Available"
- Keep response structured and clean
- Avoid hallucination (do not guess unknown facts)

Movie Description:
{paragraph}
     """
    )
])

para = input('Enter Pragraph ')
final_prompt = prompt.invoke(
    {"paragraph": para}
)

response = model.invoke(final_prompt)

print(response.content)





