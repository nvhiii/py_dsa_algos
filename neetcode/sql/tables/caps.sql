-- keywords arent case sensitive, but keep them caps for best practice!
-- keep user defined names all lowercase!

CREATE TABLE users (
  name TEXT
);

-- Do not modify below this line --
SELECT table_name, column_name, data_type
FROM information_schema.columns
WHERE table_name = 'users';
