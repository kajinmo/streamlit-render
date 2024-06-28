import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

list_jogos = ['Alemanha x Brasil', 'Canadá x Bolívia', 'Espanha x Austrália']

st.set_page_config(layout="wide")
st.title("BOLÃO PLAYERS EURO2024")

custom_css = """
<style>
div[data-baseweb="input"] input[type="number"] {
    width: 70px;
}
img.circular {
    display: block;
    margin-left: auto;
    margin-right: auto;
    border-radius: 50%;
    width: 150px;
    height: 150px;
    object-fit: cover;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.5, 1.5, 1.0])

with col1:
    st.header("Selecione o seu usuário")
    user = st.selectbox("Usuário", ["PITBULL DO SAMBA", "Usuário 2", "Usuário 3", "Usuário 4", "Usuário 5"])
    
    if user == "PITBULL DO SAMBA":
        st.image("pitbull.jpg", caption="PITBULL DO SAMBA", width=150, use_column_width=False)
        st.markdown('<style>img[alt="PITBULL DO SAMBA"]{border-radius: 50%;}</style>', unsafe_allow_html=True)
    elif user == "Usuário 2":
        st.image("user2.jpg", caption="Usuário 2", width=150, use_column_width=False)
        st.markdown('<style>img[alt="Usuário 2"]{border-radius: 50%;}</style>', unsafe_allow_html=True)
    elif user == "Usuário 3":
        st.image("user3.jpg", caption="Usuário 3", width=150, use_column_width=False)
        st.markdown('<style>img[alt="Usuário 3"]{border-radius: 50%;}</style>', unsafe_allow_html=True)
    elif user == "Usuário 4":
        st.image("user4.jpg", caption="Usuário 4", width=150, use_column_width=False)
        st.markdown('<style>img[alt="Usuário 4"]{border-radius: 50%;}</style>', unsafe_allow_html=True)
    elif user == "Usuário 5":
        st.image("user5.jpg", caption="Usuário 5", width=150, use_column_width=False)
        st.markdown('<style>img[alt="Usuário 5"]{border-radius: 50%;}</style>', unsafe_allow_html=True)

with col2:
    with st.form("my_form"):
        for jogo in list_jogos:
            st.write(f"Jogo: {jogo}")
            time1, time2 = jogo.split(' x ')
            col_time1, col_time2 = st.columns([0.5, 0.5])
            with col_time1:
                number1 = st.number_input(f"{time1}", value=0, min_value=0, max_value=10, step=1, key=f"{time1}_score")
            with col_time2:
                number2 = st.number_input(f"{time2}", value=0, min_value=0, max_value=10, step=1, key=f"{time2}_score")

        submitted = st.form_submit_button("Submit")
        if submitted:
            st.text("Seu voto foi submetido")

# Dados fictícios de pontuações
users = ["PITBULL DO SAMBA", "Usuário 2", "Usuário 3", "Usuário 4", "Usuário 5"]
scores = [85, 90, 75, 60, 95]

with col3:
    st.header("Pontuações dos Usuários")
    fig, ax = plt.subplots()
    ax.barh(users, scores, color='skyblue')
    ax.set_xlabel('Pontuação')
    ax.set_ylabel('Usuários')
    ax.set_title('Pontuações dos Usuários')
    st.pyplot(fig)
