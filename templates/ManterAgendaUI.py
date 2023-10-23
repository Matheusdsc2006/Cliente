import streamlit as st
import pandas as pd
from View import Views
import time

class ManterAgendaUI:
  def Main():
    st.header("Cadastro de Horários")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1:
      ManterAgendaUI.Agenda_Listar()
    with tab2:
      ManterAgendaUI.Agenda_Inserir()
    with tab3:
      ManterAgendaUI.Agenda_Atualizar()
    with tab4:
      ManterAgendaUI.Agenda_Excluir()

  def Agenda_Listar():
    agendas = Views.Agenda_Listar()
    dic = []
    for c in agendas:
      dic.append(c.__dict__)
    df = pd.DataFrame(dic)
    st.dataframe(df)

  def Agenda_Inserir():
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    fone = st.text_input("Informe o fone")
    if st.button("Inserir"):
      Views.Agenda_Inserir(nome, email, fone)
      st.success("Horário inserido com sucesso")
      time.sleep(2)
      st.rerun()
  
  def Agenda_Atualizar():
    agendas = Views.Agenda_Listar()
    op = st.selectbox("Atualização de Agendas", agendas)
    nome = st.text_input("Informe o novo nome")
    email = st.text_input("Informe o novo e-mail")
    fone = st.text_input("Informe o novo fone")
    if st.button("Atualizar"):
      id = op.get_id()
      Views.Agenda_Atualizar(id, nome, email, fone)
      st.success("Horário atualizado com sucesso")
      time.sleep(2)
      st.rerun()

  def Agenda_Excluir():
    agendas = Views.Agenda_Listar()
    op = st.selectbox("Exclusão de Agendas", agendas)
    if st.button("Excluir"):
      id = op.get_id()
      Views.Agenda_Excluir(id)
      st.success("Horário excluído com sucesso")
      time.sleep(2)
      st.rerun()
