-- 1. Total de ventas por categoría
SELECT Category, 
       ROUND(SUM(Sales), 2) AS total_ventas
FROM ventas
GROUP BY Category
ORDER BY total_ventas DESC;

-- 2. Top 5 productos más vendidos
SELECT "Product Name", 
       ROUND(SUM(Sales), 2) AS total_ventas
FROM ventas
GROUP BY "Product Name"
ORDER BY total_ventas DESC
LIMIT 5;

-- 3. Ventas por región
SELECT Region, 
       ROUND(SUM(Sales), 2) AS total_ventas,
       COUNT(*) AS cantidad_ordenes
FROM ventas
GROUP BY Region
ORDER BY total_ventas DESC;

-- 4. Clientes con mayor gasto promedio
SELECT "Customer Name",
       ROUND(AVG(Sales), 2) AS ticket_promedio,
       COUNT(*) AS cantidad_compras
FROM ventas
GROUP BY "Customer Name"
ORDER BY ticket_promedio DESC
LIMIT 10;

-- 5. Top 10 ciudades con más ventas
SELECT City,
       ROUND(SUM(Sales), 2) AS total_ventas,
       COUNT(*) AS cantidad_ordenes
FROM ventas
GROUP BY City
ORDER BY total_ventas DESC
LIMIT 10;