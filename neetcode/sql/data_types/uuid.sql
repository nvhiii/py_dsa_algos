
-- UUID
-- aside using auto inc for unique identifiers, we can use UUID
-- uuid: universally unique identifiers
-- 16 byte val + random gen + guaranteed unique

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(), -- usually the uuid function is uuid_generate_v4()
    name TEXT
);


-- Do not modify below this line --
SELECT * FROM users;
