# translator.py

from lexer import print_tokens
from parser import parser

def translate_usql_to_sql(usql_query):
    try:
        # Parseamos la consulta USQL sin modificar
        result = parser.parse(usql_query)
        return result
    except Exception as e:
        raise SyntaxError(f"Consulta USQL inválida: {e}")
