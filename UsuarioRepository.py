from Salvador import Salvador
from Usuario import Usuario

class UsuarioRepository(Salvador):
  
  def salvar(self, objeto: Usuario):
    return objeto.save(force_insert=True)
  
  def buscar(self, id):
    return Usuario.get_by_id(id)
  
  def listar(self):
    return [usu for usu in Usuario.select()]
  
  def deletar(self, id):
    Usuario.delete_by_id(id)