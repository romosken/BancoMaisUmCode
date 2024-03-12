
import os
from SalvadorDeArquivo import SalvadorDeArquivo
from Usuario import Usuario
from Endereco import Endereco


class UsuarioRepositoryArquivo(SalvadorDeArquivo):
    NOME_ARQUIVO = "usuario.json"

    def __init__(self):
        if not os.path.exists(self.NOME_ARQUIVO):
            self.sobrescrever_arquivo([], self.NOME_ARQUIVO)

    def salvar(self, objeto):
        dados = self.listar()
        usuario_existente = self.buscar(objeto.cpf)
        if usuario_existente:
            for i in range(len(dados)):
                if dados[i]['cpf'] == objeto.cpf:
                    dados[i] = objeto.__dict__()
        else:
            dados.append(objeto.__dict__())

        self.sobrescrever_arquivo(dados, self.NOME_ARQUIVO)

    def buscar(self, cpf):
        dados = self.listar()
        for usuario in dados:
            if usuario['cpf'] == cpf:
                return self.converterDicionarioParaObjeto(usuario)
        return None

    def converterDicionarioParaObjeto(self, dicionario):
        return Usuario(
            dicionario.get("nome"),
            dicionario.get("sobrenome"),
            dicionario.get("cpf"),
            dicionario.get("telefone"),
            self.converterEndereco(dicionario.get("endereco"))
        )

    def converterEndereco(self, dicionario):
        return Endereco(
            dicionario.get("cep"),
            dicionario.get("numero"),
            dicionario.get("complemento"),
            dicionario.get("estado"),
            dicionario.get("cidade"),
            dicionario.get("rua")
        )

    def listar(self):
        return self.ler_arquivo(self.NOME_ARQUIVO)

    def deletar(self, cpf):
        dados = self.listar()
        for i in range(len(dados)):
          if dados[i]['cpf'] == cpf:
            del dados[i]
            break

        self.sobrescrever_arquivo(dados, self.NOME_ARQUIVO)

    # CRUD  - Create Read Update Delete
