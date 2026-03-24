import streamlit as st
from Agent.Setup import initialize_kernel, create_client

st.set_page_config(page_title="Ask anything about Victor>", layout="centered")
st.title("Victor's Personal AI Agent")

config = initialize_kernel()
client = create_client()

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
                system = 
                '''You are an assistant designed specifically to 
                answer questions about victor li. Answer only using things in your knoweldge base.
                If you do not have the knowledge in your knowledgebase please respond with. I don't have that information 
                on Victor Li
                ''',
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
            )
            reply = response.content[0].text

        st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
