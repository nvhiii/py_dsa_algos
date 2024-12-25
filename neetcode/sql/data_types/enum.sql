
-- ENUM
-- data type that restricts col to a set of predefined vals
-- typically, do this so we dont have to keep repeating constraints across multiple tables
-- easier to just specify the enum var instead!
-- how we define this ENUM set:
-- CREATE TYPE status AS ENUM ('val', 'val1', 'val2');
-- how we use it in a table:
-- col status (status was the enum created and we implementing here!)

CREATE TYPE account_type AS ENUM ('checking', 'savings', 'cd', 'money_market');

CREATE TABLE bank_accounts (

    id INTEGER PRIMARY KEY,
    account_type account_type,
    balance INTEGER

);

-- Do not modify below this line --
INSERT INTO bank_accounts (id, account_type, balance) VALUES 
  (1, 'checking', 1000),
  (2, 'savings', 2000),
  (3, 'cd', 3000),
  (4, 'money_market', 4000);

SELECT 
    ba.*,
    (SELECT STRING_AGG(column_name || ' ' || data_type, ', ')
     FROM information_schema.columns 
     WHERE table_name = 'bank_accounts') AS column_types
FROM 
    bank_accounts ba;
