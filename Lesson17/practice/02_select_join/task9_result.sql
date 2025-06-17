-- Напишите запрос, который возвращает название цвета и общее количество продуктов, относящихся к этому цвету.
-- Включите в результат все цвета, даже если у них нет ни одного продукта.

SELECT
    Colors.name color_name,
    COUNT(Products.id) product_count
FROM
    Colors
JOIN
    Products ON Colors.id = Products.color_id
GROUP BY
    Colors.name;