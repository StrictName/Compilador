from queue import Empty
from symbol import parameters
import ply.lex as lex
import sys
import ply.yacc as yacc
from varTable import varTable
from funcTable import funcTable
from parametro import Parameter
from arreglo import Array
from arrayTable import arrayTable
from semanticCube import SemanticCube
from classTable import classTable


varsTable = varTable()
functionsTable = funcTable()
arraysTable = arrayTable()
claseTable = classTable()

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
t_ignore = ' \t\n\b'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex()

POper = []
PilaO = []

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
    '''clase : CLASS ID getnameClass_np getSonClass_np saveClass_np DOSPUNTOS tipo_clase ID LLAVEIZQ bloque_clase LLAVEDER PUNTOCOMA
            | CLASS ID getnameClass_np getSonClass_np saveClass_np DOSPUNTOS tipo_clase ID LLAVEIZQ bloque_clase LLAVEDER PUNTOCOMA clase
            | CLASS ID getnameClass_np getSonClass_np saveClass_np DOSPUNTOS tipo_clase ID LLAVEIZQ LLAVEDER PUNTOCOMA
            | CLASS ID getnameClass_np getSonClass_np saveClass_np DOSPUNTOS tipo_clase ID LLAVEIZQ LLAVEDER PUNTOCOMA clase
            | CLASS ID getnameClass_np getFatherClass_np saveClass_np LLAVEIZQ bloque_clase LLAVEDER PUNTOCOMA
            | CLASS ID getnameClass_np getFatherClass_np saveClass_np LLAVEIZQ bloque_clase LLAVEDER PUNTOCOMA clase
            | CLASS ID getnameClass_np getFatherClass_np saveClass_np LLAVEIZQ LLAVEDER PUNTOCOMA
            | CLASS ID getnameClass_np getFatherClass_np saveClass_np LLAVEIZQ LLAVEDER PUNTOCOMA clase'''

def p_tipo_clase(t):
    '''tipo_clase : PUBLIC
                    | PROTECTED
                    | PRIVATE'''

def p_var(t):
    '''var : VAR scopeGlobal_np varp'''

def p_varp(t):
    '''varp : tipo_compuesto ID PUNTOCOMA
            | tipo_compuesto ID PUNTOCOMA varp
            | tipo_simple ID getID_np PUNTOCOMA saveVar_np
            | tipo_simple ID getID_np PUNTOCOMA saveVar_np varp
            | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA
            | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA varp
            | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA
            | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA varp'''

def p_tipo_simple(t):
    '''tipo_simple : INT getType_np
                    | FLOAT getType_np
                    | CHAR getType_np
                    | BOOL getType_np'''


def p_tipo_compuesto(t):
    '''tipo_compuesto : ID getType_np'''

def p_funcion(t):
    '''funcion : FUNC tipo_simple getTypeFunc_np ID getIDFunc_np PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var saveFunc_np cuerpo
                | FUNC tipo_simple getTypeFunc_np ID getIDFunc_np PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var saveFunc_np cuerpo funcion
                | FUNC tipo_simple getTypeFunc_np ID getIDFunc_np PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA saveFunc_np cuerpo
                | FUNC tipo_simple getTypeFunc_np ID getIDFunc_np PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA saveFunc_np cuerpo funcion
                | FUNC VOID getTypeFunc_np ID getIDFunc_np PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var saveFunc_np cuerpo
                | FUNC VOID getTypeFunc_np ID getIDFunc_np PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var saveFunc_np cuerpo funcion
                | FUNC VOID getTypeFunc_np ID getIDFunc_np PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA saveFunc_np cuerpo
                | FUNC VOID getTypeFunc_np ID getIDFunc_np PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA cuerpo saveFunc_np funcion'''

def p_dec_var(t):
    '''dec_var : VAR  scopeFunc_np dec_varp'''

def p_dec_varp(t):
    '''dec_varp : tipo_simple ID getID_np PUNTOCOMA saveVar_np dec_varp
                | tipo_simple ID getID_np PUNTOCOMA saveVar_np
                | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA dec_varp
                | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA
                | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA dec_varp
                | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA'''

def p_parametros(t):
    '''parametros : tipo_simple ID getParameters_np saveParameter_np
                    | tipo_simple ID getParameters_np COMA saveParameter_np parametros'''

def p_cuerpo(t):
    '''cuerpo : LLAVEIZQ estatuto RETURN exp PUNTOCOMA LLAVEDER
                | LLAVEIZQ estatuto LLAVEDER'''

def p_bloque_clase(t):
    '''bloque_clase : ATTRIBUTE scopeClass_np DOSPUNTOS atributo METHOD DOSPUNTOS metodo'''

def p_atributo(t):
    '''atributo : tipo_clase tipo_simple ID getID_np PUNTOCOMA saveVar_np
                | tipo_clase tipo_simple ID getID_np PUNTOCOMA saveVar_np atributo'''

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
    '''variable : ID saveIDpilaO_np
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
            | t_exp OR saveOperadorOr_np exp'''

def p_t_exp(t):
    '''t_exp : g_exp
            | g_exp AND saveOperadorAnd_np t_exp'''

def p_g_exp(t):
    '''g_exp : m_exp
            | m_exp EQUAL saveOperadorRelacional_np m_exp
            | m_exp NOT saveOperadorRelacional_np m_exp
            | m_exp GREATERTHAN saveOperadorRelacional_np m_exp
            | m_exp LESSTHAN saveOperadorRelacional_np m_exp'''

def p_m_exp(t):
    '''m_exp : t
            | t MAS saveOperadorMasMenos_np m_exp
            | t MENOS saveOperadorMasMenos_np m_exp'''

def p_t(t):
    '''t : f
        | f POR saveOperadorMultiDivision_np t
        | f DIV saveOperadorMultiDivision_np t'''

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

def p_empty(p):
    'empty :'
    pass

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)



# PUNTOS NEURÁLGICOS #


#Guarda datos de la clase
def p_getnameClass_np(p):
    '''getnameClass_np : empty'''
    global current_name_class
    current_name_class = p[-1]

def p_geFatherClass_np(p):
    '''getFatherClass_np : empty'''
    global current_class_type
    current_class_type = 'father'

def p_getSonClass_np(p):
    '''getSonClass_np : empty'''
    global current_class_type
    current_class_type = 'son'

def p_saveClass_np(p):
    '''saveClass_np : empty'''
    claseTable.add(current_name_class, current_class_type)

# Guarda datos de las variables
def p_getID_np(p):
    '''getID_np : empty'''
    global current_var_id
    current_var_id = p[-1]

def p_getType_np(p):
    '''getType_np : empty'''
    global current_var_type
    current_var_type = p[-1]


#def p_getArraySize_np(p):
#    '''getArraySize_np : empty'''
#    global current_array_size
#    current_array_size = p[-1]

def p_scopeClass_np(p):
    '''scopeClass_np : empty'''
    global current_var_scope
    current_var_scope = 'class'

def p_scopeFunc_np(p):
    '''scopeFunc_np : empty'''
    global current_var_scope
    current_var_scope = 'func'

def p_scopeGlobal_np(p):
    '''scopeGlobal_np : empty'''
    global current_var_scope
    current_var_scope = 'global'

def p_saveVar_np(p):
    '''saveVar_np : empty'''
    varsTable.add(current_var_id, current_var_type, current_var_scope)

#Guarda datos de las funciones

def p_getIDFunc_np(p):
    '''getIDFunc_np : empty'''
    global current_func_id
    current_func_id = str(p[-1])

def p_getTypeFunc_np(p):
    '''getTypeFunc_np : empty'''
    global current_func_type
    current_func_type = str(p[-1])

def p_getParameters_np(p):
    '''getParameters_np : empty'''
    global current_parameter
    current_parameter = Parameter(str(p[-2]), str(p[-1]))

def p_saveParameter_np(p):
    '''saveParameter_np : empty'''
    global parameters_list
    parameters_list = []
    parameters_list.append(current_parameter)

def p_saveFunc_np(p):
    '''saveFunc_np : empty'''
    functionsTable.add(current_func_id, current_func_type, parameters_list, varsTable)


def p_saveIDpilaO_np(p):
    '''saveIDpilaO_np : empty'''
    global current_id_cuadruplo
    current_id_cuadruplo = p[-1]
    PilaO.append(current_id_cuadruplo)

def p_saveOperadorMultiDivision_np(p):
    '''saveOperadorMultiDivision_np : empty'''
    global current_oper_cuadruplo
    current_oper_cuadruplo = p[-1]
    POper.append(current_oper_cuadruplo)

def p_saveOperadorMasMenos_np(p):
    '''saveOperadorMasMenos_np : empty'''
    global current_oper_cuadruplo
    current_oper_cuadruplo = p[-1]
    POper.append(current_oper_cuadruplo)

def p_saveOperadorRelacional_np(p):
    '''saveOperadorRelacional_np : empty'''
    global current_oper_cuadruplo
    current_oper_cuadruplo = p[-1]
    POper.append(current_oper_cuadruplo)

def p_saveOperadorOr_np(p):
    '''saveOperadorOr_np : empty'''
    global current_oper_cuadruplo
    current_oper_cuadruplo = p[-1]
    POper.append(current_oper_cuadruplo)

def p_saveOperadorAnd_np(p):
    '''saveOperadorAnd_np : empty'''
    global current_oper_cuadruplo
    current_oper_cuadruplo = p[-1]
    POper.append(current_oper_cuadruplo)

def p_pushFondoFalso_np(p):
    '''pushFondoFalso_np : empty'''
    POper.append('(')

def p_popFondoFalso_np(p):
    '''popFondoFalso_np : empty'''
    global POper
    top = POper.pop()
    if top != '(':
        print("ERROR Fondo Falso")

def p_plusMinus_np(p):
    '''plusMinus_np : empty'''
    if len(POper) > 0:
        if POper[-1] == '+' or '-':
            left_operand = PilaO.pop()
            right_operand = PilaO.pop()
            operador = POper.pop()
    print(left_operand, right_operand, operador)

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
        
'''
parser = yacc.yacc()
file = sys.argv[1]
f = open(file, 'r')
data = f.read()
case01 = parser.parse(data)
'''

print("Tabla de variables")
print(varsTable.toString())

print("Tabla de clases")
print(claseTable.toString())

print(PilaO)
print(POper)
