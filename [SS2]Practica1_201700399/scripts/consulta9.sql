SELECT TOP 5 
    p.Gender, 
    p.Age, 
    COUNT(*) AS CantidadPasajeros
FROM dbo.Pasajeros p
JOIN dbo.Hechos h ON p.PassengerID = h.PassengerID
GROUP BY p.Gender, p.Age
ORDER BY CantidadPasajeros DESC;