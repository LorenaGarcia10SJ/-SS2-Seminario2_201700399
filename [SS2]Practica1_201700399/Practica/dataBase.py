import pyodbc
import csv
from datetime import datetime

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
	AirportCountryCode NVARCHAR(10) PRIMARY KEY,
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
    AirportCountryCode NVARCHAR(10),
	SalidaId INT,
    PilotoId INT,
    ArrivalAirport NVARCHAR(100),
    FlightStatus NVARCHAR(50)
	FOREIGN KEY (PassengerID) REFERENCES Pasajeros(PassengerID),
    FOREIGN KEY (AirportCountryCode) REFERENCES Aeropuertos(AirportCountryCode),
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
        MERGE INTO Aeropuertos AS target
        USING (
            SELECT DISTINCT AirportCountryCode, AirportName, CountryName, AirportContinent, Continents
            FROM ##informacionTemporal
        ) AS source ON target.AirportCountryCode = source.AirportCountryCode
        WHEN NOT MATCHED THEN
        INSERT (AirportCountryCode, AirportName, CountryName, AirportContinent, Continents)
        VALUES (source.AirportCountryCode, source.AirportName, source.CountryName, source.AirportContinent, source.Continents);
        
        """
        cursor.execute(insertAeropuertos)
        conn.commit()

        # DepartureDate
        insertSalidaFecha = """
        INSERT INTO SalidaFecha (DepartureDate)
        SELECT DISTINCT DepartureDate
        FROM ##informacionTemporal
        WHERE DepartureDate NOT IN (SELECT DepartureDate FROM SalidaFecha);
        """
        cursor.execute(insertSalidaFecha)
        conn.commit()
        
        # PilotName
        insertPilotos = """
        INSERT INTO Pilotos (PilotName)
        SELECT DISTINCT PilotName
        FROM ##informacionTemporal
        WHERE PilotName NOT IN (SELECT PilotName FROM Pilotos);
        """
        cursor.execute(insertPilotos)
        conn.commit()
        
        # HechosId | PassengerID | AirportCountryCode | SalidaId | PilotoId | ArrivalAirport | FlightStatus
        insertHechos = """
        INSERT INTO Hechos (PassengerID, AirportCountryCode, SalidaId, PilotoId, ArrivalAirport, FlightStatus)
        SELECT 
            t.PassengerID,
            t.AirportCountryCode,
            s.SalidaId,
            p.PilotoId,
            t.ArrivalAirport,
            t.FlightStatus
        FROM ##informacionTemporal t
        JOIN SalidaFecha s ON t.DepartureDate = s.DepartureDate
        JOIN Pilotos p ON t.PilotName = p.PilotName
        WHERE NOT EXISTS (
            SELECT 1 FROM Hechos h
            WHERE h.PassengerID = t.PassengerID
            AND h.AirportCountryCode = t.AirportCountryCode
            AND h.SalidaId = s.SalidaId
            AND h.PilotoId = p.PilotoId
            AND h.ArrivalAirport = t.ArrivalAirport
            AND h.FlightStatus = t.FlightStatus
        );
        """
        cursor.execute(insertHechos)
        conn.commit()
        
        print("Información cargada exitosamente...")
        
    except Exception as e:
        print(f"Ocurrió un error al cargar la información: {e}")
        
    