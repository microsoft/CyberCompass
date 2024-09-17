import streamlit as st
import pandas as pd

st.write("""# Welcome to Cyber Compass""")

prompt = st.chat_input("Say something")
messages = st.container()
messages.chat_message("assistant").write("Please input some data about your experience")
if prompt:
    messages.chat_message("user").write(prompt)
    messages.chat_message("assistant").write(f"The user said: {prompt}")
