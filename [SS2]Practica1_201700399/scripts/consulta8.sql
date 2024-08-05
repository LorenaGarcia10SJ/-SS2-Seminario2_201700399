SELECT TOP 5 
    a.AirportContinent, 
    COUNT(*) AS CantidadVisitantes
FROM dbo.Hechos h
JOIN dbo.Aeropuertos a ON h.AeropuertosID = a.AeropuertosID
GROUP BY a.AirportContinent
ORDER BY CantidadVisitantes DESC;