CREATE DATABASE IF NOT EXISTS jugadores_db;

USE jugadores_db;

CREATE TABLE jugadores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    extremo_izquierdo_def INT,
    segundo_izquierdo_51 INT,
    segundo_izquierdo_60 INT,
    central_def INT,
    avanzado INT,
    segundo_derecho_60 INT,
    segundo_derecho_51 INT,
    extremo_derecho_def INT,
    extremo_izquierdo INT,
    lateral_izquierdo INT,
    central_of INT,
    lateral_derecho INT,
    extremo_derecho_of INT,
    pivote INT,
    general FLOAT
);
