import streamlit as st
import pandas as pd

st.write("Mama eu :sunglasses:")

list_jogos = ['Alemanha x Brasil', 'Canadá x Bolívia', 'Espanha x Austrália']
number = st.number_input("Insert a number", value=None, placeholder="Type a number...")

for jogo in list_jogos:
    st.write(r"Jogo: {jogo}")
    st.write("The current number is ", number)


st.form_submit_button(label="Submit")