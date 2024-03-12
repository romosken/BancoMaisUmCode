import json
from Salvador import Salvador


class SalvadorDeArquivo(Salvador):

    def sobrescrever_arquivo(self, dados, nome_arquivo):
        with open(nome_arquivo, 'w', encoding="utf8") as arquivo:
            json.dump(dados, arquivo, indent=3, ensure_ascii=False)

    def ler_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'r', encoding="utf8") as arquivo:
            return json.load(arquivo)

    # CRUD  - Create Read Update Delete
