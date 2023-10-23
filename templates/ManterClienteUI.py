import streamlit as st
import pandas as pd
from View import Views
import time

class ManterClienteUI:
  def Main():
    st.header("Cadastro de Clientes")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1:
      ManterClienteUI.Cliente_Listar()
    with tab2:
      ManterClienteUI.Cliente_Inserir()
    with tab3:
      ManterClienteUI.Cliente_Atualizar()
    with tab4:
      ManterClienteUI.Cliente_Excluir()

  def Cliente_Listar():
    clientes = Views.Cliente_Listar()
    dic = []
    for c in clientes:
      dic.append(c.__dict__)
    df = pd.DataFrame(dic)
    st.dataframe(df)

  def Cliente_Inserir():
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    fone = st.text_input("Informe o fone")
    if st.button("Inserir"):
      Views.Cliente_Inserir(nome, email, fone)
      st.success("Cliente inserido com sucesso")
      time.sleep(2)
      st.rerun()
  
  def Cliente_Atualizar():
    clientes = Views.Cliente_Listar()
    op = st.selectbox("Atualização de Clientes", clientes)
    nome = st.text_input("Informe o novo nome")
    email = st.text_input("Informe o novo e-mail")
    fone = st.text_input("Informe o novo fone")
    if st.button("Atualizar"):
      id = op.get_id()
      Views.Cliente_Atualizar(id, nome, email, fone)
      st.success("Cliente atualizado com sucesso")
      time.sleep(2)
      st.rerun()

  def Cliente_Excluir():
    clientes = Views.Cliente_Listar()
    op = st.selectbox("Exclusão de Clientes", clientes)
    if st.button("Excluir"):
      id = op.get_id()
      Views.Cliente_Excluir(id)
      st.success("Cliente excluído com sucesso")
      time.sleep(2)
      st.rerun()
