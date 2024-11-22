import connexion
from typing import Dict
from typing import Tuple
from typing import Union

import requests

from openapi_server.models.usuario import Usuarios  # noqa: E501
from openapi_server import util

from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request, render_template, make_response

db = SQLAlchemy()

def import_db_controller(database):
    global db
    db = database


def add_favorito(id_usuario, contenido_favorito):  # noqa: E501
    """Añadir un nuevo contenido al listado de favoritos de un usuario por su ID

    Añade un nuevo contenido al conjunto de contenidos multimedia favoritos de un usuario específico en función de su identificador # noqa: E501

    :param id_usuario: ID del usuario al que se le añadirá un contenido a su lista de favoritos
    :type id_usuario: int
    :param body: 
    :type body: int

    :rtype: Union[Contenido, Tuple[Contenido, int], Tuple[Contenido, int, Dict[str, str]]
    """
    return 'do some magicsad'


def add_usuario():  # noqa: E501
    """Añadir un nuevo usuario a la aplicación

    Crea una nueva cuenta en la aplicación que estará asociada a un nuevo usuario # noqa: E501

    :param usuario: 
    :type usuario: dict | bytes

    :rtype: Union[Usuario, Tuple[Usuario, int], Tuple[Usuario, int, Dict[str, str]]
    """
    try:
    # Obtener los datos de la solicitud JSON
        data = connexion.request.get_json()
        if not data:
            return {"error": "No data provided"}, 400  # Código 400: No se proporcionaron datos
    
    # Verificar que todos los campos requeridos están presentes
        required_fields = ['nombre', 'rol', 'imagen', 'contenidosfavoritos']
        for field in required_fields:
            if field not in data:
                return {"error": f"Missing field: {field}"}, 422  # Código 422: Falta un campo requerido

    # Validar los valores de 'rol' e 'imagen' (comprobamos si son válidos)
        valid_rol = ['cliente']
        if data['rol'] not in valid_rol:
            return {"error": "Rol Invalido. Rol valido: cliente"}, 422  # Código 422: Rol no válido

    # SOLO EL ADMINISTRADOR PODRA TENER LA FOTO DE PERFIL 'administrador.jpg' Y EL ROL 'administrador' -> AÑADIDO DIRECTAMENTE DE LA BASE DE DATOS
        valid_imagen = ['user1.jpg', 'user2.jpg', 'user3.jpg', 'user4.jpg', 'user5.jpg', 'user6.jpg', 'administrador.jpg']
        if data['imagen'] not in valid_imagen:
            return {"error": "Imagen Invalida. Imagenes validas: user1.jpg, user2.jpg, user3.jpg, user4.jpg, user5.jpg, user6.jpg (o administrador.jpg para el admin)"}, 422  # Código 422: Imagen no válida

    # Asignar los valores de los campos
        nombre = data['nombre']
        rol = data['rol']
        imagen = data['imagen']
        contenidosfavoritos = data['contenidosfavoritos']

    # Crear el nuevo usuario
        new_usuario = Usuarios(
            nombre=nombre,
            rol=rol,
            imagen=imagen,
            contenidosfavoritos=contenidosfavoritos
        )

    # Guardar el usuario en la base de datos
        db.session.add(new_usuario)
        db.session.commit()

    # Retornar el usuario creado como diccionario
        return new_usuario.to_dict(), 200  # Código 200: Usuario creado exitosamente

    except Exception as e:
    # En caso de error, retornar un mensaje con detalles
        return {"error": f"An error occurred: {str(e)}"}, 500  # Código 500: Error del servidor


def delete_contenido_favorito(id_usuario, contenido_favorito):  # noqa: E501
    """Eliminar un contenido multimedia marcado como favorito del listado de favoritos de un usuario

    Elimina un contenido multimedia perteneciente al listado de contenidos favoritos de un usuario específico en función de su identificador # noqa: E501

    :param id_usuario: ID del usuario del que se eliminará el contenido de su lista de favoritos
    :type id_usuario: int
    :param contenido_favorito: ID del contenido marcado como favorito que se eliminará del listado de favoritos
    :type contenido_favorito: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def delete_usuario(id_usuario):  # noqa: E501
    """Eliminar un usuario específico por su ID

    Elimina un contenido multimedia específico de la aplicación en función del identificador proporcionado # noqa: E501

    :param id_usuario: ID del usuario a borrar
    :type id_usuario: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    try:
    # Asegurarse de que el ID proporcionado es un número entero
        id_usuario = int(id_usuario)
        
    # Buscar el usuario en la base de datos
        usuario = db.session.query(Usuarios).get(id_usuario)
        
        if usuario is None:
        # Si el usuario no se encuentra, devolver un error 404
            return jsonify({'error': 'Usuario no encontrado'}), 404

    # Eliminar el usuario de la sesión actual si estaba en otra sesión
        db.session.expunge(usuario)
        
    # Eliminar el usuario de la base de datos
        db.session.delete(usuario)
        db.session.commit()

    # Confirmar que el usuario fue eliminado correctamente
        return jsonify({'message': 'Usuario eliminado correctamente'}), 200

    except ValueError:
        # Devolver un error 400 si el ID proporcionado no es un número entero
        return jsonify({'error': 'ID inválido, debe ser un número entero'}), 400

    except Exception as e:
        # Capturar cualquier otro error y devolver un error 500 con detalles adicionales
        return jsonify({'error': f'Error en el servidor: {str(e)}'}), 500


def get_all_usuarios():  # noqa: E501
    """Obtener la lista de usuarios registrados en la aplicación

    Retorna el conjunto de usuarios registrados en la aplicación # noqa: E501


    :rtype: Union[List[Usuario], Tuple[List[Usuario], int], Tuple[List[Usuario], int, Dict[str, str]]
    """
    usuarios = Usuarios.query.all()
    
    usuarios_favoritos = []
    for usuario in usuarios:
        favoritos = []
        for id in usuario.contenidosfavoritos:
            url = f'http://127.0.0.1:8080/contenido/{id}'
            response = requests.get(url)
            if response.status_code == 200:
                favoritos.append(response.json())
            else:
                print(f"Error al recuperar el contenido con id {id}: {response.status_code}")
        vistas_dict = {
            "idusuario": usuario.idusuario,
            "nombre": usuario.nombre,
            "rol": usuario.rol,  
            "imagen": usuario.imagen,
            "contenidosfavoritos": usuario.contenidosfavoritos,
            "favoritos": favoritos
        }
        usuarios_favoritos.append(vistas_dict)

    return usuarios_favoritos


def get_contenido_favorito(id_usuario, contenido_favorito):  # noqa: E501
    """Obtener un contenido multimedia marcado como favorito de un usuario

    Retorna un contenido multimedia perteneciente al listado de contenidos favoritos de un usuario específico en función de su identificador # noqa: E501

    :param id_usuario: ID del usuario del que se obtendrá el contenido de su lista de favoritos
    :type id_usuario: int
    :param contenido_favorito: ID del contenido marcado como favorito que se obtendrá
    :type contenido_favorito: int

    :rtype: Union[Contenido, Tuple[Contenido, int], Tuple[Contenido, int, Dict[str, str]]
    """
    usuario = Usuarios.query.filter_by(idusuario=id_usuario).first()
    
    url = f'http://127.0.0.1:8080/contenido/{contenido_favorito}'
    response = requests.get(url)
    if response.status_code == 200:
        contenido = response.json()
    else:
        print(f"Error al recuperar el contenido con id {contenido_favorito}: {response.status_code}")

    return contenido


def get_favoritos(id_usuario):  # noqa: E501
    """Obtener el listado de contenidos multimedia favoritos de un usuario por su ID

    Retorna el conjunto de contenidos multimedia favoritos de un usuario específico en función de su identificador # noqa: E501

    :param id_usuario: ID del usuario del que se obtendrá su lista de favoritos
    :type id_usuario: int

    :rtype: Union[List[Contenido], Tuple[List[Contenido], int], Tuple[List[Contenido], int, Dict[str, str]]
    """
    usuario = Usuarios.query.filter_by(idusuario=id_usuario).first()
    contenidos = []
    for id in usuario.contenidosfavoritos:
        url = f'http://127.0.0.1:8080/contenido/{id}'
        response = requests.get(url)
        if response.status_code == 200:
            contenidos.append(response.json())
        else:
            print(f"Error al recuperar el contenido con id {id}: {response.status_code}")

    return contenidos


def get_usuario_by_id(id_usuario):  # noqa: E501
    """Obtener un usuario específico por su ID

    Retorna la información de un usuario en función del identificador proporcionado # noqa: E501

    :param id_usuario: ID del usuario a devolver
    :type id_usuario: int

    :rtype: Union[Usuario, Tuple[Usuario, int], Tuple[Usuario, int, Dict[str, str]]
    """
    usuario = Usuarios.query.get_or_404(id_usuario)
    usuarios_dict = {
        "idusuario": usuario.idusuario,
        "nombre": usuario.nombre,
        "rol": usuario.rol,  
        "imagen": usuario.imagen,
        "contenidosfavoritos": usuario.contenidosfavoritos,
        "favoritos": get_favoritos(id_usuario)
    }

    return usuarios_dict


def update_usuario(id_usuario):  # noqa: E501
    """Actualizar un usuario específico por su ID

    Actualiza la información de un usuario registrado en función del identificador proporcionado # noqa: E501

    :param id_usuario: ID del usuario a actualizar
    :type id_usuario: int
    :param usuario: 
    :type usuario: dict | bytes

    :rtype: Union[Usuario, Tuple[Usuario, int], Tuple[Usuario, int, Dict[str, str]]
    """
    try:  
    # Obtener los datos de la solicitud JSON
        data = connexion.request.get_json()
        if not data:
            return {"error": "No data provided"}, 400  # Código 400: No se proporcionaron datos
        
    # Buscar el usuario por ID
        usuario = db.session.query(Usuarios).get(id_usuario)

    # Actualizar solo los campos que fueron enviados en el cuerpo de la solicitud
        if 'nombre' in data:
            usuario.nombre = data['nombre']
        
        if 'rol' in data:          
            # Validar el valor de 'rol' (comprobamos si es válido)
            valid_rol = ['cliente']
            if data['rol'] not in valid_rol:
                return {"error": "Rol Invalido. Rol valido: cliente"}, 422  # Código 422: Rol no válido    
            usuario.rol = data['rol']

        if 'imagen' in data:
            # Validar el valor de 'imagen' (comprobamos si es válido)    
            valid_imagen = ['user1.jpg', 'user2.jpg', 'user3.jpg', 'user4.jpg', 'user5.jpg', 'user6.jpg']
            if data['imagen'] not in valid_imagen:
                return {"error": "Imagen Invalida. Imagenes validas: user1.jpg, user2.jpg, user3.jpg, user4.jpg, user5.jpg, user6.jpg"}, 422  # Código 422: Imagen no válida
            usuario.imagen = data['imagen']

        if 'contenidosfavoritos' in data:
            usuario.contenidosfavoritos = data['contenidosfavoritos']            

        # Guardar los cambios en la base de datos
        db.session.commit()
        
        # Retornar el usuario actualizado como diccionario
        return usuario.to_dict(), 200  # Código 200: Usuario actualizado exitosamente

    except Exception as e:
        # Otro tipo de error
        return {"error": f"An error occurred: {str(e)}"}, 500  # Código 500: Error del servidor

