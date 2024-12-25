-- altering table demo
-- use the keywords ALTER TABLE to modify table (add, modify, or drop / delete cols)
-- pseudo:
-- ALTER TABLE {table name} ADD COLUMN {col} INTEGER;
-- ALTER TABLE {table name} RENAME COLUMN {col} TO {new name};
-- ALTER TABLE {table name} DROP COLUMN {col};


-- so, use alter table to alter
-- ADD COLUMN (col + data type)
-- RENAME COLUMN (col to new_name)
-- DROP COLUMN (col)

CREATE TABLE books (
  id INTEGER,
  title TEXT,
  author TEXT
);
-- Do not modify above this line --

ALTER TABLE books ADD COLUMN published_year INTEGER;
ALTER TABLE books RENAME COLUMN id TO isbn;
ALTER TABLE books DROP COLUMN author;

-- Do not modify below this line --
SELECT column_name, data_type, column_default
FROM information_schema.columns
WHERE table_name = 'books'
ORDER BY column_name;
