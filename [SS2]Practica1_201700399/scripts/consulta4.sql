SELECT 
    a.CountryName, 
    COUNT(*) AS CantidadVuelos
FROM dbo.Hechos h
JOIN dbo.Aeropuertos a ON h.AeropuertosID = a.AeropuertosID
GROUP BY a.CountryName
ORDER BY CantidadVuelos DESC;