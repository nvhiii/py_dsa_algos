-- default values demo
-- we can specify defaults using the DEFAULT keyword after the col and the datatype then include default val
-- if row input doesnt have value for that col and the col has default, it will be the default set in place!
-- if no default is present and row has no val for the specific col, then the val auto input is NULL

CREATE TABLE videos (

    id INTEGER, -- no default
    name TEXT DEFAULT 'Untitled',
    is_published BOOLEAN DEFAULT false

);

-- Do not modify below this line --
INSERT INTO videos (id, name, is_published) 
VALUES (1, 'My Video', true),
       (2, 'Another Video', false);

INSERT INTO videos (id)
VALUES (3),
       (4);

INSERT INTO videos (name)
VALUES ('Video with no ID');

SELECT * FROM videos;
