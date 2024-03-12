from uuid import uuid4
from BaseModel import BaseModel
import peewee


class Endereco(BaseModel):
    id = peewee.UUIDField(primary_key=True, default=uuid4().__str__())
    cep = peewee.CharField(max_length=8)
    numero = peewee.CharField()
    complemento = peewee.CharField()
    estado = peewee.CharField()
    cidade = peewee.CharField()
    rua = peewee.CharField()


    def __dict__(self):
      return {
          "id": self.id,
          "cep": self.cep,
          "numero": self.numero,
          "complemento": self.complemento,
          "estado": self.estado,
          "cidade":self.cidade,
          "rua":self.rua
      }
  # def __init__(self, cep, numero, complemento = None, estado = None, cidade = None, rua = None):
  #   self.id = str(uuid4())
  #   self.cep = cep
  #   self.numero = numero
  #   self.complemento = complemento
  #   self.popular_campos(cep, estado, cidade, rua)

  # def popular_campos(self, cep, estado, cidade, rua):
  #   try:
  #     response = requests.get(f"https://viacep.com.br/ws/{cep}/json/").json()
  #     self.estado = response['uf']
  #     self.cidade = response['localidade']
  #     self.rua = response['logradouro']
  #   except:
  #     self.estado = estado
  #     self.cidade = cidade
  #     self.rua = rua
