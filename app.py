import streamlit as st
import google.generativeai as genai

# Configure page
st.set_page_config(
    page_title="AI Email Generator",
    page_icon="📧",
    layout="centered"
)

st.title("📧 AI Email Generator")
st.write("Generate professional emails instantly using Google Gemini AI.")
