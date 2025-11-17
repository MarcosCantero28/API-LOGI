

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
    latitud FLOAT,
    longitud FLOAT
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
    
    Select * from direccion;
    
    Select * from Usuarios;
    
    Select * from Warehouse;
    
    Select * from cotizaciones;
    
    
    