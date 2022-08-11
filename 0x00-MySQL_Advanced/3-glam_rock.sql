-- LEARNING TO USE GROUP BY
-- DONT FORGETORDER BY
SELECT band_name, (IFNULL(split, 2022)-formed) AS lifespan FROM holberton.metal_bands WHERE style LIKE '%Glam Rock%' ORDER BY lifespan DESC;
