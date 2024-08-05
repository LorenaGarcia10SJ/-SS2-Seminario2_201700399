-- Crear base de datos
CREATE DATABASE ProcesoETL;
Go

-- Crear tabla de Dimensiones
-- Pasajeros
CREATE TABLE Pasajeros (
    PassengerID NVARCHAR(50) PRIMARY KEY,
    FirstName NVARCHAR(100),
    LastName NVARCHAR(100),
    Gender NVARCHAR(10),
    Age INT,
    Nationality NVARCHAR(100)
);
-- Aeropuerto
CREATE TABLE Aeropuertos (
    AeropuertoId INT IDENTITY(1,1) PRIMARY KEY,
	AirportCountryCode NVARCHAR(10),
    AirportName NVARCHAR(100),
    CountryName NVARCHAR(100),
    AirportContinent NVARCHAR(100),
    Continents NVARCHAR(100)
);
-- SalidaFecha

CREATE TABLE SalidaFecha (
	SalidaId INT IDENTITY(1,1) PRIMARY KEY,
    DepartureDate DATE
);
-- Piloto
CREATE TABLE Pilotos (
	PilotoId INT IDENTITY(1,1) PRIMARY KEY,
    PilotName NVARCHAR(100),
);

-- Crear tabla de Hechos(fact)
CREATE TABLE Hechos (
	HechosId INT IDENTITY(1,1) PRIMARY KEY,
	PassengerID NVARCHAR(50),
    AeropuertoId INT,
	SalidaId INT,
    PilotoId INT,
    ArrivalAirport NVARCHAR(100),
    FlightStatus NVARCHAR(50)
	FOREIGN KEY (PassengerID) REFERENCES Pasajeros(PassengerID),
    FOREIGN KEY (AeropuertoId) REFERENCES Aeropuertos(AeropuertoId),
    FOREIGN KEY (SalidaId) REFERENCES SalidaFecha(SalidaId),
    FOREIGN KEY (PilotoId) REFERENCES Pilotos(PilotoId)
);

Drop DATABASE ProcesoETL;