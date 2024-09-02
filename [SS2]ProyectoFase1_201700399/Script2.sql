
CREATE DATABASE FaseDB2;
USE FaseDB2;
-- DROP TABLE TemporalCompra2;
-- DROP TABLE TemporalVenta2;

CREATE TABLE TemporalCompra2
(
    Fecha DATE,
    CodProveedor VARCHAR(5),
    NombreProveedor VARCHAR(100),
    DireccionProveedor VARCHAR(200),
    NumeroProveedor VARCHAR(8),
    WebProveedor VARCHAR(100),
    CodProducto VARCHAR(50),
    NombreProducto VARCHAR(100),
    MarcaProducto VARCHAR(100),
    Categoria VARCHAR(100),
    SodSuSursal VARCHAR(50),
    NombreSucursal VARCHAR(200),
    DireccionSucursal VARCHAR(200),
    Region VARCHAR(100),
    Departamento VARCHAR(100),
    Unidades VARCHAR(10),
    CostoU DECIMAL(18, 2)
);

CREATE TABLE TemporalVenta2 (
    Fecha DATE,
    CodigoCliente VARCHAR(5),
    NombreCliente VARCHAR(100),
    TipoCliente VARCHAR(20),
    DireccionCliente VARCHAR(100),
    NumeroCliente VARCHAR(15),
    CodVendedor VARCHAR(10),
    NombreVendedor VARCHAR(100),
    Vacacionista INT,
    CodProducto VARCHAR(10),
    NombreProducto VARCHAR(100),
    MarcaProducto VARCHAR(50),
    Categoria VARCHAR(50),
    SodSuSursal VARCHAR(10),
    NombreSucursal VARCHAR(100),
    DireccionSucursal VARCHAR(100),
    Region VARCHAR(50),
    Departamento VARCHAR(50),
    Unidades VARCHAR(10),
    PrecioUnitario DECIMAL(18, 2)
);
SELECT * FROM TemporalCompra2;
SELECT * FROM TemporalVenta2;


-- Vacias las tablas temporales
TRUNCATE TABLE TemporalVenta2;
TRUNCATE TABLE TemporalCompra2;

