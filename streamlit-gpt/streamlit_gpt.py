import streamlit as st
from openai import OpenAI

import os
api_key = "sk-proj-       "

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"assistant","content":"무엇을 알려드릴까요?"}]

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if prompt := st.chat_input("질문을 입력하세요"):
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    response = completion.to_dict()["choices"][0]["message"]["content"]
    st.session_state.messages.append({"role":"assistant","content":response})
    with st.chat_message("assistant"):
        st.markdown(response)