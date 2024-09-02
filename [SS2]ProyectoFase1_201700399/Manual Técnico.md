<span style="color:#00FF00; font-size:20px;">  Universidad de San Carlos de Guatemala <br> Facultad de Ingenieria <br> Escuela en Ciencias y Sistemas <br> Seminario de Sistemas 2 <br> Sección A </span>

# Práctica 1

## Objetivos
Generales
1. Aprender el proceso de ETL
2. Brindar resultados con la información obtenida

Específicos
- Utilizar el lenguaje Python para el procesamiento de información.
- Limpiar Datos.
- Utilizar SQL Server para la creación de un Datawarehouse.
  
## Software
- SQL Server Management
- Visual studio Code, python

# Modelo de Estrella
De los datos proporcionados del archivo .csv se observo que se puede divir la información de la siguiente manera:
<br>
PassengerID;FirstName;LastName;Gender;Age;Nationality  
AirportName;AirportCountryCode;CountryName;AirportContinent;Continents  
DepartureDate  
ArrivalAirport  
PilotName  
FlightStatus  
<br>
Observando y analizando lo anterior se procedio a estructurar los datos en un modelo de estrella por la simplicidad y claridad del modelo que incluye una tabla de hechos central y varias tablas de dimensiones. Este modelo facilita las consultas y el análisis de datos.
<br>

![](Imagen/1.png) <br>

![](Imagen/2.png) <br>


# Tabla Hechos(fact)

Contiene los datos principales que se desean analizar, como las transacciones o eventos, en este caso tomamos una base de lo que se desea consultar. En este caso la tabla de hecho incluye la siguiente informacion sobre los vuelos: <br>
<br>
- HechoID
- PassengerID
- AeropuertosID
- SalidaId
- PilotoId
- ArrivalAirport
- FlightStatus.
<br>

La metrica de ArrivalAirport y FlightStatus la estamos tomando en la tabla de hecho como un dato sin la necesidad de relacionar con otros atributos.

# Dimensiones

Proporcionan el contexto para los datos de la tabla de hechos. Las dimensiones contienen atributos descriptivos que permiten categorizar y filtrar los datos en la tabla de hechos. <br> 
Las dimensiones que se tomaron en cuentas son las sigueintes: <br>

### D1: Pasajeros 
PassengerID (llave subrogada) <br>
FirstName<br>
LastName<br>
Gender<br>
Age<br>
Nationality<br>
<br>

### D2: Aeropuertos <br>
AeropuertosID (llave subrogada)<br>
AirportName<br>
AirportCountryCode<br>
CountryName<br>
AirportContinent<br>
Continents<br>

### D3: SalidaFecha<br> 
SalidaId (llave subrogada)<br>
DepartureDate<br>

### D4: Pilotos <br>
PilotoId (llave subrogada)<br>
PilotName<br>