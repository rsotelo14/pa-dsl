# keyword_mapping.py

keywords_mapping = {
    "SELECT": "TRAEME",
    "ASTERISK": "TODO",  # Reemplazamos '*' por 'ASTERISK' para un token válido
    "FROM": "DE_LA_TABLA",
    "WHERE": "DONDE",
    "GROUP BY": "AGRUPANDO_POR",
    "AND": "Y",
    "JOIN": "MEZCLANDO",
    "ON": "EN",
    "DISTINCT": "LOS_DISTINTOS",
    "COUNT": "CONTANDO",
    "INSERT INTO": "METE_EN",
    "VALUES": "LOS_VALORES",
    "UPDATE": "ACTUALIZA",
    "SET": "SETEA",
    "DELETE FROM": "BORRA_DE_LA",
    "ORDER BY": "ORDENA_POR",
    "LIMIT": "COMO_MUCHO",
    "HAVING": "WHERE_DEL_GROUP_BY",
    "EXISTS": "EXISTE",
    "IN": "EN_ESTO",  # Removemos los dos puntos
    "BETWEEN": "ENTRE",
    "LIKE": "PARECIDO_A",
    "IS NULL": "ES_NULO",
    "ALTER TABLE": "CAMBIA_LA_TABLA",
    "ADD COLUMN": "AGREGA_LA_COLUMNA",
    "DROP COLUMN": "ELIMINA_LA_COLUMNA",
    "CREATE TABLE": "CREA_LA_TABLA",
    "DROP TABLE": "TIRA_LA_TABLA",
    "DEFAULT": "POR_DEFECTO",
    "UNIQUE": "UNICO",
    "PRIMARY KEY": "CLAVE_PRIMA",
    "FOREIGN KEY": "CLAVE_REFERENTE",
    "NOT NULL": "NO_NULO",
    "CAST": "TRANSFORMA_A",
}

reverse_keywords_mapping = {v: k for k, v in keywords_mapping.items()}