-- Lists all records with a name in the table second_table in descending score 
SELECT `score`, `name` FROM `second_table` WHERE `name` != "" ORDER BY `score` DESC;
