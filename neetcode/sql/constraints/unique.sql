
-- The "unique" constraint
-- sometimes, we want all vals in a col to be unique
-- we enforce this using the UNIQUE constraint
-- ex: col_name TYPE UNIQUE etc...
-- pseudo
-- name type UNIQUE ...;

CREATE TABLE students (

    id INTEGER UNIQUE NOT NULL,
    name TEXT NOT NULL,
    age INTEGER NOT NULL

);

-- Do not modify below this line --
SELECT 
    column_name, 
    is_nullable,
    column_default,
    CASE 
        WHEN column_name IN (
            SELECT column_name 
            FROM information_schema.table_constraints tc
            JOIN information_schema.constraint_column_usage ccu 
                ON tc.constraint_name = ccu.constraint_name
            WHERE tc.table_name = 'students' 
                AND tc.constraint_type IN ('UNIQUE')
        ) THEN 'YES'
        ELSE 'NO'
    END AS is_unique
FROM 
    information_schema.columns
WHERE 
    table_name = 'students';
