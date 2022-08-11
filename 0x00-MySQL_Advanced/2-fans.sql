-- LEARNING TO USE GROUP BY
-- DONT FORGET TO ORDER BY
SELECT origin, SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
