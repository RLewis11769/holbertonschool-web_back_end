-- List all bands with Glam Rock style by length of longevity
-- Longevity calculated as split - formed (if null give default value of 2021)
SELECT band_name, (IFNULL(split, 2020) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
