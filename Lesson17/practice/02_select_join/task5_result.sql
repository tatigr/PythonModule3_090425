-- Напишите запрос, который возвращает название продукта,
-- цену и название цвета для всех продуктов, цвет которых не является 'Red'.

SELECT Products.name, Products.price, Colors.name
FROM Products
LEFT JOIN Colors ON Products.color_id = Colors.id
WHERE Colors.name <> 'Red' OR Colors.name IS NULL;