import linecache

i = 1
cont = 1
ctes = {}
dict_func = {}
global_mem = {}
local_mem = {}
VControl = 0
cont_params = 0
cont_params_int = 0
cont_params_float = 0
cont_params_char = 0
cont_params_bool = 0
pile_funcs = []
pile_returns = []

def convert_type(address, valor):
    val = None
    #Globales
    if address >= 1 and address < 1000:
        val = int(valor)
    elif address >= 1000 and address < 2000:
        val = float(valor)
    elif address >= 2000 and address < 3000:
        val = str(valor)
    elif address >= 3000 and address < 4000:
        val = int(valor)

    #Locales
    elif address >= 4000 and address < 5000:
        val = int(valor)
    elif address >= 5000 and address < 6000:
        val = float(valor)
    elif address >= 6000 and address < 7000:
        val = str(valor)
    elif address >= 7000 and address < 8000:
        val = int(valor)
    
    #Constantes
    elif address >= 13000 and address < 14000:
        val = int(valor)
    elif address >= 14000 and address < 15000:
        val = float(valor)
    elif address >= 15000 and address < 16000:
        val = str(valor)

    return val

def operaciones_arit(oper, valueIzq, valueDer):
    result = None
    if oper == '+':
        result = valueIzq + valueDer
    elif oper == '-':
        result = valueIzq - valueDer
    elif oper == '*':
        result = valueIzq * valueDer
    elif oper == '/':
        result = valueIzq / valueDer

    elif oper == '>':
        if valueIzq > valueDer:
            return 1
        else:
            return 0
    elif oper == '<':
        if valueIzq < valueDer:
            return 1
        else:
            return 0
    elif oper == 'igual':
        if valueIzq == valueDer:
            return 1
        else:
            return 0
    elif oper == 'not':
        if valueIzq != valueDer:
            return 1
        else:
            return 0
    elif oper == 'and':
        if valueIzq == 1 and valueDer == 1:
            return 1
        else:
            return 0
    elif oper == 'or':
        if valueIzq == 1 or valueDer == 1:
            return 1
        else:
            return 0

    return result

def search_dict(address):
    if address in ctes:
        return ctes[address]
    elif address in global_mem:
        return global_mem[address]
    elif address in local_mem:
        return local_mem[address]
    elif address in local_mem[pile_funcs[-1]]:
        return local_mem[pile_funcs[-1]][address]

def add_value(address, val):
    if address > 0 and address < 4000:
        global_mem[address] = val
    elif address > 3999 and address < 8000:
        if address in local_mem:
            local_mem[address] = val
        else:
            local_mem[pile_funcs[-1]][address] = val

while True:
    if linecache.getline("dataVirtualMachine.txt", i) != '#\n':
        linea = linecache.getline("dataVirtualMachine.txt", i)
        if linea == "":
            #print(ctes, global_mem, local_mem)
            exit()

        quad = linea.split(",")

        if cont == 1:
            dict_func[quad[1]] = quad
        
        if cont == 2:
            value = convert_type(int(quad[0]), quad[1])
            ctes[int(quad[0])] = value

        if cont == 3:
            if quad[1] == '=':
                value_dict = search_dict(int(quad[2]))
                if str(quad[4]) == 'VControl\n':
                    local_mem['VControl'] = value_dict
                elif str(quad[4]) == 'VFinal\n':
                    local_mem['VFinal'] = value_dict
                else:
                    value = convert_type(int(quad[4]), value_dict)
                    add_value(int(quad[4]), value)

            elif quad[1] == '-':
                value_oper1 = search_dict(int(quad[2]))
                value_oper2 = search_dict(int(quad[3]))
                value = convert_type(int(quad[4]), operaciones_arit('-', value_oper1, value_oper2))
                add_value(int(quad[4]), value)

            elif quad[1] == '+':
                if quad[2] == 'VControl':
                    value_oper1 = search_dict(quad[2])
                    value_oper2 = int(1)
                else:
                    value_oper1 = search_dict(int(quad[2]))
                    value_oper2 = search_dict(int(quad[3]))
                value = convert_type(int(quad[4]), operaciones_arit('+', value_oper1, value_oper2))
                add_value(int(quad[4]), value)

            elif quad[1] == '*':
                value_oper1 = search_dict(int(quad[2]))
                value_oper2 = search_dict(int(quad[3]))
                value = convert_type(int(quad[4]), operaciones_arit('*', value_oper1, value_oper2))
                add_value(int(quad[4]), value)

            elif quad[1] == '/':
                value_oper1 = search_dict(int(quad[2]))
                value_oper2 = search_dict(int(quad[3]))
                value = convert_type(int(quad[4]), operaciones_arit('/', value_oper1, value_oper2))
                add_value(int(quad[4]), value)
                
            elif quad[1] == '>':
                value_oper1 = search_dict(int(quad[2]))
                value_oper2 = search_dict(int(quad[3]))
                value = convert_type(int(quad[4]), operaciones_arit('>', value_oper1, value_oper2))
                add_value(int(quad[4]), value)

            elif quad[1] == '<':
                if quad[2] == 'VControl' and quad[3] == 'VFinal':
                    value_oper1 = search_dict(quad[2])
                    value_oper2 = search_dict(quad[3])
                else:
                    value_oper1 = search_dict(int(quad[2]))
                    value_oper2 = search_dict(int(quad[3]))
                value = convert_type(int(quad[4]), operaciones_arit('<', value_oper1, value_oper2))
                add_value(int(quad[4]), value)

            elif quad[1] == 'igual':
                value_oper1 = search_dict(int(quad[2]))
                value_oper2 = search_dict(int(quad[3]))
                value = convert_type(int(quad[4]), operaciones_arit('igual', value_oper1, value_oper2))
                add_value(int(quad[4]), value)

            elif quad[1] == 'not':
                value_oper1 = search_dict(int(quad[2]))
                value_oper2 = search_dict(int(quad[3]))
                value = convert_type(int(quad[4]), operaciones_arit('not', value_oper1, value_oper2))
                add_value(int(quad[4]), value)

            elif quad[1] == 'and':
                value_oper1 = search_dict(int(quad[2]))
                value_oper2 = search_dict(int(quad[3]))
                value = convert_type(int(quad[4]), operaciones_arit('and', value_oper1, value_oper2))
                add_value(int(quad[4]), value)
            
            elif quad[1] == 'or':
                value_oper1 = search_dict(int(quad[2]))
                value_oper2 = search_dict(int(quad[3]))
                value = convert_type(int(quad[4]), operaciones_arit('or', value_oper1, value_oper2))
                add_value(int(quad[4]), value)
            
            elif quad[1] == 'WRITE':
                if quad[4][0] == '"':
                    print(quad[4])
                else:
                    value = convert_type(int(quad[4]), search_dict(int(quad[4])))
                    print(value)

            elif quad[1] == 'READ':
                value = input()
                newval = convert_type(int(quad[4]), value)
                add_value(int(quad[4]), newval)

            elif quad[1] == 'GOTO':
                if int(quad[4]) > int(quad[0]):
                    salto_linea = int(quad[4]) - int(quad[0]) + i - 1
                    i = salto_linea
                else:
                    salto_linea = i - int(quad[0]) + int(quad[4]) - 1
                    i = salto_linea

            elif quad[1] == 'GOTOF':
                buleano = search_dict(int(quad[2]))
                if buleano == 0:
                    salto_linea = int(quad[4]) - int(quad[0]) + i - 1
                    i = salto_linea
            
            elif quad[1] == 'ERA':
                pile_funcs.append(quad[2])
                cont_params = 0
                cont_params_int = 0
                cont_params_float = 0
                cont_params_char = 0
                cont_params_bool = 0
                cant_int = dict_func[quad[2]][4]
                cant_float = dict_func[quad[2]][5]
                cant_char = dict_func[quad[2]][6]
                cant_bool = dict_func[quad[2]][7]
                
                local_mem[quad[2]] = {}
                for s in range(int(cant_int)):
                    local_mem[quad[2]][4000 + s] = ''
                for s in range(int(cant_float)):
                    local_mem[quad[2]][5000 + s] = ''
                for s in range(int(cant_char)):
                    local_mem[quad[2]][6000 + s] = ''
                for s in range(int(cant_bool)):
                    local_mem[quad[2]][7000 + s] = ''

                print(pile_funcs)

            elif quad[1] == 'PARAMETER':
                current_func = pile_funcs[-1]
                val_param = search_dict(int(quad[2]))
                type_param = dict_func[current_func][8 + cont_params]
                if type_param == 'int':
                    local_mem[current_func][4000 + cont_params_int] = val_param
                    cont_params_int += 1
                elif type_param == 'float':
                    local_mem[current_func][5000 + cont_params_float] = val_param
                    cont_params_float += 1
                elif type_param == 'char':
                    local_mem[current_func][6000 + cont_params_char] = val_param
                    cont_params_char += 1
                elif type_param == 'bool':
                    local_mem[current_func][7000 + cont_params_bool] = val_param
                    cont_params_bool += 1

                cont_params += 1

            elif quad[1] == 'GOSUB':
                pile_returns.append(i)
                if int(quad[4]) > int(quad[0]):
                    salto_linea = int(quad[4]) - int(quad[0]) + i - 1
                    i = salto_linea
                else:
                    salto_linea = i - int(quad[0]) + int(quad[4]) - 1
                    i = salto_linea
                #MANDAR A DORMIR A LA MEMORIA EXISTENTE

            elif quad[1] == 'ENDFunc':
                i = pile_returns[-1]
                #pile_funcs.pop()

                
            print(ctes, global_mem, local_mem)
            print(quad)

        #print(ctes, global_mem, local_mem)

    else:
        cont += 1

    i += 1
