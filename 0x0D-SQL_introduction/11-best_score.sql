-- Lists all records with value >= 10 in the table second_table in descending score 
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BY `score` DESC;
