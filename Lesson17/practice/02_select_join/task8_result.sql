-- Для всех продуктов без цвета, задайте цвет 'Black'
PRAGMA foreign_keys = ON;
UPDATE Products
SET color_id = 5
WHERE color_id IS NULL;