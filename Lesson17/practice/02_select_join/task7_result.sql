-- Напишите запрос, который выводит название и цену всех продуктов,
-- у которых не указан цвет (т.е., color_id равен NULL).

SELECT name, price
FROM Products
WHERE color_id IS NULL;