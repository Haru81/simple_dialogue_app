import streamlit as st

st.title("Test App")
text_input = st.text_input("Input")
st.write(f"Your input: {text_input}")