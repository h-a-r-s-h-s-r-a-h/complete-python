import streamlit as st
import pandas as pd

st.title("Streamlit Widgets Example")

name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Hello, {name}! You are {age} years old.")

option = ["Python", "Java", "Rust"]
choice = st.selectbox("Choose your favorite programming language:", option)
st.write(f"You selected: {choice}")

if name:
    st.write(f"Hello, {name}!")

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 22],
    "City": ["New York", "Los Angeles", "Chicago"],
}
df = pd.DataFrame(data)
st.write("Here is a sample DataFrame:")
st.dataframe(df)


uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df_uploaded = pd.read_csv(uploaded_file)
    st.write("Data from the uploaded CSV file:")
    st.dataframe(df_uploaded)