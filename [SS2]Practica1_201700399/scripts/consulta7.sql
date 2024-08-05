SELECT TOP 5 
    a.CountryName, 
    COUNT(*) AS CantidadVisitantes
FROM dbo.Hechos h
JOIN dbo.Aeropuertos a ON h.AeropuertosID = a.AeropuertosID
GROUP BY a.CountryName
ORDER BY CantidadVisitantes DESC;