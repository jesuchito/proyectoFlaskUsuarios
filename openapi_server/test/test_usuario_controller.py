import unittest

from flask import json

from openapi_server.models.contenido import Contenido  # noqa: E501
from openapi_server.models.usuario import Usuario  # noqa: E501
from openapi_server.test import BaseTestCase


class TestUsuarioController(BaseTestCase):
    """UsuarioController integration test stubs"""

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_add_favorito(self):
        """Test case for add_favorito

        Añadir un nuevo contenido al listado de favoritos de un usuario por su ID
        """
        body = 56
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/usuario/{id_usuario}/ListaFavoritos'.format(id_usuario=56),
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_add_usuario(self):
        """Test case for add_usuario

        Añadir un nuevo usuario a la aplicación
        """
        usuario = {"idUsuario":5,"imagen":["imagen","imagen"],"favoritos":[10,10],"nombre":"Marcos","rol":"administrador"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/usuario',
            method='POST',
            headers=headers,
            data=json.dumps(usuario),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_contenido_favorito(self):
        """Test case for delete_contenido_favorito

        Eliminar un contenido multimedia marcado como favorito del listado de favoritos de un usuario
        """
        headers = { 
        }
        response = self.client.open(
            '/usuario/{id_usuario}/{contenido_favorito}'.format(id_usuario=56, contenido_favorito=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_usuario(self):
        """Test case for delete_usuario

        Eliminar un usuario específico por su ID
        """
        headers = { 
        }
        response = self.client.open(
            '/usuario/{id_usuario}'.format(id_usuario=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_usuarios(self):
        """Test case for get_all_usuarios

        Obtener la lista de usuarios registrados en la aplicación
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/usuario',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_contenido_favorito(self):
        """Test case for get_contenido_favorito

        Obtener un contenido multimedia marcado como favorito de un usuario
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/usuario/{id_usuario}/{contenido_favorito}'.format(id_usuario=56, contenido_favorito=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_favoritos(self):
        """Test case for get_favoritos

        Obtener el listado de contenidos multimedia favoritos de un usuario por su ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/usuario/{id_usuario}/ListaFavoritos'.format(id_usuario=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_usuario_by_id(self):
        """Test case for get_usuario_by_id

        Obtener un usuario específico por su ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/usuario/{id_usuario}'.format(id_usuario=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_update_usuario(self):
        """Test case for update_usuario

        Actualizar un usuario específico por su ID
        """
        usuario = {"idUsuario":5,"imagen":["imagen","imagen"],"favoritos":[10,10],"nombre":"Marcos","rol":"administrador"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/usuario/{id_usuario}'.format(id_usuario=56),
            method='PUT',
            headers=headers,
            data=json.dumps(usuario),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
