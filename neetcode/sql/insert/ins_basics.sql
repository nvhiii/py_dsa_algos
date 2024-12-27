-- Insert Into stmnt
-- we can only insert rows into a table after it has already been created!
-- pseudo:
-- INSERT INTO table (cols...)
-- VALUES (cols...),
-- (cols...);
-- it can be multiple rows, like above, etc.

CREATE TYPE account_type AS ENUM ('checking', 'savings', 'cd', 'money_market');

CREATE TABLE bank_accounts (
    id INTEGER PRIMARY KEY,
    account_type account_type,
    balance INTEGER
);

-- Do not modify above this line --

-- the params of the cols must be the vals specified in the create table stmt
-- the row vals are the ones we must adhere to the valid data types
INSERT INTO bank_accounts (id, account_type, balance)
    VALUES (1, 'checking', 1000),
    (2, 'savings', 2000),
    (3, 'cd', 3000),
    (4, 'money_market', 4000);

-- Do not modify below this line --
SELECT * FROM bank_accounts;
