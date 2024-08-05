-- Top 5 aeropuertos con mayor número de pasajeros.
SELECT TOP 5 
    a.AirportName, 
    COUNT(*) AS NoPasajeros
FROM dbo.Hechos h
JOIN dbo.Aeropuertos a ON h.AeropuertosID = a.AeropuertosID
GROUP BY a.AirportName
ORDER BY NoPasajeros DESC;