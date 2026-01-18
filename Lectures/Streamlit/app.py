import streamlit as st
import pandas as pd
import numpy as np

st.title("This is a sample streamlit app")

st.write("Welcome to my first streamlit app")

age = st.slider("Enter your age", min_value=0, max_value = 100)
st.write(f"Your age is {age} years old.")
 
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello {name}!")

programming_languages = ['C++', "Python", "Java", "R"]
select = st.selectbox("Select you favourite programming language:" , options=programming_languages)
st.write("You selected: ", select)

df = pd.DataFrame({
    "name" : ["Ali", "Zara", "Taha", "Sarah", "Fatima"],
    "marks" : [67,98,76,56,66]
})
st.write(df)

st.bar_chart(df, x="name", y="marks")