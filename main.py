from Conta import Conta
from Usuario import Usuario
from Endereco import Endereco
from Salvador import Salvador
from UsuarioRepository import UsuarioRepository
from UsuarioRepositoryArquivo import UsuarioRepositoryArquivo


repository: Salvador = UsuarioRepository()

usuario = Usuario(nome= "Rodrigo",
  sobrenome= "Mosken",
  telefone= "11948977666",
  cpf= "77777777777",
  endereco= Endereco(
    cep ="05496494",
    numero = "2",
    complemento ="",
    estado= "SP",
    cidade= "São Paulo",
    rua= "Av. Paulista"
  )
)


repository.salvar(usuario)

usuarios =repository.listar()

print(usuarios)