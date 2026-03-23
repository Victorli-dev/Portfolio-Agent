import streamlit as st
from anthropic import Anthropic
from Agent.Setup import initialize_kernel

st.set_page_config(page_title="Document Index Agent", layout="centered")
st.title("Document Index Agent")

config = initialize_kernel()
client = Anthropic(api_key=config["api_key"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.messages.create(
                model=config["model"],
                max_tokens=1024,
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
            )
            reply = response.content[0].text

        st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
