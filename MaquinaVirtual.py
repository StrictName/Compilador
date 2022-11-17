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
                    if int(quad[2]) in ctes:
                        value = convert_type(int(quad[4]), ctes[int(quad[2])])
                        global_mem[int(quad[4])] = value
                    elif int(quad[2]) in global_mem:
                        value = convert_type(int(quad[4]), global_mem[int(quad[2])])
                        global_mem[int(quad[4])] = value
                    elif int(quad[2]) in temp_mem:
                        value = convert_type(int(quad[4]), temp_mem[int(quad[2])])
                        global_mem[int(quad[4])] = value
                elif int(quad[4]) > 3999 and int(quad[4]) < 8000:
                    if int(quad[2]) in ctes:
                        value = convert_type(int(quad[4]), ctes[int(quad[2])])
                        temp_mem[int(quad[4])] = value
                    elif int(quad[2]) in global_mem:
                        value = convert_type(int(quad[4]), global_mem[int(quad[2])])
                        temp_mem[int(quad[4])] = value
                    elif int(quad[2]) in temp_mem:
                        value = convert_type(int(quad[4]), temp_mem[int(quad[2])])
                        temp_mem[int(quad[4])] = value

            elif quad[1] == '+':
                if int(quad[4]) > 0 and int(quad[4]) < 4000:
                    if int(quad[2]) in ctes:
                        oper1 = ctes[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        elif int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        elif int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                    value = convert_type(int(quad[4]), operaciones_arit('+', oper1, oper2))
                    global_mem[int(quad[4])] = value
                elif int(quad[4]) > 3999 and int(quad[4]) < 8000:
                    if int(quad[2]) in ctes:
                        oper1 = ctes[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        elif int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        elif int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                    value = convert_type(int(quad[4]), operaciones_arit('+', oper1, oper2))
                    global_mem[int(quad[4])] = value
                


                '''
                if int(quad[4]) > 0 and int(quad[4]) < 3999:
                    if int(quad[2]) in ctes:
                        if int(quad[4]) > 0 and int(quad[4]) < 1000:
                            oper1 = int(ctes[int(quad[2])])
                            if int(quad[3]) in ctes:
                                oper2 = int(ctes[int(quad[3])])
                            if int(quad[3]) in global_mem:
                                oper2 = int(global_mem[int(quad[3])])
                            if int(quad[3]) in temp_mem:
                                oper2 = int(temp_mem[int(quad[3])])
                        else:
                            oper1 = float(ctes[int(quad[2])])
                            if int(quad[3]) in ctes:
                                oper2 = float(ctes[int(quad[3])])
                            if int(quad[3]) in global_mem:
                                oper2 = float(global_mem[int(quad[3])])
                            if int(quad[3]) in temp_mem:
                                oper2 = float(temp_mem[int(quad[3])])
                        resul = oper1 + oper2
                        global_mem[int(quad[4])] = resul

                    elif int(quad[2]) in global_mem:
                        if int(quad[4]) > 0 and int(quad[4]) < 1000:
                            oper1 = int(global_mem[int(quad[2])])
                            if int(quad[3]) in ctes:
                                oper2 = int(ctes[int(quad[3])])
                            if int(quad[3]) in global_mem:
                                oper2 = int(global_mem[int(quad[3])])
                            if int(quad[3]) in temp_mem:
                                oper2 = int(temp_mem[int(quad[3])])
                        else:
                            oper1 = float(global_mem[int(quad[2])])
                            if int(quad[3]) in ctes:
                                oper2 = float(ctes[int(quad[3])])
                            if int(quad[3]) in global_mem:
                                oper2 = float(global_mem[int(quad[3])])
                            if int(quad[3]) in temp_mem:
                                oper2 = float(temp_mem[int(quad[3])])
                        resul = oper1 + oper2
                        global_mem[int(quad[4])] = resul

                    elif int(quad[2]) in temp_mem:
                        if int(quad[4]) > 0 and int(quad[4]) < 1000:
                            oper1 = int(temp_mem[int(quad[2])])
                            if int(quad[3]) in ctes:
                                oper2 = int(ctes[int(quad[3])])
                            if int(quad[3]) in global_mem:
                                oper2 = int(global_mem[int(quad[3])])
                            if int(quad[3]) in temp_mem:
                                oper2 = int(temp_mem[int(quad[3])])

                        else:
                            oper1 = float(temp_mem[int(quad[2])])
                            if int(quad[3]) in ctes:
                                oper2 = float(ctes[int(quad[3])])
                            if int(quad[3]) in global_mem:
                                oper2 = float(global_mem[int(quad[3])])
                            if int(quad[3]) in temp_mem:
                                oper2 = float(temp_mem[int(quad[3])])

                        resul = oper1 + oper2
                        global_mem[int(quad[4])] = resul

                elif int(quad[4]) > 3999 and int(quad[4]) < 13000:
                    if int(quad[2]) in ctes:
                        oper1 = ctes[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                        resul = float(oper1) + float(oper2)
                        temp_mem[int(quad[4])] = resul
                    elif int(quad[2]) in global_mem:
                        oper1 = global_mem[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                        resul = float(oper1) + float(oper2)
                        temp_mem[int(quad[4])] = resul
                    elif int(quad[2]) in temp_mem:
                        oper1 = temp_mem[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                        resul = float(oper1) + float(oper2)
                        temp_mem[int(quad[4])] = resul
                        

            elif quad[1] == '-':
                if int(quad[4]) > 0 and int(quad[4]) < 3999:
                    if int(quad[2]) in ctes:
                        oper1 = ctes[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                        resul = float(oper1) - float(oper2)
                        global_mem[int(quad[4])] = resul
                    elif int(quad[2]) in global_mem:
                        oper1 = global_mem[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                        resul = float(oper1) - float(oper2)
                        global_mem[int(quad[4])] = resul
                    elif int(quad[2]) in temp_mem:
                        oper1 = temp_mem[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                        resul = float(oper1) - float(oper2)
                        global_mem[int(quad[4])] = resul
                elif int(quad[4]) > 3999 and int(quad[4]) < 13000:
                    if int(quad[2]) in ctes:
                        oper1 = ctes[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                        resul = float(oper1) - float(oper2)
                        temp_mem[int(quad[4])] = resul
                    elif int(quad[2]) in global_mem:
                        oper1 = global_mem[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                        resul = float(oper1) - float(oper2)
                        temp_mem[int(quad[4])] = resul
                    elif int(quad[2]) in temp_mem:
                        oper1 = temp_mem[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                        resul = float(oper1) - float(oper2)
                        temp_mem[int(quad[4])] = resul
                        '''

            elif quad[1] == '*':
                if int(quad[4]) > 0 and int(quad[4]) < 3999:
                    if int(quad[2]) in ctes:
                        oper1 = ctes[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                        resul = float(oper1) * float(oper2)
                        global_mem[int(quad[4])] = resul
                    elif int(quad[2])in global_mem:
                        oper1 = global_mem[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                        resul = float(oper1) * float(oper2)
                        global_mem[int(quad[4])] = resul
                    elif int(quad[2]) in temp_mem:
                        oper1 = temp_mem[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                        resul = float(oper1) * float(oper2)
                        global_mem[int(quad[4])] = resul
                elif int(quad[4]) > 3999 and int(quad[4]) < 13000:
                    if int(quad[2]) in ctes:
                        oper1 = ctes[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                        resul = float(oper1) * float(oper2)
                        temp_mem[int(quad[4])] = resul
                    elif int(quad[2])in global_mem:
                        oper1 = global_mem[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                        resul = float(oper1) * float(oper2)
                        temp_mem[int(quad[4])] = resul
                    elif int(quad[2]) in temp_mem:
                        oper1 = temp_mem[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                        resul = float(oper1) * float(oper2)
                        temp_mem[int(quad[4])] = resul

            elif quad[1] == '/':
                if int(quad[4]) > 0 and int(quad[4]) < 3999:
                    if int(quad[2]) in ctes:
                        oper1 = ctes[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                        resul = int(oper1) / int(oper2)
                        global_mem[int(quad[4])] = resul
                    elif int(quad[2])in global_mem:
                        oper1 = global_mem[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                        resul = int(oper1) / int(oper2)
                        global_mem[int(quad[4])] = resul
                    elif int(quad[2]) in temp_mem:
                        oper1 = temp_mem[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                        resul = int(oper1) / int(oper2)
                        global_mem[int(quad[4])] = resul
                elif int(quad[4]) > 3999 and int(quad[4]) < 13000:
                    if int(quad[2]) in ctes:
                        oper1 = ctes[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                        resul = int(oper1) / int(oper2)
                        temp_mem[int(quad[4])] = resul
                    elif int(quad[2])in global_mem:
                        oper1 = global_mem[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                        resul = int(oper1) / int(oper2)
                        temp_mem[int(quad[4])] = resul
                    elif int(quad[2]) in temp_mem:
                        oper1 = temp_mem[int(quad[2])]
                        if int(quad[3]) in ctes:
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem:
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem:
                            oper2 = temp_mem[int(quad[3])]
                        resul = int(oper1) / int(oper2)
                        temp_mem[int(quad[4])] = resul
                

    else:
        cont += 1

    i += 1
