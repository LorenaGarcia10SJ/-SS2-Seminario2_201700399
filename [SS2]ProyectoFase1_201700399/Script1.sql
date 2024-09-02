CREATE DATABASE Fase1;
USE Fase1;
-- DROP TABLE TemporalCompra;
-- DROP TABLE TemporalVenta;


CREATE TABLE TemporalCompra
(
    Fecha DATE,
    CodProveedor VARCHAR(5),
    NombreProveedor VARCHAR(250),
    DireccionProveedor VARCHAR(250),
    NumeroProveedor VARCHAR(8),
    WebProveedor VARCHAR(100),
    CodProducto VARCHAR(50),
    NombreProducto VARCHAR(250),
    MarcaProducto VARCHAR(250),
    Categoria VARCHAR(100),
    SodSuSursal VARCHAR(50),
    NombreSucursal VARCHAR(250),
    DireccionSucursal VARCHAR(250),
    Region VARCHAR(100),
    Departamento VARCHAR(100),
    Unidades VARCHAR(10),
    CostoU DECIMAL(18, 2)
);

CREATE TABLE TemporalVenta (
    Fecha DATE,
    CodigoCliente VARCHAR(5),
    NombreCliente VARCHAR(250),
    TipoCliente VARCHAR(20),
    DireccionCliente VARCHAR(250),
    NumeroCliente VARCHAR(15), ------
    CodVendedor VARCHAR(10),
    NombreVendedor VARCHAR(250),
    Vacacionista INT, -----------------
    CodProducto VARCHAR(10),
    NombreProducto VARCHAR(250),
    MarcaProducto VARCHAR(250),
    Categoria VARCHAR(50), -------------
    SodSuSursal VARCHAR(10),
    NombreSucursal VARCHAR(250),
    DireccionSucursal VARCHAR(250),
    Region VARCHAR(50),
    Departamento VARCHAR(50), --------------
    Unidades VARCHAR(10),
    PrecioUnitario DECIMAL(18, 2)
);

SELECT * FROM TemporalCompra;
SELECT * FROM TemporalVenta;

-- Vacias las tablas temporales
DELETE FROM TemporalVenta;
DELETE FROM TemporalCompra;
------------------------------------------- DATA WAREHOUSE ----------------------------------------------------------------------
-- Dimension: Tiempo
CREATE TABLE DimTiempo(
	CodFecha INT IDENTITY(1,1) PRIMARY KEY,
    Fecha DATE
);


-- Dimension: Cliente
CREATE TABLE DimCliente(
	CodCliente INT IDENTITY(1,1) PRIMARY KEY,
	CodigoCliente VARCHAR(5),
    NombreCliente VARCHAR(250),
    TipoCliente VARCHAR(20),
    DireccionCliente VARCHAR(250),
    NumeroCliente VARCHAR(15),
);


-- Dimension: Vendedor
CREATE TABLE DimVendedor(
	CodigoVendedor INT IDENTITY(1,1) PRIMARY KEY,
	CodVendedor VARCHAR(10),
    NombreVendedor VARCHAR(250),
    Vacacionista INT
);

-- Dimension: Producto
CREATE TABLE DimProducto (
    CodigoProducto INT IDENTITY(1,1) PRIMARY KEY,
	CodProducto VARCHAR(10),
    NombreProducto VARCHAR(250),
    MarcaProducto VARCHAR(250),
    Categoria VARCHAR(50),
);

-- Dimension: Proveedor
CREATE TABLE DimProveedor (
    CodigoProveedor INT IDENTITY(1,1) PRIMARY KEY,
    CodProveedor VARCHAR(5),
    NombreProveedor VARCHAR(250),
    DireccionProveedor VARCHAR(250),
    NumeroProveedor VARCHAR(8),
    WebProveedor VARCHAR(100),
);

-- Dimension: Sucursal
CREATE TABLE DimSucursal (
    CodSucursal INT IDENTITY(1,1) PRIMARY KEY,
    SodSuSursal VARCHAR(10),
    NombreSucursal VARCHAR(250),
    DireccionSucursal VARCHAR(250),
    Region VARCHAR(50),
    Departamento VARCHAR(50)
);
-- Tabla de hechos para Ventas .........................................................................................
CREATE TABLE FactVentas(
	CodVenta INT IDENTITY(1,1) PRIMARY KEY,
    CodFecha INT,
	CodCliente INT,
	CodigoVendedor INT, 
    CodigoProducto INT,
	CodigoSucursal INT,
    Unidades INT,
    PrecioUnitario DECIMAL(10, 2),
	FOREIGN KEY (CodFecha) REFERENCES DimTiempo(CodFecha),
	FOREIGN KEY (CodCliente) REFERENCES DimCliente(CodCliente),
	FOREIGN KEY (CodigoVendedor) REFERENCES DimVendedor(CodigoVendedor),
	FOREIGN KEY (CodigoProducto) REFERENCES DimProducto(CodigoProducto),
	FOREIGN KEY (CodigoSucursal) REFERENCES DimSucursal(CodSucursal)
);



-- Tabla de hechos para Compras
CREATE TABLE Compras_Fact (
    Fecha DATE,
    CodProducto INT,
    CodProveedor INT,
    Unidades INT,
    CostoU DECIMAL(10, 2),
    Total DECIMAL(10, 2) AS (Unidades * CostoU) PERSISTED
);

