from usuario import Usuario
from usuario_dao import UsuarioDAO
from logger_base import log

opcion = None

while opcion!=5:
    print('Opciones:')
    print('1. Listar usuarios')
    print('2. Agregar usuarios')
    print('3. Modificar usuarios')
    print('4. Eliminar usuarios')
    print('5. Salir')
    opcion = int(input('Escribe una opcion (1-5):'))
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('Escribe el username: ')
        password_var = input('Escribe el password: ')   
        usuario = Usuario(username=username_var,password=password_var)   
        usuarios_insertados = UsuarioDAO.insertar(usuario)
        log.info(f'Usuarios insertados: {usuarios_insertados}')
    elif opcion == 3:
        id_usuario_var = int(input("Escribel el id_usuario a modificar: "))
        username_var = input('Escribe el nuevo username: ')
        password_var = input('Escribe el nuevo password: ')
        usuario = Usuario(id_usuario_var,username_var,password_var)
        usuarios_actualizados = UsuarioDAO.actualizar(usuario)
        log.info(f'Usuario actualizados: {usuarios_actualizados}')
    elif opcion == 4:
        id_usuario_var = int(input("Escribe el id_usuario a eliminar: "))
        usuario = Usuario(id_usuario=id_usuario_var)
        usuarios_eliminados = UsuarioDAO.eliminar(usuario)
        log.info(f'Usuarios eliminados: {usuarios_eliminados}')        
    else:   
        log.info('Salimos de la aplicacion.')     
            