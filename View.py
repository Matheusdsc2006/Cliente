from models.Cliente import Cliente, NCliente
from models.Servico import Servico, NServico
from models.Agenda import Agenda, NAgenda

class Views:
  def Cliente_Inserir(nome, email, fone):
    cliente = Cliente(0, nome, email, fone)
    NCliente.inserir(cliente)

  def Cliente_Listar():
    return NCliente.listar()
  
  def Cliente_Atualizar(id, nome, email, fone):
    cliente = Cliente(id, nome, email, fone)
    NCliente.atualizar(cliente)

  def Cliente_Excluir(id):
    cliente = Cliente(id, "", "", "")
    NCliente.excluir(cliente)

  def Servico_Inserir(nome, email, fone):
    servico = Servico(0, nome, email, fone)
    NServico.inserir(servico)

  def Servico_Listar():
    return NServico.listar()
  
  def Servico_Atualizar(id, nome, email, fone):
    servico = Servico(id, nome, email, fone)
    NServico.atualizar(servico)

  def Servico_Excluir(id):
    servico = Servico(id, "", "", "")
    NServico.excluir(servico)

  def Agenda_Inserir(nome, email, fone):
    agenda = Agenda(0, nome, email, fone)
    NAgenda.inserir(agenda)

  def Agenda_Listar():
    return NAgenda.listar()
  
  def Agenda_Atualizar(id, nome, email, fone):
    agenda = Agenda(id, nome, email, fone)
    NAgenda.atualizar(agenda)

  def Agenda_Excluir(id):
    agenda = Agenda(id, "", "", "")
    NAgenda.excluir(agenda)