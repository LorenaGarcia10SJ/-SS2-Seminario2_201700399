import pyodbc
import csv
from datetime import datetime
import os

def conexionBD():
    try:
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-VUS22HJ1;DATABASE=ProcesoETL;Trusted_Connection=yes;')
        return conn
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def borrarModelo():
    conn = conexionBD()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS Hechos, Pasajeros, Aeropuertos, SalidaFecha, Pilotos")
    conn.commit()
    #conn.close()
    print("Modelo borrado con éxito...")

def crearModelo():
    conn = conexionBD()
    cursor = conn.cursor()
    
    ScriptPractica1 = """
    use ProcesoETL;
    
    CREATE TABLE Pasajeros (
        PassengerID VARCHAR(50) PRIMARY KEY,
        FirstName NVARCHAR(100),
        LastName NVARCHAR(100),
        Gender NVARCHAR(10),
        Age INT,
        Nationality NVARCHAR(100)
    );
    
    CREATE TABLE Aeropuertos (
    AeropuertosID INT IDENTITY(1,1) PRIMARY KEY,
	AirportCountryCode NVARCHAR(10),
    AirportName NVARCHAR(100),
    CountryName NVARCHAR(100),
    AirportContinent NVARCHAR(100),
    Continents NVARCHAR(100)
    );
    
    CREATE TABLE SalidaFecha (
	SalidaId INT IDENTITY(1,1) PRIMARY KEY,
    DepartureDate DATE
    );
    
    CREATE TABLE Pilotos (
	PilotoId INT IDENTITY(1,1) PRIMARY KEY,
    PilotName NVARCHAR(100),
    );
    
    CREATE TABLE Hechos (
	HechosId INT IDENTITY(1,1) PRIMARY KEY,
	PassengerID VARCHAR(50),
    AeropuertosID INT,
	SalidaId INT,
    PilotoId INT,
    ArrivalAirport NVARCHAR(100),
    FlightStatus NVARCHAR(50)
	FOREIGN KEY (PassengerID) REFERENCES Pasajeros(PassengerID),
    FOREIGN KEY (AeropuertosID) REFERENCES Aeropuertos(AeropuertosID),
    FOREIGN KEY (SalidaId) REFERENCES SalidaFecha(SalidaId),
    FOREIGN KEY (PilotoId) REFERENCES Pilotos(PilotoId)
    );

    """
    
    cursor.execute(ScriptPractica1)
    conn.commit()
    #conn.close()
    print("Modelo creado con éxito...")

    ## C:\\Users\\logas\\Downloads\\data\\practica.csv
def extraerInformacion(ruta,conn):
    try:
        cursor = conn.cursor()
        
        tablaTemporal = """
        CREATE TABLE ##informacionTemporal (
            PassengerID VARCHAR(50),
            FirstName NVARCHAR(100),
            LastName NVARCHAR(100),
            Gender NVARCHAR(10),
            Age INT,
            Nationality NVARCHAR(100),
            AirportName NVARCHAR(100),
            AirportCountryCode NVARCHAR(50),
            CountryName NVARCHAR(100),
            AirportContinent NVARCHAR(100),
            Continents NVARCHAR(100),
            DepartureDate DATE,
            ArrivalAirport NVARCHAR(100),
            PilotName NVARCHAR(100),
            FlightStatus NVARCHAR(50)
        );
        """
        cursor.execute(tablaTemporal)
        conn.commit()

        bulkQuery = f"""
        BULK INSERT ##informacionTemporal
        FROM '{ruta}'
        WITH (
            FIELDTERMINATOR = ';',
            ROWTERMINATOR = '\\n',
            FIRSTROW = 2,
            TABLOCK
        );
        """
        cursor.execute(bulkQuery)
        conn.commit()
        print(f"Información extraída de {ruta} exitosamente...")
        
    except Exception as e:
        print(f"Ocurrió un error al extraer la información: {e}")


def cargarInformacion(conn):
    try:
        cursor = conn.cursor()

        # PassengerID | FirstName | LastName | Gender | Age | Nationality
        insertPasajeros = """
        MERGE INTO Pasajeros AS target
        USING (
            SELECT DISTINCT PassengerID, FirstName, LastName, Gender, Age, Nationality
            FROM ##informacionTemporal
        ) AS source ON target.PassengerID = source.PassengerID
        WHEN NOT MATCHED THEN
        INSERT (PassengerID, FirstName, LastName, Gender, Age, Nationality)
        VALUES (source.PassengerID, source.FirstName, source.LastName, source.Gender, source.Age, source.Nationality);
        
        """
        cursor.execute(insertPasajeros)
        conn.commit()

        # AirportCountryCode | AirportName  | CountryName | AirportContinent | Continents
        insertAeropuertos = """
        INSERT INTO Aeropuertos (AirportCountryCode, AirportName, CountryName, AirportContinent, Continents)
        SELECT DISTINCT AirportCountryCode, AirportName, CountryName, AirportContinent, Continents
        FROM ##informacionTemporal;
        """
        cursor.execute(insertAeropuertos)
        conn.commit()
        
        insertSalidaFecha = """
        INSERT INTO SalidaFecha (DepartureDate)
        SELECT DISTINCT DepartureDate
        FROM ##informacionTemporal;
        """
        
        cursor.execute(insertSalidaFecha)
        conn.commit()
        
        insertPilotos = """
        INSERT INTO Pilotos (PilotName)
        SELECT DISTINCT PilotName
        FROM ##informacionTemporal;
        """
        
        cursor.execute(insertPilotos)
        conn.commit()
        
        # PassengerID | AeropuertoId | SalidaId  | PilotoId | ArrivalAirport | FlightStatus
        insertHechos = """
        INSERT INTO Hechos (PassengerID, AeropuertosID, SalidaId, PilotoId, ArrivalAirport, FlightStatus)
        SELECT 
            it.PassengerID,
            a.AeropuertosID,
            s.SalidaId,
            p.PilotoId,
            it.ArrivalAirport,
            it.FlightStatus
        FROM ##informacionTemporal it
        JOIN Pasajeros pa ON it.PassengerID = pa.PassengerID
        JOIN Aeropuertos a ON it.AirportCountryCode = a.AirportCountryCode AND it.AirportName = a.AirportName
        JOIN SalidaFecha s ON it.DepartureDate = s.DepartureDate
        JOIN Pilotos p ON it.PilotName = p.PilotName;
        """
        
        cursor.execute(insertHechos)
        conn.commit()
        
        print("Información cargada exitosamente...")
        
    except Exception as e:
        print(f"Ocurrió un error al cargar la información: {e}")
        