import linecache

i = 1
cont = 1
ctes = {}
global_mem = {}
temp_mem = {}
VControl = 0

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
    elif address in temp_mem:
        return temp_mem[address]

def add_value(address, val):
    if address > 0 and address < 4000:
        global_mem[address] = val
    elif address > 3999 and address < 8000:
        temp_mem[address] = val


while True:
    if linecache.getline("dataVirtualMachine.txt", i) != '#\n':
        linea = linecache.getline("dataVirtualMachine.txt", i)
        if linea == "":
            print(ctes, global_mem, temp_mem)
            exit()

        quad = linea.split(",")

        if cont == 2:
            value = convert_type(int(quad[0]), quad[1])
            ctes[int(quad[0])] = value

        if cont == 3:
            if quad[1] == '=':
                value_dict = search_dict(int(quad[2]))
                if str(quad[4]) == 'VControl\n' or str(quad[4]) == 'VFinal\n':
                    temp_mem[quad[4]] = value_dict
                    print(temp_mem[quad[4]])
                else:
                    value = convert_type(int(quad[4]), value_dict)
                    add_value(int(quad[4]), value)


            elif quad[1] == '-':
                value_oper1 = search_dict(int(quad[2]))
                value_oper2 = search_dict(int(quad[3]))
                value = convert_type(int(quad[4]), operaciones_arit('-', value_oper1, value_oper2))
                add_value(int(quad[4]), value)

            elif quad[1] == '+':
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

            




            
    else:
        cont += 1

    i += 1
