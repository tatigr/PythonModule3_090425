-- Напишите запрос, который показывает название продукта, цену и название цвета для всех товаров, чья цена превышает 100.00.

SELECT Products.name, Products.price, Colors.name
FROM Products
INNER JOIN Colors ON Products.color_id = Colors.id
WHERE Products.price > 100;