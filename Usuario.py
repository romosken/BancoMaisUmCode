
from BaseModel import BaseModel
from Endereco import Endereco
import peewee


class Usuario(BaseModel):
    nome = peewee.CharField()
    sobrenome = peewee.CharField()
    cpf = peewee.CharField(max_length=11, primary_key=True)
    telefone = peewee.CharField()
    endereco = peewee.ForeignKeyField(Endereco, backref="usuario")

    def __dict__(self):
        return {
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "cpf": self.cpf,
            "telefone": self.telefone,
            "endereco": self.endereco.__dict__()
        }

