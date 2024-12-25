
-- AUTO INCREMENT
-- since we sometimes may want to assign unique identifiers 
-- in each row, we can auto increment in multiple ways
-- SERIAL -> shorthand for creating auto-inc int col
-- IDENTITY -> the SQL standard way to create auto inc columns
-- SEQUENCES -> define own sequence and set start + inc values!

-- sequence ex:
-- CREATE SEQUENCE sq START WITH val INCREMENT BY val2;
-- accessing create table:
-- col type DEFAULT nextval('sq')

-- identity ex:
-- col type GENERATED ALWAYS AS IDENTITY

-- serial ex:
-- col SERIAL -> serial is a type

CREATE SEQUENCE gov_id START WITH 1000 INCREMENT BY 3;

CREATE TABLE gov_employee (

    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    gov_id INTEGER DEFAULT nextval('gov_id'),
    name TEXT

);

-- Do not modify below this line --
INSERT INTO gov_employee (name) 
  VALUES
      ('John Doe'),
      ('Jane Doe'),
      ('Jim Beam');

SELECT * FROM gov_employee;
