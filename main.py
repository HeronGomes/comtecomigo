import streamlit as st
from  genai import conversa,limpa_historico



if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def zera_historico():

    limpa_historico()
    st.session_state.messages.clear()



st.set_page_config(page_title="Comtecomigo", page_icon=":brain:", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("ComteComigo - Seu amigo virtual nas horas mais complicadas!")
st.info("ComteComigo é um projeto desenvolvido para o desafio de imersão Alura e Google, utilizando tecnologia Gemini 🧡")


mensagem_inicial = "Olá 👋, em que posso ajudar?!?!"
container = st.container(height=300)
container.chat_message("assistant",avatar="🤖").markdown(mensagem_inicial)

with st.container():

    if prompt := st.chat_input("Sua mensagem..."):


        container.chat_message("user", avatar="🗣️").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = conversa(prompt_user=prompt)

        container.chat_message("assistant",avatar="🤖").markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})


    st.button('Limpar',on_click=zera_historico())