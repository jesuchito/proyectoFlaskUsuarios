-- Creación de la tabla "usuarios"
CREATE TABLE usuarios (
    idUsuario SERIAL PRIMARY KEY,  -- SERIAL para auto-incremento automático
    nombre VARCHAR(255) NOT NULL,
    rol VARCHAR(30) CHECK (rol IN ('administrador', 'cliente')),
    imagen TEXT,
    contenidosFavoritos INTEGER[]
);


--Insert Usuarios
INSERT INTO usuarios VALUES (1,'Maria','administrador','administrador.jpg',ARRAY[1, 2, 5]);
INSERT INTO usuarios VALUES (2,'Luis','cliente','user2.jpg',ARRAY[2, 3]);