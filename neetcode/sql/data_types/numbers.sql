
-- numbers
-- several numerical reps in postgres

-- ints
-- SMALLINT -> 2 byte signed int, 16 bit num in 0s and 1s since base 2 rep
-- INTEGER -> 4 byte signed int, 32 bit num " "
-- BIGINT -> 8 byte signed int, 64 bit num " "

-- floats
-- FLOAT -> 4 byte floating-point num
-- DOUBLE PRECISION -> 8 byte floating point num, bigger float rep
-- DECIMAL -> stores fixed point number, precision must be specifed
-- ex: col DECIMAL(10, 2) -> 10 = digits total, up to 2 digits to the right of decimal
-- in this example, the total num of digits in this num may be 10, but keep in mind 2 of those spots MUST be for the decimals, so 8 nums at MOST to the left!
-- NUMERIC -> Same thing as DECIMAL

CREATE TABLE bank_accounts (

    id BIGINT PRIMARY KEY, -- this is 8 byte num
    balance NUMERIC(20, 2),
    interest_rate NUMERIC(5, 2),
    number_of_owners SMALLINT

);

-- Do not modify below this line --
INSERT INTO bank_accounts (id, balance, interest_rate, number_of_owners) VALUES
    (1, 123451234512345123.45, 123.45, 1);

SELECT 
    ba.*,
    (SELECT STRING_AGG(column_name || ' ' || data_type || CASE WHEN numeric_precision IS NOT NULL THEN '(' || numeric_precision || ',' || numeric_scale || ')' ELSE '' END, ', ')
     FROM information_schema.columns 
     WHERE table_name = 'bank_accounts') AS column_types
FROM 
    bank_accounts ba;
