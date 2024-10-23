# lexer.py

import ply.lex as lex
from keyword_mapping import keywords_mapping

# Crear mapeo inverso para USQL a SQL
reverse_keywords_mapping = {v: k for k, v in keywords_mapping.items()}

# Función para limpiar y generar nombres de tokens válidos
def clean_token_name(name):
    import re
    name = name.replace(' ', '_')
    name = name.replace(':', '')
    name = name.replace('*', 'ASTERISK')
    name = re.sub(r'\W', '', name)
    return name.upper()

# Lista base de tokens
tokens = [
    'IDENTIFIER',
    'STRING',
    'NUMBER',
    'COMMA',
    'SEMICOLON',
    'DOT',
    'EQUALS',
    'GREATER',
    'LESS',
    'GREATER_EQUALS',
    'LESS_EQUALS',
    'NOT_EQUALS',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'AND',
    'OR',
    'NOT',
    'ASTERISK',  # Incluir 'ASTERISK' como token
]

# Crear el diccionario 'reserved' a partir de las palabras clave
reserved = {}
for keyword in keywords_mapping.values():
    token_name = clean_token_name(keyword)
    reserved[keyword.upper()] = token_name

for keyword in keywords_mapping.keys():
    token_name = clean_token_name(keyword)
    reserved[keyword.upper()] = token_name

# Agregar tokens generados a partir de las palabras clave
tokens += list(set(reserved.values()))

# Remover duplicados
tokens = list(set(tokens))

# Definiciones de expresiones regulares para los tokens
t_COMMA = r','
t_SEMICOLON = r';'
#t_DOT = r'\.'
t_EQUALS = r'='
t_GREATER_EQUALS = r'>='
t_LESS_EQUALS = r'<='
t_NOT_EQUALS = r'<>|!='
t_ASTERISK = r'\*'
t_GREATER = r'>'
t_LESS = r'<'
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COUNT = r'COUNT|CONTANDO'

def t_AND(t):
    r'AND|Y'
    return t

def t_OR(t):
    r'OR|O'
    return t

# def t_NOT(t):
#     r'NOT|NO'
#     return t


# Token para identificadores y palabras clave
def t_IDENTIFIER(t):
    r'[A-Za-z_][A-Za-z0-9_]*(\.[A-Za-z_][A-Za-z0-9_]*)*'
    t_upper = t.value.upper()
    if t_upper in reserved:
        t.type = reserved[t_upper]
    else:
        t.type = 'IDENTIFIER'
    return t

# Token para cadenas de texto
def t_STRING(t):
    r'\'([^\\\n]|(\\.))*?\''
    return t

# Token para números
def t_NUMBER(t):
    r'\d+'
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de nuevas líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

# Función para depurar e imprimir los tokens
def print_tokens(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)