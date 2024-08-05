-- Count divido por estado de vuelo
SELECT 
    FlightStatus, 
    COUNT(*) AS CantidadVuelos
FROM dbo.Hechos
GROUP BY FlightStatus
ORDER BY CantidadVuelos DESC;