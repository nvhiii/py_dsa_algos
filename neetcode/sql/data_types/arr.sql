
-- arrays
-- we use them like so:
-- pseudo:
-- col type[] -> the square brackets indicate the arr
-- when we do the following:
-- INSERT INTO table (cols...) VALUES (cols... ARRAY[]) -> we use ARRAY syntax, not the data type itself!
-- usually dont use arrays in db, just normalize data into separate tables tbh

CREATE TABLE orders (

    id INTEGER PRIMARY KEY,
    items TEXT[],
    total_price INTEGER

);

-- Do not modify below this line --
INSERT INTO orders (id, items, total_price) 
    VALUES (1, ARRAY['apple', 'banana'], 100),
          (2, ARRAY['orange', 'grape'], 200),
          (3, ARRAY['watermelon', 'pineapple'], 300);

SELECT * FROM orders;
