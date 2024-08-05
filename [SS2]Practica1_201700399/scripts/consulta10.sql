SELECT 
    FORMAT(s.DepartureDate, 'MM-yyyy') AS MesAno,
    COUNT(*) AS CantidadVuelos
FROM dbo.Hechos h
JOIN dbo.SalidaFecha s ON h.SalidaId = s.SalidaId
GROUP BY FORMAT(s.DepartureDate, 'MM-yyyy')
ORDER BY MesAno;