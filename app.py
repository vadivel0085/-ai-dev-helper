import os
import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="AI Dev Helper",
    page_icon="🤖"
)

st.title("🤖 AI Dev Helper")
st.write(
    "An open-source AI assistant for code documentation, "
    "review, explanations, and developer productivity."
)

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.warning(
        "OPENAI_API_KEY is not configured. "
        "Add it as an environment variable before running the app."
    )
    st.stop()

client = OpenAI(api_key=api_key)

code = st.text_area(
    "Paste your code",
    height=300,
    placeholder="Paste Python, JavaScript, Java, or other code here..."
)

task = st.selectbox(
    "What would you like AI Dev Helper to do?",
    [
        "Explain this code",
        "Review this code",
        "Find possible bugs",
        "Suggest improvements",
        "Generate documentation",
        "Suggest unit tests",
    ],
)

if st.button("✨ Generate"):

    if not code.strip():
        st.error("Please paste some code first.")
        st.stop()

    prompt = f"""
You are an expert software developer.

Task:
{task}

Analyze the following code:

```text
{code}

  with st.spinner("AI is analyzing your code..."):
    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

st.subheader("AI Result")
st.markdown(response.output_text)
