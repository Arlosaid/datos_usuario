from conexion import Conexion
from cursor_del_pool import CursorDelPool
from logger_base import log
from usuario import Usuario


class UsuarioDAO:
    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE  id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando usuarios')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario =Usuario(registro[0],registro[1],registro[2])
                usuarios.append(usuario)
            return usuarios  
        
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.username, usuario.password) 
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount  
        
    @classmethod
    def actualizar(cls,usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a actualizar {usuario}')
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)  
            return cursor.rowcount 
    
    @classmethod
    def eliminar(cls,usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a eliminar: {usuario}')
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount    
        
if __name__ == '__main__':
    #Eliminar registro
    #usuario1 = Usuario(id_usuario=2)
    #persona_eliminadas = UsuarioDAO.eliminar(usuario1)
    #log.debug(f'Persona eliminadas: {persona_eliminadas}')

    #Actualizar registro
    persona1 = Usuario(3,'kgomez', 'abcd')
    personas_actualizadas = UsuarioDAO.actualizar(persona1)
    log.debug(f'Persona actualizadas: {personas_actualizadas}')

    #Insertar registro
    #usuario1 = Usuario(username='ahernandez',password='abcd')
    #personas_insertadas = UsuarioDAO.insertar(usuario1)
    #log.debug(f'Personas insertadas: {personas_insertadas}')

    #Seleccionar objetos
    #personas = UsuarioDAO.seleccionar()
    #for persona in personas:
        #log.debug(persona)