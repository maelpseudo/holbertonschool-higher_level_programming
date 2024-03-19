-- Ce script liste tous les enregistrements de `second_table` avec un score >= 10,
-- en affichant score et nom, et ordonne les résultats par score de manière décroissante

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
