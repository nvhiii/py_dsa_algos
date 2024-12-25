
-- primary key
-- special column within a table
-- MUST be unique for each row + cannot be NULL
-- ONLY 1 primary key in table
-- usually specified using keywords PRIMARY KEY

-- good practice to have a primary key in every table
-- usually use id as primary key
-- good way to connect tables together and make correlations + relationshisp between tables
-- pseudo
-- name type PRIMARY KEY;


CREATE TABLE users (

    id INTEGER PRIMARY KEY, -- no need for unique + not null constraint, since implied
    username TEXT

);

CREATE TABLE videos (

    id INTEGER PRIMARY KEY,
    title TEXT,
    owner_id INTEGER

);

-- Do not modify below this line --
SELECT 
    c.table_name,
    c.column_name, 
    c.data_type, 
    CASE 
        WHEN kcu.column_name IS NOT NULL THEN 'YES'
        ELSE 'NO'
    END AS is_primary_key
FROM 
    information_schema.columns c
LEFT JOIN 
    information_schema.key_column_usage kcu
    ON c.table_name = kcu.table_name 
    AND c.column_name = kcu.column_name
LEFT JOIN 
    information_schema.table_constraints tc
    ON kcu.constraint_name = tc.constraint_name
    AND tc.constraint_type = 'PRIMARY KEY'
WHERE 
    c.table_name IN ('users', 'videos')
ORDER BY 
    c.table_name,
    c.ordinal_position;
