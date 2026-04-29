DROP DATABASE IF EXISTS gestor_de_tareas;
CREATE DATABASE gestor_de_tareas;
USE gestor_de_tareas;

-- =========================
-- ESTADOS
-- =========================
CREATE TABLE estados (
    id_estado INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nombre VARCHAR(50) NOT NULL
);

-- =========================
-- CATEGORIAS
-- =========================
CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

-- =========================
-- TAREAS
-- =========================
CREATE TABLE tareas (
    id_tarea INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,

    activa TINYINT(1) DEFAULT 1,

    id_estado INT NOT NULL,
    id_categoria INT NOT NULL,

    FOREIGN KEY (id_estado) REFERENCES estados(id_estado),
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

-- =========================
-- REPETICIONES
-- =========================
CREATE TABLE repeticiones (
    id_repeticion INT AUTO_INCREMENT PRIMARY KEY,
    id_tarea INT NOT NULL,

    tipo ENUM('diaria', 'semanal', 'mensual') NOT NULL,
    intervalo INT NOT NULL DEFAULT 1,

    fecha_base DATE NOT NULL,
    fecha_fin DATE NULL,

    solo_laborales TINYINT(1) DEFAULT 0,

    FOREIGN KEY (id_tarea) REFERENCES tareas(id_tarea) ON DELETE CASCADE
);

-- =========================
-- DIAS REPETICION
-- =========================
CREATE TABLE dias_repeticion (
    id_dia_rep INT AUTO_INCREMENT PRIMARY KEY,
    id_repeticion INT NOT NULL,

    tipo_dia ENUM('semana', 'mes') NOT NULL,
    valor INT,
    orden_semana INT,
    hora TIME,

    -- evitar duplicados
    UNIQUE (id_repeticion, tipo_dia, valor, orden_semana, hora),

    FOREIGN KEY (id_repeticion) REFERENCES repeticiones(id_repeticion) ON DELETE CASCADE,

    -- validaciones básicas
    CHECK (
        (tipo_dia = 'semana' AND valor BETWEEN 1 AND 7 AND orden_semana IS NULL)
        OR
        (tipo_dia = 'mes' AND valor BETWEEN 1 AND 31)
    )
);

-- =========================
-- EVENTOS
-- =========================
CREATE TABLE eventos_tarea (
    id_evento INT AUTO_INCREMENT PRIMARY KEY,
    id_tarea INT NOT NULL,

    fecha DATE NOT NULL,
    hora TIME,

    FOREIGN KEY (id_tarea) REFERENCES tareas(id_tarea) ON DELETE CASCADE,

    -- permitir múltiples fechas por tarea pero no duplicar el mismo día
    UNIQUE (id_tarea, fecha)
);

-- =========================
-- INDICES
-- =========================
CREATE INDEX idx_fecha_evento 
ON eventos_tarea(fecha);

CREATE INDEX idx_tarea_evento 
ON eventos_tarea(id_tarea);

CREATE INDEX idx_tarea_estado 
ON tareas(id_estado);

CREATE INDEX idx_tarea_categoria 
ON tareas(id_categoria);