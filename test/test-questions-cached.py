import streamlit as st
import vanna as vn
from vanna.remote import VannaDefault

vn = VannaDefault(api_key=st.secrets.get("VANNA_API_KEY"), model='chinook')
vn.connect_to_sqlite("https://vanna.ai/Chinook.sqlite")
vn.ask("What is the total revenue?")
# questions = vn.generate_questions()
# print(questions)
