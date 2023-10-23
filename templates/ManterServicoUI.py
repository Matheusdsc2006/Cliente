import streamlit as st
import pandas as pd
from View import Views
import time

class ManterServicoUI:
    def Main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterServicoUI.Servico_Listar()
        with tab2:
            ManterServicoUI.Servico_Inserir()
        with tab3:
            ManterServicoUI.Servico_Atualizar()
        with tab4:
            ManterServicoUI.Servico_Excluir()

    def Servico_Listar():
        servicos = Views.Servico_Listar()
        dic = []
        for c in servicos:
            dic.append(c.__dict__)
        df = pd.DataFrame(dic)
        st.dataframe(df)

    def Servico_Inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        if st.button("Inserir"):
            Views.Servico_Inserir(nome, email, fone)
            st.success("Serviço inserido com sucesso")
            time.sleep(2)
            st.rerun()
    
    def Servico_Atualizar():
        servicos = Views.Servico_Listar()
        op = st.selectbox("Atualização de Servicos", servicos)
        nome = st.text_input("Informe o novo nome")
        email = st.text_input("Informe o novo e-mail")
        fone = st.text_input("Informe o novo fone")
        if st.button("Atualizar"):
            id = op.get_id()
            Views.Servico_Atualizar(id, nome, email, fone)
            st.success("Serviço atualizado com sucesso")
            time.sleep(2)
            st.rerun()

    def Servico_Excluir():
        servicos = Views.Servico_Listar()
        op = st.selectbox("Exclusão de Servicos", servicos)
        if st.button("Excluir"):
            id = op.get_id()
            Views.Servico_Excluir(id)
            st.success("Serviço excluído com sucesso")
            time.sleep(2)
            st.rerun()