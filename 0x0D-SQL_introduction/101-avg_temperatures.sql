-- Displays the average temperature of cities in desending ordered based on temperature.
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
