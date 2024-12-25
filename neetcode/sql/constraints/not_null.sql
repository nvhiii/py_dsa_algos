
-- Not Null demo
-- sometimes we want to enforce a col to have a val
-- so use name type NOT NULL, etc
-- we can have default val + not null as well in same col instantiation
-- the order of the above 2 dont matter!
-- not null is a type of many constraints!
-- a string is represented in sql using single paren
-- pseudo
-- name type NOT NULL;


CREATE TABLE products (

    name TEXT NOT NULL DEFAULT 'Unknown',
    price INTEGER NOT NULL,
    quantity INTEGER DEFAULT 0

);

-- Do not modify below this line --
SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'products';
