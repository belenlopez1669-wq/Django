-- 1. Tabla de Docentes
CREATE TABLE DOCENTES (
    id INT PRIMARY KEY AUTO_INCREMENT, -- Agregamos AUTO_INCREMENT para que se genere solo
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    id_de_docente VARCHAR(20) NOT NULL UNIQUE, -- UNIQUE evita que se repita el legajo/ID
    telefono VARCHAR(20) NULL,                 -- Opcional (admite valores NULL)
    correo VARCHAR(50) NOT NULL 
);

-- 2. Tabla de Materias
CREATE TABLE MATERIAS (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_de_la_materia VARCHAR(50) NOT NULL,
    id_de_la_materia VARCHAR(20) NOT NULL UNIQUE
);

-- 3. Tabla Intermedia: DICTA (Aquí es donde se unen)
CREATE TABLE DICTA (
    id_docente INT,
    id_materia INT,
    PRIMARY KEY (id_docente, id_materia), -- Evita que se repita exactamente la misma asignación
    FOREIGN KEY (id_docente) REFERENCES DOCENTES(id) ON DELETE CASCADE,
    FOREIGN KEY (id_materia) REFERENCES MATERIAS(id) ON DELETE CASCADE
);