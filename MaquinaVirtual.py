import linecache

i = 1
cont = 1
ctes = {}
global_mem = {}
temp_mem = {}

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
    
    #Constante
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
    elif oper == '=':
        valueDer = valueIzq
        result = valueDer

    return result

def search_dict(address):
    if address in ctes:
        return ctes[address]
    elif address in global_mem:
        return global_mem[address]
    elif address in temp_mem:
        return temp_mem[address]


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
                if int(quad[4]) > 0 and int(quad[4]) < 4000:
                    value_dict = search_dict(int(quad[2]))
                    value = convert_type(int(quad[4]), value_dict)
                    global_mem[int(quad[4])] = value

                elif int(quad[4]) > 3999 and int(quad[4]) < 8000:
                    value_dict = search_dict(int(quad[2]))
                    value = convert_type(int(quad[4]), value_dict)
                    temp_mem[int(quad[4])] = value

            elif quad[1] == '+':
                if int(quad[4]) > 0 and int(quad[4]) < 4000:
                    value_oper1 = search_dict(int(quad[2]))
                    value_oper2 = search_dict(int(quad[3]))
                    value = convert_type(int(quad[4]), operaciones_arit('+', value_oper1, value_oper2))
                    global_mem[int(quad[4])] = value
                elif int(quad[4]) > 3999 and int(quad[4]) < 8000:
                    value_oper1 = search_dict(int(quad[2]))
                    value_oper2 = search_dict(int(quad[3]))
                    value = convert_type(int(quad[4]), operaciones_arit('+', value_oper1, value_oper2))
                    temp_mem[int(quad[4])] = value

            elif quad[1] == '*':
                if int(quad[4]) > 0 and int(quad[4]) < 4000:
                    value_oper1 = search_dict(int(quad[2]))
                    value_oper2 = search_dict(int(quad[3]))
                    value = convert_type(int(quad[4]), operaciones_arit('*', value_oper1, value_oper2))
                    global_mem[int(quad[4])] = value
                elif int(quad[4]) > 3999 and int(quad[4]) < 8000:
                    value_oper1 = search_dict(int(quad[2]))
                    value_oper2 = search_dict(int(quad[3]))
                    value = convert_type(int(quad[4]), operaciones_arit('*', value_oper1, value_oper2))
                    temp_mem[int(quad[4])] = value

            elif quad[1] == '/':
                if int(quad[4]) > 0 and int(quad[4]) < 4000:
                    value_oper1 = search_dict(int(quad[2]))
                    value_oper2 = search_dict(int(quad[3]))
                    value = convert_type(int(quad[4]), operaciones_arit('/', value_oper1, value_oper2))
                    global_mem[int(quad[4])] = value
                elif int(quad[4]) > 3999 and int(quad[4]) < 8000:
                    value_oper1 = search_dict(int(quad[2]))
                    value_oper2 = search_dict(int(quad[3]))
                    value = convert_type(int(quad[4]), operaciones_arit('/', value_oper1, value_oper2))
                    temp_mem[int(quad[4])] = value
                

    else:
        cont += 1

    i += 1
