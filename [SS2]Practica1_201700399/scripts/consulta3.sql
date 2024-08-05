SELECT 
    Nationality, 
    FORMAT(DepartureDate, 'MM-yyyy') AS MesAno,
    COUNT(*) AS Cantidad
FROM dbo.Pasajeros p
JOIN dbo.Hechos h ON p.PassengerID = h.PassengerID
JOIN dbo.SalidaFecha s ON h.SalidaId = s.SalidaId
GROUP BY Nationality, FORMAT(DepartureDate, 'MM-yyyy')
ORDER BY Nationality, MesAno;