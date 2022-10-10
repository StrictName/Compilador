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
    'public' : 'PUBLIC',
    'private' : 'PRIVATE',
    'protected' : 'PROTECTED',
    'attribute' : 'ATTRIBUTE',
    'method' : 'METHOD',
    'read' : 'READ',
    'write' : 'WRITE',
    'while' : 'WHILE',
    'do' : 'DO',
    'from' : 'FROM',
    'to' : 'TO',
    'and' : 'AND',
    'or' : 'OR',
    'not' : 'NOT',
    'equal' : 'EQUAL',
    'if' : 'IF',
    'else' : 'ELSE'
}

tokens = [
    'ID',
    'PUNTOCOMA',
    'PARENTESISIZQ',
    'PARENTESISDER',
    'LLAVEIZQ',
    'LLAVEDER',
    'CTEI',
    'CTEF',
    'CTECH',
    'CORCHETEIZQ',
    'CORCHETEDER',
    'COMA',
    'DOSPUNTOS',
    'IGUAL',
    'LETRERO',
    'LESSTHAN',
    'GREATERTHAN',
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'PUNTO'
] + list(reserved.values())

t_PUNTOCOMA = r';'
t_PARENTESISIZQ = r'\('
t_PARENTESISDER = r'\)'
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'
t_CORCHETEIZQ = r'\['
t_CORCHETEDER = r'\]'
t_COMA = r','
t_DOSPUNTOS = r'\:'
t_IGUAL = r'\='
t_LESSTHAN = r'\<'
t_GREATERTHAN = r'\>'
t_MAS = r'\+'
t_MENOS = r'\-'
t_POR = r'\*'
t_DIV = r'\/'
t_PUNTO = r'.'

t_LETRERO = r'"[a-zA-Z_][a-zA-Z_0-9]*"'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_CTECH(t):
    r'\'[a-zA-Z_][a-zA-Z_0-9]?\''
    t.type = reserved.get(t.value, 'CTECH')
    return t

def t_CTEF(t):
    r'\d+\.\d+'
    t.value = float(t.value)
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

def return_type_cubo(opdo1, opdo2, operador):
    return cubo_semantico[opdo1][opdo2][operador]
cubo_semantico = {
   'int':{
        'int':{
            '+': 'int',
            '-': 'int',
            '/': 'float',
            '*': 'int',
            '<': 'bool',
            '>': 'bool',
            'and': 'err',
            'or': 'err',
            'not': 'bool',
            'equal': 'bool',
            '=': True
        },
        'float':{
            '+': 'float',
            '-': 'float',
            '/': 'float',
            '*': 'float',
            '<': 'bool',
            '>': 'bool',
            'and': 'err',
            'or': 'err',
            'not': 'bool',
            'equal': 'bool',
            '=': False
        },
        'bool':{
            '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            'and': 'err',
            'or': 'err',
            'not': 'err',
            'equal': 'err',
            '=': False
        },
        'char':{
            '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            'and': 'err',
            'or': 'err',
            'not': 'err',
            'equal': 'err',
            '=': False
        }
    },

    'float':{
        'int':{
            '+': 'float',
            '-': 'float',
            '/': 'float',
            '*': 'float',
            '<': 'bool',
            '>': 'bool',
            'and': 'err',
            'or': 'err',
            'not': 'bool',
            'equal': 'bool',
            '=': True
        },
        'float':{
            '+': 'float',
            '-': 'float',
            '/': 'float',
            '*': 'float',
            '<': 'bool',
            '>': 'bool',
            'and': 'err',
            'or': 'err',
            'not': 'bool',
            'equal': 'bool',
            '=': True
        },
        'bool':{
            '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            'and': 'err',
            'or': 'err',
            'not': 'err',
            'equal': 'err',
            '=': False
        },
        'char':{
            '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            'and': 'err',
            'or': 'err',
            'not': 'err',
            'equal': 'err',
            '=': False
        }
    },

    'bool':{
        'int':{
            '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            'and': 'err',
            'or': 'err',
            'not': 'err',
            'equal': 'err',
            '=': False
        },
        'float':{
            '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            'and': 'err',
            'or': 'err',
            'not': 'err',
            'equal': 'err',
            '=': False
        },
        'bool':{
            '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            'and': 'bool',
            'or': 'bool',
            'not': 'bool',
            'equal': 'bool',
            '=': True
        },
        'char':{
            '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            'and': 'err',
            'or': 'err',
            'not': 'err',
            'equal': 'err',
            '=': False
        }
    },
    'char':{
        'int':{
            '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            'and': 'err',
            'or': 'err',
            'not': 'err',
            'equal': 'err',
            '=': False
        },
        'float':{
            '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            'and': 'err',
            'or': 'err',
            'not': 'err',
            'equal': 'err',
            '=': False
        },
        'bool':{
            '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            'and': 'err',
            'or': 'err',
            'not': 'err',
            'equal': 'err',
            '=': False
        },
        'char':{
            '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            'and': 'err',
            'or': 'err',
            'not': 'bool',
            'equal': 'bool',
            '=': True
        }
    }

}

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
            | MAIN PARENTESISIZQ PARENTESISDER LLAVEIZQ estatuto LLAVEDER'''

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
    '''tipo_simple : INT n_seen_type
                    | FLOAT
                    | CHAR
                    | BOOL'''

def p_tipo_compuesto(t):
    '''tipo_compuesto : ID'''

def p_funcion(t):
    '''funcion : FUNC tipo_simple ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var cuerpo
                | FUNC tipo_simple ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var cuerpo funcion
                | FUNC tipo_simple ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA cuerpo
                | FUNC tipo_simple ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA cuerpo funcion
                | FUNC VOID ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var cuerpo
                | FUNC VOID ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var cuerpo funcion
                | FUNC VOID ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA cuerpo
                | FUNC VOID ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA cuerpo funcion'''

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
    '''cuerpo : LLAVEIZQ estatuto RETURN exp PUNTOCOMA LLAVEDER
                | LLAVEIZQ estatuto LLAVEDER'''

def p_bloque_clase(t):
    '''bloque_clase : ATTRIBUTE DOSPUNTOS atributo METHOD DOSPUNTOS metodo'''

def p_atributo(t):
    '''atributo : tipo_clase tipo_simple ID PUNTOCOMA
                | tipo_clase tipo_simple ID PUNTOCOMA atributo'''

def p_metodo(t):
    '''metodo : tipo_clase tipo_simple ID PARENTESISIZQ parametros PARENTESISDER cuerpo
            | tipo_clase tipo_simple ID PARENTESISIZQ parametros PARENTESISDER cuerpo metodo
            | tipo_clase VOID ID PARENTESISIZQ parametros PARENTESISDER cuerpo
            | tipo_clase VOID ID PARENTESISIZQ parametros PARENTESISDER cuerpo metodo'''


def p_estatuto(t):
    '''estatuto : asignacion PUNTOCOMA
                | asignacion PUNTOCOMA estatuto
                | llamada PUNTOCOMA
                | llamada PUNTOCOMA estatuto
                | lee PUNTOCOMA
                | lee PUNTOCOMA estatuto
                | escribe PUNTOCOMA
                | escribe PUNTOCOMA estatuto
                | condicion
                | condicion estatuto
                | ciclo_w
                | ciclo_w estatuto
                | ciclo_f
                | ciclo_f estatuto
                | llamada_metodo PUNTOCOMA estatuto
                | llamada_atributo PUNTOCOMA estatuto'''

def p_asignacion(t):
    '''asignacion : variable IGUAL exp'''

def p_llamada(t):
    '''llamada :  ID PARENTESISIZQ llamadap PARENTESISDER'''

def p_llamadap(t):
    '''llamadap : exp
                | exp COMA llamadap'''

def p_lee(t):
    '''lee : READ PARENTESISIZQ leep PARENTESISDER'''

def p_leep(t):
    '''leep : variable
            | variable COMA leep'''

def p_variable(t):
    '''variable : ID
                | ID CORCHETEIZQ exp CORCHETEDER
                | ID CORCHETEIZQ exp CORCHETEDER CORCHETEIZQ exp CORCHETEDER'''

def p_escribe(t):
    '''escribe : WRITE PARENTESISIZQ escribep PARENTESISDER'''

def p_escribep(t):
    '''escribep : exp
                | exp COMA escribep
                | LETRERO
                | LETRERO COMA escribep'''

def p_condicion(t):
    '''condicion : IF PARENTESISIZQ exp PARENTESISDER LLAVEIZQ estatuto LLAVEDER
                | IF PARENTESISIZQ exp PARENTESISDER LLAVEIZQ estatuto LLAVEDER ELSE LLAVEIZQ estatuto LLAVEDER'''

def p_ciclo_w(t):
    '''ciclo_w : WHILE PARENTESISIZQ exp PARENTESISDER DO LLAVEIZQ estatuto LLAVEDER'''

def p_ciclo_f(t):
    '''ciclo_f : FROM variable IGUAL exp TO exp DO LLAVEIZQ estatuto LLAVEDER'''

def p_exp(t):
    '''exp : t_exp
            | t_exp OR exp'''

def p_t_exp(t):
    '''t_exp : g_exp
            | g_exp AND t_exp'''

def p_g_exp(t):
    '''g_exp : m_exp
            | m_exp EQUAL m_exp
            | m_exp NOT m_exp
            | m_exp GREATERTHAN m_exp
            | m_exp LESSTHAN m_exp'''

def p_m_exp(t):
    '''m_exp : t
            | t MAS m_exp
            | t MENOS m_exp'''

def p_t(t):
    '''t : f
        | f POR t
        | f DIV t'''

def p_f(t):
    '''f : PARENTESISIZQ exp PARENTESISDER
        | CTEI
        | CTEF
        | CTECH
        | variable
        | llamada
        | llamada_metodo
        | llamada_atributo'''

def p_llamada_metodo(t):
    '''llamada_metodo : ID PUNTO ID PARENTESISIZQ llamada_metodop PARENTESISDER'''

def p_llamada_metodop(t):
    '''llamada_metodop : CTEI
                        | CTEI COMA llamada_metodop
                        | CTEF
                        | CTEF COMA llamada_metodop
                        | CTECH
                        | CTECH COMA llamada_metodop
                        | ID
                        | ID COMA llamada_metodop'''

def p_llamada_atributo(t):
    '''llamada_atributo : ID PUNTO ID'''

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)


# Punto neuralgico para reconocer el tipo
def p_n_seen_type(p):
    'n_seen_type : '
    global current_type
    current_type = p[-1]


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