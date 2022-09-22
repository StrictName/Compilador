import ply.lex as lex

reserved = {
    'program' : 'PROGRAM',
    'main' : 'MAIN',
    'class' : 'CLASS',
    'var' : 'VAR',
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR'
}

tokens = [
    'ID',
    'PUNTOCOMA',
    'PARENTESISIZQ',
    'PARENTESISDER',
    'LLAVEIZQ',
    'LLAVEDER',
    'FUNCION',
    'BLOQUE',
    'BLOQUECLASE',
    'CTEI',
    'CORCHETEIZQ',
    'CORCHETEDER'
] + list(reserved.values())

t_PUNTOCOMA = r';'
t_PARENTESISIZQ = r'\('
t_PARENTESISDER = r'\)'
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'
t_CORCHETEIZQ = r'\['
t_CORCHETEDER = r'\]'

t_FUNCION = r'FUNCION'
t_BLOQUE = r'BLOQUE'
t_BLOQUECLASE = r'BLOQUECLASE'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_CTEI(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\n\b'
 
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lex.lex()


import sys
import ply.yacc as yacc

def p_programa(t):
    '''programa : PROGRAM ID PUNTOCOMA main
                | PROGRAM ID PUNTOCOMA clase main
                | PROGRAM ID PUNTOCOMA clase var main
                | PROGRAM ID PUNTOCOMA clase var FUNCION main'''
    t[0] = "Este es un programa"

def p_main(t):
    '''main : MAIN PARENTESISIZQ PARENTESISDER LLAVEIZQ LLAVEDER
            | MAIN PARENTESISIZQ PARENTESISDER LLAVEIZQ BLOQUE LLAVEDER'''

def p_clase(t):
    '''clase : CLASS ID LLAVEIZQ LLAVEDER PUNTOCOMA
            | CLASS ID LLAVEIZQ BLOQUECLASE LLAVEDER PUNTOCOMA'''

def p_var(t):
    '''var : VAR varp'''

def p_varp(t):
    '''varp : tipo_compuesto ID PUNTOCOMA
            | tipo_compuesto ID PUNTOCOMA varp
            | tipo_simple ID PUNTOCOMA
            | tipo_simple ID PUNTOCOMA varp
            | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA
            | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA varp
            | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA
            | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA varp'''

def p_tipo_simple(t):
    '''tipo_simple : INT
                    | FLOAT
                    | CHAR'''

def p_tipo_compuesto(t):
    '''tipo_compuesto : ID'''

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

yacc.yacc()

if __name__ == '__main__':

    if len(sys.argv) > 1:
        file = sys.argv[1]
        try:
            f = open(file, 'r')
            data = f.read()
            f.close()
            if yacc.parse(data) == "Este es un programa":
                print("Sintáxis válida")
        except EOFError:
            print(EOFError)
    else:
        print("Archivo no encontrado")