-- Ce script liste tous les enregistrements de `second_table` avec un nom non vide,
-- en affichant le score et le nom, triés par score de manière décroissante

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name <> '' ORDER BY score DESC;
