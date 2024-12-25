-- relational dbs stored in dbs, hence named relational -> the relations between tables makes up
-- the table in itself

-- tables have basically class def, with cols initialized as absolute beginner stuff

-- below is a schema

CREATE TABLE videos (

    id INTEGER,
    name TEXT,
    created_at DATE,
    published BOOL

);

-- Do not modify below this line --
SELECT table_name, column_name, data_type
FROM information_schema.columns
WHERE table_name = 'videos';
