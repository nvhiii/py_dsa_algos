-- inserting default values in tables
-- if you use INSERT INTO table (cols...) VALUES (cols...); then omit a specific col val, it auto is null.
-- primary keys CANNOT BE omitted

CREATE TABLE products (
  id INTEGER PRIMARY KEY,
  name TEXT,
  stock INTEGER DEFAULT 0
);

-- Do not modify above this line --

INSERT INTO products (id, name)
VALUES
(1, 'Apple'),
(2, 'Banana'),
(3, 'Orange');

-- Do not modify below this line --
SELECT * FROM products;
