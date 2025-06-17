-- Напишите запрос, который возвращает название продукта,
-- цену продукта и название соответствующего цвета для всех товаров, у которых есть назначенный цвет.

SELECT Products.name, Products.price, Colors.name
FROM Products
INNER JOIN Colors ON Products.color_id = Colors.id;