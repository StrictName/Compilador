import ply.lex as lex

reserved = {
    'program' : 'PROGRAM',
    'main' : 'MAIN',
    'class' : 'CLASS',
    'var' : 'VAR',
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
    'bool' : 'BOOL',
    'func' : 'FUNC',
    'void' : 'VOID',
    'return' : 'RETURN',
    'estatuto' : 'ESTATUTO',
    'public' : 'PUBLIC',
    'private' : 'PRIVATE',
    'protected' : 'PROTECTED',
    'attribute' : 'ATTRIBUTE',
    'method' : 'METHOD'
}

tokens = [
    'ID',
    'PUNTOCOMA',
    'PARENTESISIZQ',
    'PARENTESISDER',
    'LLAVEIZQ',
    'LLAVEDER',
    'CTEI',
    'CORCHETEIZQ',
    'CORCHETEDER',
    'COMA',
    'DOSPUNTOS'
] + list(reserved.values())

t_PUNTOCOMA = r';'
t_PARENTESISIZQ = r'\('
t_PARENTESISDER = r'\)'
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'
t_CORCHETEIZQ = r'\['
t_CORCHETEDER = r'\]'
t_COMA = r','
t_DOSPUNTOS = r':'

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
                | PROGRAM ID PUNTOCOMA clase var funcion main
                | PROGRAM ID PUNTOCOMA clase funcion main
                | PROGRAM ID PUNTOCOMA var main
                | PROGRAM ID PUNTOCOMA var funcion main
                | PROGRAM ID PUNTOCOMA funcion main'''
    t[0] = "Este es un programa"

def p_main(t):
    '''main : MAIN PARENTESISIZQ PARENTESISDER LLAVEIZQ LLAVEDER
            | MAIN PARENTESISIZQ PARENTESISDER LLAVEIZQ ESTATUTO LLAVEDER'''

def p_clase(t):
    '''clase : CLASS ID DOSPUNTOS tipo_clase ID LLAVEIZQ bloque_clase LLAVEDER PUNTOCOMA
            | CLASS ID DOSPUNTOS tipo_clase ID LLAVEIZQ bloque_clase LLAVEDER PUNTOCOMA clase
            | CLASS ID DOSPUNTOS tipo_clase ID LLAVEIZQ LLAVEDER PUNTOCOMA
            | CLASS ID DOSPUNTOS tipo_clase ID LLAVEIZQ LLAVEDER PUNTOCOMA clase
            | CLASS ID LLAVEIZQ bloque_clase LLAVEDER PUNTOCOMA
            | CLASS ID LLAVEIZQ bloque_clase LLAVEDER PUNTOCOMA clase
            | CLASS ID LLAVEIZQ LLAVEDER PUNTOCOMA
            | CLASS ID LLAVEIZQ LLAVEDER PUNTOCOMA clase'''

def p_tipo_clase(t):
    '''tipo_clase : PUBLIC
                    | PROTECTED
                    | PRIVATE'''

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
                    | CHAR
                    | BOOL'''

def p_tipo_compuesto(t):
    '''tipo_compuesto : ID'''

def p_funcion(t):
    '''funcion : FUNC tipo_simple ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var cuerpo
                | FUNC tipo_simple ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var cuerpo funcion
                | FUNC tipo_simple ID PARENTESISIZQ PARENTESISDER PUNTOCOMA dec_var cuerpo
                | FUNC tipo_simple ID PARENTESISIZQ PARENTESISDER PUNTOCOMA dec_var cuerpo funcion
                | FUNC tipo_simple ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA cuerpo
                | FUNC tipo_simple ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA cuerpo funcion
                | FUNC tipo_simple ID PARENTESISIZQ PARENTESISDER PUNTOCOMA cuerpo
                | FUNC tipo_simple ID PARENTESISIZQ PARENTESISDER PUNTOCOMA cuerpo funcion
                | FUNC VOID ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var cuerpo
                | FUNC VOID ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var cuerpo funcion
                | FUNC VOID ID PARENTESISIZQ PARENTESISDER PUNTOCOMA dec_var cuerpo
                | FUNC VOID ID PARENTESISIZQ PARENTESISDER PUNTOCOMA dec_var cuerpo funcion
                | FUNC VOID ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA cuerpo
                | FUNC VOID ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA cuerpo funcion
                | FUNC VOID ID PARENTESISIZQ PARENTESISDER PUNTOCOMA cuerpo
                | FUNC VOID ID PARENTESISIZQ PARENTESISDER PUNTOCOMA cuerpo funcion'''

def p_dec_var(t):
    '''dec_var : VAR dec_varp'''

def p_dec_varp(t):
    '''dec_varp : tipo_simple ID PUNTOCOMA dec_varp
                | tipo_simple ID PUNTOCOMA
                | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA dec_varp
                | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA
                | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA dec_varp
                | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA'''

def p_parametros(t):
    '''parametros : tipo_simple ID
                    | tipo_simple ID COMA parametros'''

def p_cuerpo(t):
    '''cuerpo : LLAVEIZQ ESTATUTO RETURN ID PUNTOCOMA LLAVEDER
                | LLAVEIZQ ESTATUTO LLAVEDER'''

def p_bloque_clase(t):
    '''bloque_clase : ATTRIBUTE DOSPUNTOS atributo METHOD DOSPUNTOS metodo'''

def p_atributo(t):
    '''atributo : tipo_clase tipo_simple ID PUNTOCOMA
                | tipo_clase tipo_simple ID PUNTOCOMA atributo'''

def p_metodo(t):
    '''metodo : tipo_clase tipo_simple ID PARENTESISIZQ parametros PARENTESISDER cuerpo
            | tipo_clase tipo_simple ID PARENTESISIZQ PARENTESISDER cuerpo
            | tipo_clase tipo_simple ID PARENTESISIZQ parametros PARENTESISDER cuerpo metodo
            | tipo_clase tipo_simple ID PARENTESISIZQ PARENTESISDER cuerpo metodo
            | tipo_clase VOID ID PARENTESISIZQ parametros PARENTESISDER cuerpo
            | tipo_clase VOID ID PARENTESISIZQ PARENTESISDER cuerpo
            | tipo_clase VOID ID PARENTESISIZQ parametros PARENTESISDER cuerpo metodo
            | tipo_clase VOID ID PARENTESISIZQ PARENTESISDER cuerpo metodo'''




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