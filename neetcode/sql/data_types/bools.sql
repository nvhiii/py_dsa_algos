
-- bools
-- type of data type, can only be truthy or falsy
-- some valid examples of true: TRUE, true, 't', 'y', 'YES', 'on', '1'
-- valid examples of false: FALSE, false, 'f', 'n', 'NO', 'off', '0'

CREATE TABLE three_column_table (

    id INTEGER PRIMARY KEY,
    is_active BOOLEAN,
    is_admin BOOLEAN

);

-- Do not modify below this line --
INSERT INTO three_column_table (id, is_active, is_admin) 
  VALUES (1, TRUE, FALSE),
         (2, true, false),
         (3, 't', 'f'),
         (4, 'y', 'n'),
         (5, 'yes', 'no'),
         (6, 'on', 'off'),
         (7, '1', '0');

SELECT * FROM three_column_table;
