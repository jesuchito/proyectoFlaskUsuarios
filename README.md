# Api Usuarios 

<img width="603" alt="image" src="https://github.com/user-attachments/assets/e9785aa7-18d3-493f-b0ed-fc09817966bf">

# Descripción General

Este microservicio de gestión de usuarios está diseñado para la  gestion y administración de usuarios en la aplicación de streaming tipo Netflix. Proporciona funcionalidades clave como el registro,  la gestión del perfil de usuario. Además, permite a los usuarios agregar, eliminar y consultar sus contenidos favoritos, creando una experiencia personalizada que facilita el acceso a sus preferencias. El sistema distingue entre dos tipos de usuarios: clientes, que solo pueden gestionar sus propios datos y favoritos, y administradores, quienes tienen privilegios completos para realizar los post o put en la aplicación.

La API está construida utilizando principios RESTful, lo que permite una comunicación sencilla y eficiente entre el cliente y el servidor. Cada operación es accesible a través de endpoints bien definidos que soportan solicitudes en formato JSON y XML. Además, el sistema está optimizado para garantizar un rendimiento ágil y escalable, lo que facilita su integración en plataformas más grandes. Con una estructura robusta y segura, este microservicio puede ser fácilmente extendido para incluir nuevas funcionalidades y adaptarse a futuras necesidades de la aplicación de streaming.


## Endpoints de la API

- **Obtener lista de usuarios**  
  `GET /usuarios`: Recupera todos los usuarios registrados en el sistema.

- **Crear un nuevo usuario**  
  `POST /usuarios`: Crea un nuevo usuario en el sistema. Los datos del usuario deben incluir nombre, correo electrónico y contraseña.

- **Obtener detalles de un usuario**  
  `GET /usuarios/{idUsuario}`: Recupera la información detallada de un usuario en función de su ID.

- **Actualizar información de un usuario**  
  `PUT /usuarios/{idUsuario}`: Actualiza la información de un usuario existente en el sistema según su ID.

- **Eliminar un usuario**  
  `DELETE /usuarios/{idUsuario}`: Elimina un usuario específico por su ID.

- **Obtener lista de contenidos favoritos de un usuario**  
  `GET /usuarios/{idUsuario}/ListaFavoritos`: Recupera todos los contenidos multimedia favoritos de un usuario en función de su ID.

- **Añadir un contenido a los favoritos de un usuario**  
  `POST /usuarios/{idUsuario}/ListaFavoritos`: Añade un nuevo contenido multimedia a la lista de favoritos de un usuario.

- **Eliminar un contenido de los favoritos de un usuario**  
  `DELETE /usuarios/{idUsuario}/{ContenidoFavorito}`: Elimina un contenido multimedia de la lista de favoritos de un usuario.

- **Obtener un contenido favorito de un usuario**  
  `GET /usuarios/{idUsuario}/{ContenidoFavorito}`: Recupera un contenido multimedia específico de la lista de favoritos de un usuario.



## Tecnologías y Herramientas Usadas:

- Se utilizó **PostgreSQL** como base de datos SQL para almacenar y gestionar los datos de la API.

- **Postman** se utilizó para realizar pruebas de los endpoints de la API, asegurando que todas las solicitudes y respuestas fueran correctas.

- **GitHub Actions** se configuró para automatizar el proceso de integración continua, ejecutando pruebas y despliegues cada vez que se realizaba un push al repositorio.

- **Swagger** se usó para definir la arquitectura de la API, incluyendo los endpoints del microservicio. Esto proporcionó una documentación interactiva y permitió probar la API directamente desde la interfaz.

- **OpenAPI Generator** se empleó para generar el esqueleto del código de la API, lo que permitió comenzar rápidamente con una estructura base para los endpoints definidos en el archivo Swagger.

- El desarrollo se realizó en **Python**, utilizando el framework **Flask** para construir la API. Flask es ligero, fácil de usar y perfecto para construir microservicios.

- **Docker** se utilizó para crear contenedores tanto para la API como para la base de datos, permitiendo simular un entorno de despliegue real. Esto garantizó que la API funcionara correctamente tanto en desarrollo como en pruebas, aislando el entorno de ejecución.

- Se utilizó una **arquitectura modular**, separando el código en diferentes paquetes y clases. Esto permitió un orden claro y mantenible en el código. La separación en paquetes facilita el desarrollo y la extensión del sistema sin que otras partes se vean afectadas, favoreciendo la escalabilidad del proyecto.

- Se utilizaron las siguientes librerías:

    Flask-SQLAlchem: Para la integración con la base de datos PostgreSQL, gestionando las operaciones CRUD.

    Flask-CORS: Para habilitar el soporte de CORS, permitiendo que la API sea accesible desde diferentes dominios.


## Requisitos de la API
Python 3.5.2+

## Guía de Uso En el Directorio

### Despliegue en Directorio 

1. Instalación:
 * Asegúrate de tener Python 3.5.2 o superior instalado en tu máquina.

2. Configuración del entorno
 * Asegúrate de tener PostgreSQL corriendo y configurado en tu entorno local o usa un servicio en la nube .
 * Nombra tu base de datos como Usuarios
 * Para inicializar las tablas la base de datos y el contenido de esta, asegúrate de ejecutar las query definidas en el archivo Init.sql para crear las tablas y estructuras necesaria

3. Para ejecutar la Api Contenidos , ejecute lo siguiente desde el directorio raíz
 * Instale los requerimientos 
    ```
    pip3 install -r requirements.txt
    pip3 install -r requeriments_sqlalchemy.txt
    ```
 * Ejecute la Api con el siguiente Comando
    ```
    python3 -m openapi_server
    ```
 * La Api debe estarse  ejecutando 

4. Definición de OpenAPI

Abre tu navegador y accede a la siguiente URL para ver la interfaz de usuario de la API:
```
http://localhost:8080/ui/
```

La definición de OpenAPI está disponible en formato JSON en:
```
http://localhost:8080/openapi.json
```

## Despliegue en Docker 

Para desplegar la API en un contenedor Docker , Ejecute el siguiente comando 
```bash
# Construir e iniciar la imagen y el contenedor
docker-compose up --build


