import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="🎬 CineSage",
    page_icon="🎬",
    layout="wide"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
h1, h2, h3 {
    color: #f8fafc;
}
.stTextArea textarea {
    border-radius: 12px;
    padding: 10px;
}
.stButton>button {
    border-radius: 12px;
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    color: white;
    font-weight: bold;
    height: 3em;
    width: 100%;
}
.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.title("🎬 CineSage")
st.markdown("### Your AI-powered Movie Intelligence System 🚀")

# ------------------ SIDEBAR ------------------
with st.sidebar:
    st.header("⚙️ Settings")
    temp = st.slider("Creativity (Temperature)", 0.0, 1.5, 1.0)
    max_tok = st.slider("Max Tokens", 50, 500, 200)

# ------------------ MODEL ------------------
model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=temp,
    max_tokens=max_tok
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert movie analyst, film critic, and data summarizer."),
    ("human", "{paragraph}")
])

# ------------------ INPUT SECTION ------------------
st.subheader("🎥 Enter Movie Description")

col1, col2 = st.columns([3, 1])

with col1:
    user_input = st.text_area(
        "Paste your movie description...",
        height=200
    )

with col2:
    st.markdown("### 💡 Tips")
    st.info("Paste detailed story for better analysis")

# ------------------ BUTTON ------------------
if st.button("✨ Analyze Movie"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter movie description")
    else:
        with st.spinner("Analyzing movie... 🎬"):
            final_prompt = prompt.invoke({"paragraph": user_input})
            response = model.invoke(final_prompt)

        st.success("✅ Analysis Complete")

        result = response.content

        # ------------------ TABS ------------------
        tab1, tab2, tab3 = st.tabs(["📄 Summary", "🎭 Details", "⭐ Review"])

        with tab1:
            st.markdown("### 📄 Summary")
            st.markdown(f'<div class="card">{result}</div>', unsafe_allow_html=True)

        with tab2:
            st.markdown("### 🎭 Movie Breakdown")
            st.markdown(f'<div class="card">{result}</div>', unsafe_allow_html=True)

        with tab3:
            st.markdown("### ⭐ Review & Verdict")
            st.markdown(f'<div class="card">{result}</div>', unsafe_allow_html=True)

# ------------------ FOOTER ------------------
st.markdown("---")
st.markdown("Made with ❤️ by Rajneesh 🚀")