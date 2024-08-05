-- Porcentaje de pasajeros por género.
SELECT Gender, 
       COUNT(*) * 100.0 / (SELECT COUNT(*) FROM dbo.Pasajeros) AS Porcentaje
FROM dbo.Pasajeros
GROUP BY Gender;
