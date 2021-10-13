-- Modelo
CREATE DATABASE cinemapp;
USE cinemapp;

CREATE TABLE usuario(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    correo VARCHAR(255) NOT NULL,
    contraseña VARCHAR(255) NOT NULL
);

CREATE TABLE pelicula(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    fecha_visto DATE NOT NULL,
    imagen VARCHAR(1024) NOT NULL,
    director VARCHAR(100) NOT NULL,
    año SMALLINT UNSIGNED NOT NULL,
    valoracion TINYINT,
    favorito BOOLEAN,
    reseña VARCHAR(5000),
    compartido BOOLEAN,
    usuarioId INT UNSIGNED NOT NULL,
    FOREIGN KEY (usuarioId) REFERENCES usuario(id)
);

CREATE TABLE personaje(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    actor_nombre VARCHAR(50) NOT NULL,
    actor_img VARCHAR(1024) NOT NULL,
    personaje_nombre VARCHAR(50) NOT NULL,
    personaje_img VARCHAR(1024) NOT NULL,
    peliculaId INT UNSIGNED NOT NULL,
    FOREIGN KEY (peliculaId) 
    REFERENCES pelicula(id)
);

CREATE TABLE comentario(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    texto VARCHAR(1000) NOT NULL,
    fecha_visto DATETIME NOT NULL,
    peliculaId INT UNSIGNED NOT NULL,
    usuarioId INT UNSIGNED NOT NULL,
    FOREIGN KEY (peliculaId) REFERENCES pelicula(id),    
    FOREIGN KEY (usuarioId) REFERENCES usuario(id)
);

-- Registros para mostrar
INSERT INTO usuario(correo, contraseña) VALUES 
('ivan@cinemapp.com', '2001SpaceOdyssey'),
('diana@cinemapp.com', 'EternalSunshine'),
('edson@cinemapp.com', 'DonnieDarko'),
('emmanuel@cinemapp.com', 'Interestellar'),
('andres@cinemapp.com', 'Inception1917');

-- Para crear el usuario que se conectará 
CREATE USER 'cinemapp_admin'@'localhost' IDENTIFIED BY 'Inception2001';

GRANT ALL PRIVILEGES ON cinemapp.* TO 'cinemapp_admin'@'localhost';

-- Consulta utilizada
SELECT * FROM usuario;