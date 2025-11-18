

-- Usar la base de datos
USE prueba_api;

CREATE TABLE IF NOT EXISTS Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(80) NOT NULL,
    email VARCHAR(80) NOT NULL UNIQUE,
    telefono BIGINT UNIQUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_nombre (nombre)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS Direccion(
    id INT AUTO_INCREMENT PRIMARY KEY,
    calle VARCHAR(255) NOT NULL,
    numero_calle INT NOT NULL,
    pais VARCHAR(100) NOT NULL,
    ciudad VARCHAR(100) NOT NULL,
    codigo_postal VARCHAR(10),
    latitud FLOAT,
    longitud FLOAT,
    INDEX idx_codigo_postal (codigo_postal)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS Warehouse(
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_direccion INT NOT NULL,
    FOREIGN KEY (id_direccion) REFERENCES Direccion(id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS Cotizaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_direccion_destino INT NOT NULL,
    id_direccion_origen INT NOT NULL,
    distancia_km INT NOT NULL,
    cantidad_items INT NOT NULL,
    peso_kg FLOAT NOT NULL,
    costo_estimado FLOAT NOT NULL,
    volumen_unidad FLOAT NOT NULL,
    prioridad INT NOT NULL,
    fecha_solicitud TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_direccion_destino) REFERENCES Direccion(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_direccion_origen) REFERENCES Warehouse(id) ON DELETE CASCADE ON UPDATE CASCADE,
    INDEX idx_usuario (id_usuario)
    );

CREATE TABLE IF NOT EXISTS Tarifario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo_postal VARCHAR(10) NOT NULL UNIQUE,
    tarifa_base FLOAT NOT NULL,
    tarifa_kg_adicional FLOAT NOT NULL,
    tarifa_volumen_adicional FLOAT,
    zona_geografica VARCHAR(50)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS TipoEnvio(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(10) NOT NULL UNIQUE,
    coeficiente FLOAT NOT NULL,
    descripcion VARCHAR(256)
);
INSERT INTO TipoEnvio (nombre, coeficiente, descripcion) 
VALUES ('Normal', 1.0, 'Entrega estándar en 5-7 días hábiles');

INSERT INTO TipoEnvio (nombre, coeficiente, descripcion) 
VALUES ('Urgente', 1.5, 'Entrega prioritaria en 2-3 días hábiles');

INSERT INTO TipoEnvio (nombre, coeficiente, descripcion) 
VALUES ('Express', 2.0, 'Entrega express en 24 horas');

CREATE TABLE IF NOT EXISTS EstadoEnvio(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    descripcion VARCHAR(256)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO EstadoEnvio (nombre, descripcion) 
VALUES ('Pendiente', 'El envío ha sido registrado pero aún no se ha procesado');

INSERT INTO EstadoEnvio (nombre, descripcion) 
VALUES ('En tránsito', 'El envío está en camino hacia su destino');

INSERT INTO EstadoEnvio (nombre, descripcion) 
VALUES ('Entregado', 'El envío ha sido entregado al destinatario');

INSERT INTO EstadoEnvio (nombre, descripcion) 
VALUES ('Cancelado', 'El envío ha sido cancelado');

CREATE TABLE IF NOT EXISTS Envio(
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo_postal VARCHAR(10) NOT NULL,
    id_tipo_envio INT NOT NULL,
    direccion_destino VARCHAR(500) NOT NULL,
    localidad VARCHAR(100) NOT NULL,
    provincia VARCHAR(100) NOT NULL,
    pais VARCHAR(100) DEFAULT 'Argentina',
    peso_kg FLOAT NOT NULL,
    volumen_unidad FLOAT NOT NULL,
    id_estado_envio INT DEFAULT 1,
    nombre_receptor VARCHAR(255) NOT NULL,
    dni_receptor VARCHAR(20) NOT NULL,
    costo_total FLOAT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (id_tipo_envio) REFERENCES TipoEnvio(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (id_estado_envio) REFERENCES EstadoEnvio(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    INDEX idx_codigo_postal (codigo_postal),
    INDEX idx_estado_envio (id_estado_envio),
    INDEX idx_dni_receptor (dni_receptor)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

Select * from TipoEnvio;
Select * from EstadoEnvio;


    Select * from direccion;
    Select * from Usuarios;
    Select * from Warehouse;
    Select * from cotizaciones;
    Select * from tarifario;
	Select * from Envio;
    

    
    
    
    
    