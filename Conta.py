import random

from BaseModel import BaseModel
from Usuario import Usuario
import peewee

class Conta(BaseModel):
  numero = peewee.BigIntegerField(primary_key=True)
  tipo = peewee.CharField(null=False)
  usuario = peewee.ForeignKeyField(Usuario, backref="contas")
  saldo = peewee.FloatField(null=False)
   
  def __init__(self, tipo, usuario, saldo = 0.0):
    self.tipo = tipo
    self.usuario = usuario
    self.saldo = saldo
    self.numero = self.gera_numero_conta()
    
  def gera_numero_conta(self):
    return f'{random.randint(1, 100000):06}'
  
  def depositar(self, valor):
    self.saldo += valor

  def sacar(self, valor):
    if self.saldo - valor >= 0:
      self.saldo -= valor
    else:
      raise Exception("Saldo insuficiente!")

  def transferir(self, conta, valor):
    self.sacar(valor)
    conta.depositar(valor)