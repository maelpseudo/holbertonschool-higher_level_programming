-- Crée l'utilisateur `user_0d_1` s'il n'existe pas déjà et définit son mot de passe
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Accorde à `user_0d_1` tous les privilèges sur le serveur MySQL
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Applique immédiatement les modifications des privilèges
FLUSH PRIVILEGES;
