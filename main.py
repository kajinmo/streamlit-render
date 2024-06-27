import streamlit as st
import pandas as pd


list_jogos = ['Alemanha x Brasil', 'Canadá x Bolívia', 'Espanha x Austrália']

with st.form("my_form"):
    st.write("Mama eu :sunglasses:")

    for jogo in list_jogos:
        st.write(r"Jogo: {}".format(jogo))
        time1 = jogo.split(' x ')[0]
        time2 = jogo.split(' x ')[1]
        number1 = st.number_input(time1, value=None, placeholder="Defina o número de gols de {}".format(time1))
        number2 = st.number_input(time2, value=None, placeholder="Defina o número de gols de {}".format(time1))


    st.form_submit_button(label="Submit")
    #  streamlit run main.py [-- script args]