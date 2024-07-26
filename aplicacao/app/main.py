import streamlit as st
from mongo_db import save, find_by_name, update, delete
import datetime


if 'nome' not in st.session_state:
    st.session_state.nome = ''
if 'idade' not in st.session_state:
    st.session_state.idade = 0
if 'data_nascimento' not in st.session_state:
    st.session_state.data_nascimento = datetime.date.today()

st.title("Formulário de Cadastro")

pesquisa = st.text_input("Pesquisa :badminton_racquet_and_shuttlecock:")

nome = st.text_input("Nome", value=st.session_state.nome)
idade = st.number_input("Idade", value=st.session_state.idade)
data_nascimento = st.date_input("Data de Nascimento", value=st.session_state.data_nascimento)


col1, col2, col3, col4, col5 = st.columns([1, 0.1, 1, 0.1, 1])

with col1:
    if st.button("Pesquisar"):
        data = find_by_name(pesquisa)
        if data:
            st.session_state.nome = data['nome']
            st.session_state.idade = data['idade']
            data_ajustada = datetime.datetime.strptime(data['data_nascimento'], "%d/%m/%Y").date()
            st.session_state.data_nascimento = data_ajustada
            st.session_state.identificador = data['_id']
            st.rerun()  # Recarregar a página para refletir os valores atualizados
        else:
            st.session_state.identificador = None

with col3:
    if st.button("Enviar"):
        data_formatada = data_nascimento.strftime("%d/%m/%Y")
        if nome and idade and data_nascimento:
            st.success("Formulário enviado com sucesso!")
            st.write("Nome:", nome)
            st.write("Idade:", idade)
            st.write("Data de Nascimento:", data_formatada)
        else:
            st.error("Por favor, preencha todos os campos do formulário.")

        if st.session_state.identificador:
            objeto = {
                '_id': st.session_state.identificador,
                'nome': nome,
                'idade': idade,
                'data_nascimento': data_formatada
            }
            update(objeto)
        else:
            objeto = {
                'nome': nome,
                'idade': idade,
                'data_nascimento': data_formatada
            }
            save(objeto)

with col5:
    if st.button("Remover"):
        delete(st.session_state.identificador)