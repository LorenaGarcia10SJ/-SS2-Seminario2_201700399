
CREATE DATABASE FaseDB2;
USE FaseDB2;
-- DROP TABLE TemporalCompra2;
-- DROP TABLE TemporalVenta2;

CREATE TABLE TemporalCompra2
(
    Fecha DATE,
    CodProveedor VARCHAR(5),
    NombreProveedor VARCHAR(200),
    DireccionProveedor VARCHAR(200),
    NumeroProveedor VARCHAR(200),
    WebProveedor VARCHAR(200),
    CodProducto VARCHAR(50),
    NombreProducto VARCHAR(200),
    MarcaProducto VARCHAR(200),
    Categoria VARCHAR(200),
    SodSuSursal VARCHAR(50),
    NombreSucursal VARCHAR(200),
    DireccionSucursal VARCHAR(200),
    Region VARCHAR(200),
    Departamento VARCHAR(200),
    Unidades VARCHAR(200),
    CostoU DECIMAL(18, 2)
);

CREATE TABLE TemporalVenta2 (
    Fecha DATE,
    CodigoCliente VARCHAR(5),
    NombreCliente VARCHAR(200),
    TipoCliente VARCHAR(200),
    DireccionCliente VARCHAR(200),
    NumeroCliente VARCHAR(200),
    CodVendedor VARCHAR(50),
    NombreVendedor VARCHAR(200),
    Vacacionista INT,
    CodProducto VARCHAR(50),
    NombreProducto VARCHAR(200),
    MarcaProducto VARCHAR(200),
    Categoria VARCHAR(200),
    SodSuSursal VARCHAR(50),
    NombreSucursal VARCHAR(200),
    DireccionSucursal VARCHAR(200),
    Region VARCHAR(200),
    Departamento VARCHAR(200),
    Unidades VARCHAR(200),
    PrecioUnitario DECIMAL(18, 2)
);
SELECT * FROM TemporalCompra2;
SELECT * FROM TemporalVenta2;


-- Vacias las tablas temporales
TRUNCATE TABLE TemporalVenta2;
TRUNCATE TABLE TemporalCompra2;

