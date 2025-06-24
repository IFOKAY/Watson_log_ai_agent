import streamlit as st
from ibm_watsonx_ai.foundation_models import ModelInference

# Page setup
st.set_page_config(page_title="Watsonx Log AI Chatbot", layout="centered")
st.title("🤖 Ask Log Issue Bot")

# Sidebar config
with st.sidebar:
    st.header("🔧 Watsonx Configuration")
    project_id = st.text_input("Project ID", value="7c7a1f85-5c71-49c7-973b-dab8e9554ff1")
    api_key = st.text_input("API Key", type="password", value=st.session_state.get("api_key", "9xfWwR4t525B3gQPjK_YL5M_ClzCrUPSsFwy18ibiZpY"))
    url = st.text_input("Watsonx URL", value="https://au-syd.ml.cloud.ibm.com")
    model_id = st.text_input("Model ID", value="ibm/granite-3-8b-instruct")

    # Save to session state
    st.session_state.api_key = api_key
    st.session_state.project_id = project_id
    st.session_state.url = url
    st.session_state.model_id = model_id

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Describe your issue...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        # Watsonx inference setup
        model = ModelInference(
            model_id=model_id,
            project_id=project_id,
            credentials={"apikey": api_key, "url": url}
        )

        prompt = f"""
Analyze the following log message and provide:
- Exactly 2 possible root causes
- Exactly 1 suggested solution

Respond in this format:
Root Cause 1: ...
Root Cause 2: ...
Solution: ...

Log message:
{user_input}
"""

        params = {
            "max_new_tokens": 300,
            "temperature": 0.6,
            "decoding_method": "sample",
            "repetition_penalty": 1.1
        }

        result = model.generate_text(prompt=prompt, params=params)

        # Handle both string and dict response
        if isinstance(result, dict):
            response_text = result.get("results", [{}])[0].get("generated_text", "⚠️ No response from Watsonx.")
        else:
            response_text = result

        # Format for display
        formatted_response = f"### 🧠 Analysis Result\n{response_text.strip()}"

    except Exception as e:
        formatted_response = f"❌ Error from Watsonx: {str(e)}"

    # Show bot message
    st.session_state.messages.append({"role": "assistant", "content": formatted_response})
    with st.chat_message("assistant"):
        st.markdown(formatted_response)
