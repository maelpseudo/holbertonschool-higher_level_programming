-- Ce script liste le nombre d'enregistrements pour chaque score dans `second_table`
-- et les trie par ce nombre de manière décroissante

SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC, score DESC;
