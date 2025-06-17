CREATE TABLE Colors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE Products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    color_id INTEGER,
    FOREIGN KEY (color_id) REFERENCES Colors(id)
);

PRAGMA foreign_keys = ON;

INSERT INTO Colors (name) VALUES
('Red'),
('Blue'),
('Green');


INSERT INTO Products (name, price, color_id) VALUES
('Smartphone S', 800.00, 1),
('Smartwatch W', 250.00, 1),
('Headphones P', 150.00, 2),
('Headphones D', 185.00, 3),
('SmarTV', 215.00, 1);