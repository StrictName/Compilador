from distutils.log import error
from queue import Empty
from tokenize import PseudoExtras
import ply.lex as lex
import sys
import ply.yacc as yacc
from varTable import varTable
from funcTable import funcTable
from parametro import Parameter
from cteTable import cteTable
from arreglo import Array
from arrayTable import arrayTable
from semanticCube import SemanticCube
from classTable import classTable
import quadruple as quadruple


varsTable = varTable()
functionsTable = funcTable()
arraysTable = arrayTable()
claseTable = classTable()
cuboS = SemanticCube()
cuadruplo = quadruple.quadruplesList()
constantsTable = cteTable()
#printCuadruplo = quadruple.quadruple()

POper = []
PilaO = []
PilaTipos = []
PSaltos = []

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
    'for' : 'FOR',
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

# Direcciones de memoria virtual
dir_global_int = 0
dir_global_float = 500
dir_global_char = 1000
dir_global_bool = 1500
dir_local_funcion_int = 2000
dir_local_funcion_float = 2500
dir_local_funcion_char = 3000
dir_local_funcion_bool = 3500
dir_local_clase_int = 4000
dir_local_clase_float = 4500
dir_local_clase_char = 5000
dir_local_clase_bool = 5500
dir_constante_int = 6000
dir_constante_float = 6500
dir_constante_char = 7000


def p_programa(t):
    '''programa : PROGRAM getTypeFunc_np ID getIDFunc_np PUNTOCOMA gotoMain_np main
                | PROGRAM getTypeFunc_np ID getIDFunc_np PUNTOCOMA gotoMain_np clase main
                | PROGRAM getTypeFunc_np ID getIDFunc_np PUNTOCOMA gotoMain_np clase var main
                | PROGRAM getTypeFunc_np ID getIDFunc_np PUNTOCOMA gotoMain_np clase var funcion main
                | PROGRAM getTypeFunc_np ID getIDFunc_np PUNTOCOMA gotoMain_np clase funcion main
                | PROGRAM getTypeFunc_np ID getIDFunc_np PUNTOCOMA gotoMain_np var main
                | PROGRAM getTypeFunc_np ID getIDFunc_np PUNTOCOMA gotoMain_np var funcion main
                | PROGRAM getTypeFunc_np ID getIDFunc_np PUNTOCOMA gotoMain_np funcion main'''
    t[0] = "Este es un programa"

def p_main(t):
    '''main : MAIN fillMain_np PARENTESISIZQ PARENTESISDER LLAVEIZQ LLAVEDER
            | MAIN fillMain_np PARENTESISIZQ PARENTESISDER LLAVEIZQ estatuto LLAVEDER'''

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
            | tipo_simple ID getID_np CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA saveVar_np
            | tipo_simple ID getID_np CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA saveVar_np varp
            | tipo_simple ID getID_np CORCHETEIZQ CTEI CORCHETEDER CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA saveVar_np
            | tipo_simple ID getID_np CORCHETEIZQ CTEI CORCHETEDER CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA saveVar_np varp'''

def p_tipo_simple(t):
    '''tipo_simple : INT getType_np
                    | FLOAT getType_np
                    | CHAR getType_np
                    | BOOL getType_np'''

def p_tipo_simple_func(t):
    '''tipo_simple_func : INT getTypeFunc_np
                        | FLOAT getTypeFunc_np
                        | CHAR getTypeFunc_np
                        | BOOL getTypeFunc_np'''


def p_tipo_compuesto(t):
    '''tipo_compuesto : ID'''

def p_funcion(t):
    '''funcion : FUNC tipo_simple_func ID getIDFunc_np PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var saveFunc_np cuerpo
                | FUNC tipo_simple_func ID getIDFunc_np PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var saveFunc_np cuerpo funcion
                | FUNC tipo_simple_func ID getIDFunc_np PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA saveFunc_np cuerpo
                | FUNC tipo_simple_func ID getIDFunc_np PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA saveFunc_np cuerpo funcion
                | FUNC VOID getTypeFunc_np ID getIDFunc_np PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var saveFunc_np cuerpo
                | FUNC VOID getTypeFunc_np ID getIDFunc_np PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var saveFunc_np cuerpo funcion
                | FUNC VOID getTypeFunc_np ID getIDFunc_np PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA saveFunc_np cuerpo
                | FUNC VOID getTypeFunc_np ID getIDFunc_np PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA cuerpo saveFunc_np funcion'''

def p_dec_var(t):
    '''dec_var : VAR  scopeFunc_np dec_varp'''

def p_dec_varp(t):
    '''dec_varp : tipo_simple ID getID_np PUNTOCOMA saveVar_np dec_varp
                | tipo_simple ID getID_np PUNTOCOMA saveVar_np
                | tipo_simple ID getID_np CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA saveVar_np dec_varp
                | tipo_simple ID getID_np CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA saveVar_np
                | tipo_simple ID getID_np CORCHETEIZQ CTEI CORCHETEDER CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA saveVar_np dec_varp
                | tipo_simple ID getID_np CORCHETEIZQ CTEI CORCHETEDER CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA saveVar_np'''

def p_parametros(t):
    '''parametros : INT ID getParameters_np saveParameter_np
                    | INT ID getParameters_np COMA saveParameter_np parametros
                    | FLOAT ID getParameters_np saveParameter_np
                    | FLOAT ID getParameters_np COMA saveParameter_np parametros
                    | CHAR ID getParameters_np saveParameter_np
                    | CHAR ID getParameters_np COMA saveParameter_np parametros
                    | BOOL ID getParameters_np saveParameter_np
                    | BOOL ID getParameters_np COMA saveParameter_np parametros'''

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
    '''estatuto : asignacion PUNTOCOMA multiDiv_np plusMinus_np relationalOp_np and_np or_np igual_np
                | asignacion PUNTOCOMA multiDiv_np plusMinus_np relationalOp_np and_np or_np igual_np estatuto
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
    '''asignacion : variable IGUAL saveOperadorIgual_np exp'''

def p_llamada(t):
    '''llamada :  ID PARENTESISIZQ llamadap PARENTESISDER'''

def p_llamadap(t):
    '''llamadap : exp
                | exp COMA llamadap'''

def p_lee(t):
    '''lee : READ PARENTESISIZQ leep PARENTESISDER'''

def p_leep(t):
    '''leep : variable readQuad_np
            | variable readQuad_np COMA leep'''

def p_variable(t):
    '''variable : ID saveIDpilaO_np
                | ID CORCHETEIZQ exp CORCHETEDER
                | ID CORCHETEIZQ exp CORCHETEDER CORCHETEIZQ exp CORCHETEDER'''

def p_escribe(t):
    '''escribe : WRITE PARENTESISIZQ escribep PARENTESISDER'''

def p_escribep(t):
    '''escribep : exp writeQuad_np
                | exp writeQuad_np COMA escribep
                | LETRERO pushLetrero_np writeQuad_np
                | LETRERO pushLetrero_np writeQuad_np COMA escribep'''

def p_condicion(t):
    '''condicion : IF PARENTESISIZQ exp PARENTESISDER multiDiv_np plusMinus_np relationalOp_np and_np or_np ifQuad_np LLAVEIZQ estatuto LLAVEDER fillIfQuad_np
                | IF PARENTESISIZQ exp PARENTESISDER multiDiv_np plusMinus_np relationalOp_np and_np or_np ifQuad_np LLAVEIZQ estatuto LLAVEDER ELSE elseQuad_np LLAVEIZQ estatuto LLAVEDER fillIfQuad_np'''

def p_ciclo_w(t):
    '''ciclo_w : WHILE whileQuadSaltos_np PARENTESISIZQ exp PARENTESISDER multiDiv_np plusMinus_np relationalOp_np and_np or_np whileQuad_np DO LLAVEIZQ estatuto LLAVEDER fillWhileQuad_np'''

def p_ciclo_f(t):
    '''ciclo_f : FOR variable_for IGUAL exp multiDiv_np plusMinus_np relationalOp_np and_np or_np forInitialExp_np TO exp multiDiv_np plusMinus_np relationalOp_np and_np or_np forResultExp_np DO LLAVEIZQ estatuto LLAVEDER endFor_np'''

def p_variable_for(t):
    '''variable_for : ID validarIdFor_np'''

def p_exp(t):
    '''exp : t_exp
            | t_exp or_np OR saveOperadorOr_np exp'''

def p_t_exp(t):
    '''t_exp : g_exp
            | g_exp and_np AND saveOperadorAnd_np t_exp'''

def p_g_exp(t):
    '''g_exp : m_exp
            | m_exp relationalOp_np EQUAL saveOperadorRelacional_np m_exp
            | m_exp relationalOp_np NOT saveOperadorRelacional_np m_exp
            | m_exp relationalOp_np GREATERTHAN saveOperadorRelacional_np m_exp
            | m_exp relationalOp_np LESSTHAN saveOperadorRelacional_np m_exp'''

def p_m_exp(t):
    '''m_exp : t
            | t plusMinus_np MAS saveOperadorMasMenos_np m_exp
            | t plusMinus_np MENOS saveOperadorMasMenos_np m_exp'''

def p_t(t):
    '''t : f
        | f multiDiv_np POR saveOperadorMultiDivision_np t
        | f multiDiv_np DIV saveOperadorMultiDivision_np t'''

def p_f(t):
    '''f : PARENTESISIZQ exp PARENTESISDER
        | CTEI saveConstantInt_np
        | CTEF saveConstantFloat_np
        | CTECH saveConstantChar_np
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


######################
# PUNTOS NEURÁLGICOS #
######################

##################### Guarda datos de la clase ####################
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

################### Guarda datos de las variables###################
def p_getID_np(p):
    '''getID_np : empty'''
    global current_var_id
    current_var_id = p[-1]

def p_getType_np(p):
    '''getType_np : empty'''
    global current_var_type
    current_var_type = p[-1]

####Arreglo####


#def p_getArray_np(p):
#    '''getArray_np : empty'''
#    global current_var_type
#    current_var_type += '[' + str(p[-2])+']'

####Matriz####

#def p_getMatrix_np(p):
#    '''getMatrix_np : empty'''
#    global current_var_type
#    current_var_type += '[' + str(p[-5])+']' + '[' + str(p[-2])+']'

#####Scope####

def p_scopeClass_np(p):
    '''scopeClass_np : empty'''
    global current_var_scope
    current_var_scope = 'class'

def p_scopeFunc_np(p):
    '''scopeFunc_np : empty'''
    global current_var_scope
    current_var_scope = 'funcion'

def p_scopeGlobal_np(p):
    '''scopeGlobal_np : empty'''
    global current_var_scope
    current_var_scope = 'global'

def p_saveVar_np(p):
    '''saveVar_np : empty'''
    address = asignar_direccion_memoria()
    varsTable.add(current_var_id, current_var_type, current_var_scope, address)

def p_saveConstantInt_np(p):
    '''saveConstantInt_np : empty'''
    global cte_type
    cte_type = 'int'
    address = asignar_direccion_memoriaCtes()
    PilaO.append(address)
    PilaTipos.append(cte_type)
    constantsTable.add(p[-1], cte_type, address)

def p_saveConstantFloat_np(p):
    '''saveConstantFloat_np : empty'''
    global cte_type
    cte_type = 'float'
    address = asignar_direccion_memoriaCtes()
    PilaO.append(address)
    PilaTipos.append(cte_type)
    constantsTable.add(p[-1], cte_type, address)

def p_saveConstantChar_np(p):
    '''saveConstantChar_np : empty'''
    global cte_type
    cte_type = 'char'
    address = asignar_direccion_memoriaCtes()
    PilaO.append(address)
    PilaTipos.append(cte_type)
    constantsTable.add(p[-1], cte_type, address)

################Guarda datos de las funciones###################

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
    functionsTable.add(current_func_id, current_func_type, parameters_list)

############################Cuadruplos#########################3

#def p_saveTypeVar_np(p):
#    '''saveTypeVar_np : empty'''
#    global current_var_type
#    current_var_type = p[-2]
#    PilaTipos.append(current_var_type)

def search_address(id):
    global varsTable
    if id == varsTable.search(id):
        return varsTable.find_address(id)
    else:
        error('No se encontró la dirección de la variable')

def search_type(id):
    global varsTable
    if id == varsTable.search(id):
        return varsTable.find_type(id)
    else:
        error('No se encontró el type de la variable')

def p_saveIDpilaO_np(p):
    '''saveIDpilaO_np : empty'''
    PilaO.append(search_address(p[-1]))
    PilaTipos.append(search_type(p[-1]))

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

def p_saveOperadorIgual_np(p):
    '''saveOperadorIgual_np : empty'''
    global current_oper_cuadruplo
    current_oper_cuadruplo = p[-1]
    POper.append(current_oper_cuadruplo)

#def p_pushFondoFalso_np(p):
#    '''pushFondoFalso_np : empty'''
#    POper.append('(')

#def p_popFondoFalso_np(p):
#    '''popFondoFalso_np : empty'''
#    global POper
#    top = POper.pop()
#    if top != '(':
#        print("ERROR Fondo Falso")

def p_gotoMain_np(p):
    '''gotoMain_np : empty'''
    cuadruplo.addGotoMain()

def p_fillMain_np(p):
    '''fillMain_np : empty'''
    cuadruplo.fillMain(0)

#def p_mainJump_np(p):
#    '''mainJump_np : empty'''

def p_multiDiv_np(p):
    '''multiDiv_np : empty'''
    global right_operand, right_type, left_operand, left_type, operador, result_type, result, current_var_type, current_var_scope
    if len(POper) > 0:
        if (POper[-1] == '*' or  POper[-1] == '/'):
            right_operand = PilaO.pop()
            right_type = PilaTipos.pop()
            left_operand = PilaO.pop()
            left_type = PilaTipos.pop()
            operador = POper.pop()
            result_type = cuboS.type_cube(left_type, right_type, operador)
            if result_type != 'err':
                current_var_type = result_type
                current_var_scope = 'funcion'
                result = asignar_direccion_memoria()
                cuadruplo.addQuadruple(operador, left_operand, right_operand, result)
                PilaTipos.append(result_type)
                PilaO.append(result)
            #print(left_operand, left_type, right_operand, right_type, operador)

def p_plusMinus_np(p):
    '''plusMinus_np : empty'''
    global right_operand, right_type, left_operand, left_type, operador, result_type, result, current_var_type, current_var_scope
    if len(POper) > 0:
        if (POper[-1] == '+' or POper[-1] == '-'):
            right_operand = PilaO.pop()
            right_type = PilaTipos.pop()
            left_operand = PilaO.pop()
            left_type = PilaTipos.pop()
            operador = POper.pop()
            result_type = cuboS.type_cube(left_type, right_type, operador)
            if result_type != 'err':
                current_var_type = result_type
                current_var_scope = 'funcion'
                result = asignar_direccion_memoria()
                cuadruplo.addQuadruple(operador, left_operand, right_operand, result)
                PilaTipos.append(result_type)
                PilaO.append(result)
            #print(left_operand, left_type, right_operand, right_type, operador)

def p_relationalOp_np(p):
    '''relationalOp_np : empty'''
    global right_operand, right_type, left_operand, left_type, operador, result_type, result, current_var_type, current_var_scope
    if len(POper) > 0:
        if POper[-1] == '<' or POper[-1] == '>' or POper[-1] == 'equal' or POper[-1] == 'not':
            right_operand = PilaO.pop()
            right_type = PilaTipos.pop()
            left_operand = PilaO.pop()
            left_type = PilaTipos.pop()
            operador = POper.pop()
            result_type = cuboS.type_cube(left_type, right_type, operador)
            if result_type != 'err':
                current_var_type = result_type
                current_var_scope = 'funcion'
                result = asignar_direccion_memoria()
                cuadruplo.addQuadruple(operador, left_operand, right_operand, result)
                PilaTipos.append(result_type)
                PilaO.append(result)
            #print(left_operand, left_type, right_operand, right_type, operador)

def p_and_np(p):
    '''and_np : empty'''
    global right_operand, right_type, left_operand, left_type, operador, result_type, result, current_var_type, current_var_scope
    if len(POper) > 0:
        if POper[-1] == 'and':
            right_operand = PilaO.pop()
            right_type = PilaTipos.pop()
            left_operand = PilaO.pop()
            left_type = PilaTipos.pop()
            operador = POper.pop()
            result_type = cuboS.type_cube(left_type, right_type, operador)
            if result_type != 'err':
                current_var_type = result_type
                current_var_scope = 'funcion'
                result = asignar_direccion_memoria()
                cuadruplo.addQuadruple(operador, left_operand, right_operand, result)
                PilaTipos.append(result_type)
                PilaO.append(result)
            #print(left_operand, left_type, right_operand, right_type, operador)

def p_or_np(p):
    '''or_np : empty'''
    global right_operand, right_type, left_operand, left_type, operador, result_type, result, current_var_type, current_var_scope
    if len(POper) > 0:
        if POper[-1] == 'or':
            right_operand = PilaO.pop()
            right_type = PilaTipos.pop()
            left_operand = PilaO.pop()
            left_type = PilaTipos.pop()
            operador = POper.pop()
            result_type = cuboS.type_cube(left_type, right_type, operador)
            if result_type != 'err':
                current_var_type = result_type
                current_var_scope = 'funcion'
                result = asignar_direccion_memoria()
                cuadruplo.addQuadruple(operador, left_operand, right_operand, result)
                PilaTipos.append(result_type)
                PilaO.append(result)
            #print(left_operand, left_type, right_operand, right_type, operador)

def p_igual_np(p):
    '''igual_np : empty'''
    global right_operand, right_type, left_operand, left_type, operador, result_type, result, current_var_type, current_var_scope
    if len(POper) > 0:
        if POper[-1] == '=':
            right_operand = PilaO.pop()
            right_type = PilaTipos.pop()
            left_operand = PilaO.pop()
            left_type = PilaTipos.pop()
            operador = POper.pop()
            result_type = cuboS.type_cube(left_type, right_type, operador)
            if result_type != False:
                cuadruplo.addQuadrupleIgual(operador, left_operand, right_operand)
            #print(left_operand, left_type, right_operand, right_type, operador)


######################### IF #####################
def p_ifQuad_np(p):
    '''ifQuad_np : empty'''
    global result_type
    result_type = PilaTipos.pop()
    if (result_type != 'bool'):
        print('Type-mismatch')
    else:
        result = PilaO.pop()
        cuadruplo.addQuadIf(result)
        PSaltos.append(cuadruplo.cont - 1)

def p_fillIfQuad_np(p):
    '''fillIfQuad_np : empty'''
    end = PSaltos.pop()
    cuadruplo.fill(end-1)

def p_elseQuad_np(p):
    '''elseQuad_np : empty'''
    false = PSaltos.pop()
    cuadruplo.addQuadGOTO()
    PSaltos.append(cuadruplo.cont - 1)
    cuadruplo.fill(false-1)


###################### WHILE ##########################
def p_whileQuadSaltos_np(p):
    '''whileQuadSaltos_np : empty'''
    PSaltos.append(cuadruplo.cont)

def p_whileQuad_np(p):
    '''whileQuad_np : empty'''
    global result_type
    result_type = PilaTipos.pop()
    if (result_type != 'bool'):
        print('Type-mismatch')
    else:
        result = PilaO.pop()
        cuadruplo.addQuadGotoF(result)
        PSaltos.append(cuadruplo.cont - 1)

def p_fillWhileQuad_np(p):
    '''fillWhileQuad_np : empty'''
    end = PSaltos.pop()
    retorno = PSaltos.pop()
    cuadruplo.addQuadWhile(retorno)
    cuadruplo.fill(end-1)

###################### FOR #################
def p_validarIdFor_np(p):
    '''validarIdFor_np : empty'''
    if (varsTable.find_type(p[-1]) != 'int'):
        print("ERROR: Type mismatch")
    else:
        PilaO.append(varsTable.find_address(p[-1]))
        PilaTipos.append(varsTable.find_type(p[-1]))

def p_forInitialExp_np(p):
    '''forInitialExp_np : empty'''
    global vControl, exp
    exp_type = PilaTipos.pop()
    if (exp_type != 'int'):
        print("ERROR: Type mismatch")
    else:
        exp = PilaO.pop()
        vControl = PilaO[-1]
        control_type = PilaTipos[-1]
        tipo_res = cuboS.type_cube(control_type, exp_type, '=')
        if (tipo_res != True):
            print("ERROR: Type mismatch")
        else:
            cuadruplo.addQuadrupleIgual('=', vControl, exp)
            cuadruplo.addQuadrupleIgual('=', 'VControl', vControl)

def p_forResultExp_np(p):
    '''forResultExp_np : empty'''
    global current_var_type, result_type, vControl, current_var_scope, result, exp
    exp_type = PilaTipos.pop()
    if (exp_type != 'int'):
        print("ERROR: Type mismatch")
    else:
        exp = PilaO.pop()
        cuadruplo.addQuadrupleIgual('=', 'VFinal', exp)
        current_var_type = 'bool'
        current_var_scope = 'funcion'
        result = asignar_direccion_memoria()
        cuadruplo.addQuadruple('<', 'VControl', 'VFinal', result)
        PSaltos.append(cuadruplo.cont-1)
        cuadruplo.addQuadGotoF(result)
        PSaltos.append(cuadruplo.cont-1)

def p_endFor_np(p):
    '''endFor_np : empty'''
    print(PilaO)
    print(PilaTipos)
    global result_type, current_var_scope, current_var_type, result
    current_var_type = 'int'
    current_var_scope = 'funcion'
    result = asignar_direccion_memoria()
    cuadruplo.addQuadruple('+', 'VControl', 1, result)
    cuadruplo.addQuadrupleIgual('=', 'VControl', result)
    cuadruplo.addQuadrupleIgual('=', PilaO[-1], result)
    FIN = PSaltos.pop()
    print(FIN)
    RET = PSaltos.pop()
    cuadruplo.addQuadruple('GOTO', ' ', ' ', RET)
    cuadruplo.fill(FIN-1)
    PilaO.pop()
    PilaTipos.pop()

################## READ #################
def p_readQuad_np(p):
    '''readQuad_np : empty'''
    variable = PilaO.pop()
    PilaTipos.pop()
    cuadruplo.addQuadRead(variable)

################## WRITE ###############
def p_pushLetrero_np(p):
    '''pushLetrero_np : empty'''
    PilaO.append(p[-1])
    PilaTipos.append("string")


def p_writeQuad_np(p):
    '''writeQuad_np : empty'''
    variable = PilaO.pop()
    PilaTipos.pop()
    cuadruplo.addQuadWrite(variable)

########################## Memoria virtual #################################
def asignar_direccion_memoria():
    global current_var_type, current_var_scope, dir_global_bool, dir_global_char, dir_global_float, dir_global_int, dir_local_clase_bool, dir_local_clase_char, dir_local_clase_float, dir_local_clase_int, dir_local_funcion_bool, dir_local_funcion_char, dir_local_funcion_float, dir_local_funcion_int
    aux = 0
    if current_var_scope == 'global':
        if current_var_type == 'int':
            if dir_global_int > 499:
                print('ERROR: Se excedió el máximo de variables enteras globales')
            aux = dir_global_int
            dir_global_int += 1
        elif current_var_type == 'float':
            if dir_global_float > 999:
                print('ERROR: Se excedió el máximo de variables float globales')
            aux = dir_global_float
            dir_global_float += 1
        elif current_var_type == 'char':
            if dir_global_char > 1499:
                print('ERROR: Se excedió el máximo de variables char globales')
            aux = dir_global_char
            dir_global_char += 1
        elif current_var_type == 'bool':
            if dir_global_bool > 1999:
                print('ERROR: Se excedió el máximo de variables bool globales')
            aux = dir_global_bool
            dir_global_bool += 1

    elif current_var_scope == 'funcion':
        if current_var_type == 'int':
            if dir_local_funcion_int > 2499:
                print('ERROR: Se excedió el máximo de variables enteras locales funcion')
            aux = dir_local_funcion_int
            dir_local_funcion_int += 1
        elif current_var_type == 'float':
            if dir_local_funcion_float > 2999:
                print('ERROR: Se excedió el máximo de variables enteras locales funcion')
            aux = dir_local_funcion_float
            dir_local_funcion_float += 1
        elif current_var_type == 'char':
            if dir_local_funcion_char > 3499:
                print('ERROR: Se excedió el máximo de variables enteras locales funcion')
            aux = dir_local_funcion_char
            dir_local_funcion_char += 1
        elif current_var_type == 'bool':
            if dir_local_funcion_bool > 3999:
                print('ERROR: Se excedió el máximo de variables enteras locales funcion')
            aux = dir_local_funcion_bool
            dir_local_funcion_bool += 1

    else:
        if current_var_type == 'int':
            if dir_local_clase_int > 4499:
                print('ERROR: Se excedió el máximo de variables enteras locales clase')
            aux = dir_local_clase_int
            dir_local_clase_int += 1
        elif current_var_type == 'float':
            if dir_local_clase_float > 4999:
                print('ERROR: Se excedió el máximo de variables enteras locales clase')
            aux = dir_local_clase_float
            dir_local_clase_float += 1
        elif current_var_type == 'char':
            if dir_local_clase_char > 5499:
                print('ERROR: Se excedió el máximo de variables enteras locales clase')
            aux = dir_local_clase_char
            dir_local_clase_char += 1
        elif current_var_type == 'bool':
            if dir_local_clase_bool > 5999:
                print('ERROR: Se excedió el máximo de variables enteras locales clase')
            aux = dir_local_clase_bool
            dir_local_clase_bool += 1
    return aux

def asignar_direccion_memoriaCtes():
    global cte_type, dir_constante_int, dir_constante_float, dir_constante_char
    aux = 0
    if cte_type == 'int':
        if dir_constante_int > 6499:
            print('ERROR: Se excedió el máximo de constantes int')
        aux = dir_constante_int
        dir_constante_int += 1
    elif cte_type == 'float':
        if dir_constante_float > 6999:
            print('ERROR: Se excedió el máximo de constantes float')
        aux = dir_constante_float
        dir_constante_float += 1
    elif cte_type == 'char':
        if dir_constante_char > 7499:
            print('ERROR: Se excedió el máximo de constantes char')
        aux = dir_constante_char
        dir_constante_char += 1
    return aux

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

#print("Tabla de clases")
#print(claseTable.toString())

#print("Tabla de Funciones")
#print(functionsTable.toString())

print("Tabla de constantes")
print(constantsTable.toString())

cuadruplo.printQuads()

print(PilaO)
print(POper)
print(PilaTipos)