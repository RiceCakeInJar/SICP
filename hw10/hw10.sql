.read hw10_data.sql


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs, sizes WHERE height > min AND height <= max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT child AS name FROM dogs, parents WHERE name = parent ORDER BY -height;


-- Sentences about siblings that are the same size
CREATE TABLE siblings AS
  SELECT a.child AS m, b.child AS n FROM parents AS a,parents AS b
    WHERE a.parent = b.parent AND a.child < b.child;

CREATE TABLE sentences AS
  SELECT 'The two siblings, ' || m || ' plus ' || n || ' have the same size: ' || a.size
    FROM siblings,size_of_dogs AS a, size_of_dogs AS b
      WHERE m = a.name AND n = b.name AND a.size = b.size;
 