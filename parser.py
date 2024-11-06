import ply.yacc as yacc
from lexer import tokens

def p_query(p):
    '''query : select_query
             | insert_query
             | update_query
             | alter_query
             | delete_query'''
    p[0] = p[1]


def p_alter_query(p):
    '''alter_query : CAMBIA LA TABLA table alter_action SEMICOLON'''
    p[0] = 'ALTER TABLE {} {};'.format(p[4], p[5])

def p_alter_action(p):
    '''alter_action : AGREGA LA COLUMNA IDENTIFIER datatype opt_constraints
                    | ELIMINA LA COLUMNA IDENTIFIER'''
    if p[1] == 'AGREGA':
        p[0] = 'ADD COLUMN {} {} {}'.format(p[4], p[5], ' '.join(p[6]))
    else:
        p[0] = 'DROP COLUMN {}'.format(p[4])

def p_opt_constraints(p):
    '''opt_constraints : constraints
                       | '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = []

def p_constraints(p):
    '''constraints : constraints constraint
                   | constraint'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_constraint(p):
    '''constraint : NO NULO
                  | UNICO
                  | POR_DEFECTO value'''
    if p[1] == 'NO':
        p[0] = 'NOT NULL'
    elif p[1] == 'UNICO':
        p[0] = 'UNIQUE'
    elif p[1] == 'POR_DEFECTO':
        p[0] = 'DEFAULT ' + p[2]

def p_datatype(p):
    'datatype : IDENTIFIER LPAREN NUMBER RPAREN'
    p[0] = '{}({})'.format(p[1], p[3])


def p_select_query(p):
    'select_query : TRAEME selection DE LA TABLA table opt_join_clause opt_where_clause opt_group_by_clause opt_having_clause opt_order_by_clause opt_limit_clause SEMICOLON'
    p[0] = 'SELECT {} FROM {}{}{}{}{}{}{}{}'.format(p[2], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13])

def p_selection(p):
    '''selection : TODO
                 | LOS DISTINTOS columns
                 | CONTANDO LPAREN ASTERISK RPAREN
                 | CONTANDO LPAREN TODO RPAREN
                 | columns'''
    if p[1] == 'TODO':
        p[0] = '*'
    elif p[1] == 'LOS':
        p[0] = 'DISTINCT ' + p[3]
    elif p[1] == 'CONTANDO':
        p[0] = 'COUNT(*)'
    else:
        p[0] = p[1]

def p_opt_having_clause(p):
    '''opt_having_clause : WHERE DEL GROUP BY condition
                         | '''
    if len(p) == 6:
        p[0] = ' HAVING {}'.format(p[5])
    else:
        p[0] = ''

def p_opt_join_clause(p):
    '''opt_join_clause : MEZCLANDO table EN condition
                       | '''
    if len(p) == 5:
        p[0] = ' JOIN {} ON {}'.format(p[2], p[4])
    else:
        p[0] = ''


def p_columns(p):
    'columns : column_list'
    p[0] = p[1]

def p_column_list(p):
    '''column_list : column_list COMMA column
                   | column'''
    if len(p) == 4:
        p[0] = '{} , {}'.format(p[1], p[3])
    else:
        p[0] = p[1]

def p_column(p):
    'column : IDENTIFIER'
    p[0] = p[1]

def p_table(p):
    'table : IDENTIFIER '
    p[0] = p[1]

def p_opt_where_clause(p):
    '''opt_where_clause : DONDE condition
                        | '''
    if len(p) == 3:
        p[0] = ' WHERE ' + p[2]
    else:
        p[0] = ''

def p_condition(p):
    '''condition : IDENTIFIER EQUALS value
                 | IDENTIFIER GREATER value
                 | IDENTIFIER LESS value
                 | IDENTIFIER GREATER_EQUALS value
                 | IDENTIFIER LESS_EQUALS value
                 | IDENTIFIER NOT_EQUALS value
                 | IDENTIFIER ENTRE value AND value
                 | IDENTIFIER PARECIDO_A value
                 | IDENTIFIER ES_NULO
                 | CONTANDO LPAREN ASTERISK RPAREN GREATER NUMBER'''

    if p[2] == 'ES_NULO':
        p[0] = '{} IS NULL'.format(p[1])
    elif p[2] == 'ENTRE':
        p[0] = '{} BETWEEN {} AND {}'.format(p[1], p[3], p[5])
    elif p[2] == 'PARECIDO_A':
        p[0] = '{} LIKE {}'.format(p[1], p[3])
    elif p[1] == 'CONTANDO':
        p[0] = 'COUNT(*) > {}'.format(p[6])
    else:
        p[0] = '{} {} {}'.format(p[1], p[2], p[3])

def p_value(p):
    '''value : NUMBER
             | STRING
             | IDENTIFIER '''
    p[0] = p[1]

def p_opt_group_by_clause(p):
    '''opt_group_by_clause : AGRUPANDO POR columns
                           | '''
    if len(p) == 4:
        p[0] = ' GROUP BY ' + p[3]
    else:
        p[0] = ''

def p_opt_order_by_clause(p):
    '''opt_order_by_clause : ORDENA_POR columns
                           | '''
    if len(p) == 3:
        p[0] = 'ORDER BY ' + p[2]
    else:
        p[0] = ''

def p_opt_limit_clause(p):
    '''opt_limit_clause : COMO_MUCHO NUMBER
                        | '''
    if len(p) == 3:
        p[0] = 'LIMIT ' + p[2]
    else:
        p[0] = ''

def p_insert_query(p):
    'insert_query : METE EN table LPAREN columns RPAREN LOS VALORES LPAREN values RPAREN SEMICOLON'
    p[0] = 'INSERT INTO {} ({}) VALUES ({});'.format(p[3], p[5], p[10])

def p_values(p):
    '''values : values COMMA value
              | value'''
    if len(p) == 4:
        p[0] = '{} , {}'.format(p[1], p[3])
    else:
        p[0] = p[1]

def p_update_query(p):
    'update_query : ACTUALIZA table SETEA assignments opt_where_clause SEMICOLON'
    if p[5]:
        p[0] = f"UPDATE {p[2]} SET {p[4]} {p[5]};"
    else:
        p[0] = f"UPDATE {p[2]} SET {p[4]};"

def p_assignments(p):
    '''assignments : assignments COMMA assignment
                   | assignment'''
    if len(p) == 4:
        p[0] = '{} , {}'.format(p[1], p[3])
    else:
        p[0] = p[1]

def p_assignment(p):
    'assignment : IDENTIFIER EQUALS value'
    p[0] = '{} = {}'.format(p[1], p[3])

def p_delete_query(p):
    'delete_query : BORRA DE LA TABLA table opt_where_clause SEMICOLON'
    if p[6]:
        p[0] = 'DELETE FROM {} {};'.format(p[5], p[6])
    else:
        p[0] = 'DELETE FROM {}'.format(p[5])

def p_error(p):
    if p:
        print(f"Error de sintaxis en el token '{p.value}' en la línea {p.lineno}")
        raise SyntaxError(f"Error de sintaxis en el token '{p.value}', tipo: {p.type}")
    else:
        raise SyntaxError("Error de sintaxis en la entrada: No hay más tokens")

parser = yacc.yacc(debug=True)
