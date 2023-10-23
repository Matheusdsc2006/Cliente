
from templates.ManterClienteUI import ManterClienteUI
from templates.ManterServicoUI import ManterServicoUI
from templates.ManterAgendaUI import ManterAgendaUI
import streamlit as st

class IndexUI:
  def sidebar():
      op = st.sidebar.selectbox("Menu", ["Manter Clientes", "Manter Serviços", "Manter Agenda"])
      if op == "Manter Clientes": ManterClienteUI.Main()
      if op == "Manter Serviços": ManterServicoUI.Main()
      if op == "Manter Agenda": ManterAgendaUI.Main()

  def main():
    IndexUI.sidebar()

IndexUI.main()