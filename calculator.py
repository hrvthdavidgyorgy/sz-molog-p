

import streamlit as st
 
st.title("Calculator App using Streamlit")
 
# creates a horizontal line
st.write("---")

# input 1
num1 = st.number_input(label="ird be az eslö számot")
 
# input 2
num2 = st.number_input(label="ird be a második számot")

st.write("Operation")
 
operation = st.radio("Select an operation to perform:",
                    ("Add", "Subtract", "Multiply", "Divide"))
