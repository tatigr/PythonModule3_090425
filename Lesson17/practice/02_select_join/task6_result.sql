-- Напишите запрос, который возвращает название продукта,
-- цену и название цвета для всех продуктов, в названии которых встречается подстрока "Pro"

SELECT Products.name, Products.price, Colors.name
FROM Products
INNER JOIN Colors ON Products.color_id = Colors.id
WHERE Products.name LIKE lower('%Pro%');