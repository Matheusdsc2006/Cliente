import json

class Agenda:
    def __init__(self, id, data, confirmado, idCliente, idServico):
        self.__id = id
        self.__data = data
        self.__confirmado = confirmado
        self.__idCliente = idCliente
        self.__idServico = idServico
    def set_id(self, id):
        self.__id = id
    def set_idCliente(self, idCliente):
        self.__idCliente = idCliente
    def set_idServico(self, idServico):
        self.__idServico = idServico
    def set_data(self, data):
        self.__data = data
    def set_confirmado(self, confirmado):
        self.__confirmado = confirmado
    def get_id(self):
        return self.__id
    def get_idCliente(self):
        return self.__idCliente
    def get_idServico(self):
        return self.__idServico
    def get_data(self):
        return self.__data
    def get_confirmado(self):
        return self.__confirmado
    def __str__(self):
        return f"id: {self.__id}, idCliente: {self.__idCliente}, idServico: {self.__idServico}, data: {self.__data}, confirmado: {self.__confirmado}"

class NAgenda:
  __agendas = []  # lista de agendas inicia vazia

  @classmethod
  def inserir(cls, obj):
    NAgenda.abrir()
    id = 0  # encontrar o maior id já usado
    for agenda in cls.__agendas:
      if agenda.get_id() > id: id = agenda.get_id()
    obj.set_id(id + 1)
    cls.__agendas.append(obj)  # insere um agenda (obj) na lista
    NAgenda.salvar()

  @classmethod
  def listar(cls):
    NAgenda.abrir()
    return cls.__agendas  # retorna a lista de agendas

  @classmethod
  def listar_id(cls, id):
    NAgenda.abrir()
    for agenda in cls.__agendas:
      if agenda.get_id() == id: return agenda
    return None

  @classmethod
  def atualizar(cls, obj):
    NAgenda.abrir()
    agenda = cls.listar_id(obj.get_id())
    agenda.set_data(obj.get_data())
    agenda.set_confirmado(obj.get_confirmado())
    agenda.set_id_cliente(obj.get_id_cliente())
    agenda.set_id_servico(obj.get_id_servico())
    NAgenda.salvar()

  @classmethod
  def excluir(cls, obj):
    NAgenda.abrir()
    agenda = cls.listar_id(obj.get_id())
    cls.__agendas.remove(agenda)
    NAgenda.salvar()

  @classmethod
  def abrir(cls):
    try:
      cls.__agendas = []
      with open("agendas.json", mode="r") as f:
        s = json.load(f)
        for agenda in s:
          c = Agenda(
            agenda["_Agenda__id"],
            datetime.datetime.strptime(agenda["_Agenda__data"],
                                       "%d/%m/%Y %H:%M"),
            agenda["_Agenda__confirmado"], agenda["_Agenda__id_cliente"],
            agenda["_Agenda__id_servico"])
          cls.__agendas.append(c)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("agendas.json", mode="w") as f:
      json.dump(cls.__agendas, f, default=Agenda.to_json)