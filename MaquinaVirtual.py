import linecache

i = 1
cont = 1
ctes = {}
global_mem = {}
temp_mem = {}

while True:
    if linecache.getline("dataVirtualMachine.txt", i) != '#\n':
        linea = linecache.getline("dataVirtualMachine.txt", i)
        if linea == "":
            print(ctes, global_mem, temp_mem)
            exit()

        quad = linea.split(",")

        if cont == 2:
            ctes[int(quad[0])] = quad[1]

        if cont == 3:
            if quad[1] == '=':
                if int(quad[4]) > 0 and int(quad[4]) < 4000:
                    if int(quad[2]) in ctes:
                        print('HOLA')
                        value = ctes[int(quad[2])]
                        global_mem[int(quad[4])] = value
                    elif int(quad[2]) in global_mem.keys():
                        value = global_mem[int(quad[2])]
                        global_mem[int(quad[4])] = value
                    elif int(quad[2]) in temp_mem.keys():
                        value = global_mem[int(quad[2])]
                        global_mem[int(quad[4])] = value
                #if int(quad[4]) > 3999 and int(quad[4]) < 12999:
                    #temp_mem[int(quad[4])] = ctes[int(quad[1])]
            if quad[1] == '*':
                if int(quad[4]) > 0 and int(quad[4]) < 3999:
                    print(quad[2])
                    if int(quad[2]) in ctes.keys():
                        oper1 = ctes[int(quad[2])]
                        if int(quad[3]) in ctes.keys():
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem.keys():
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem.keys():
                            oper2 = temp_mem[int(quad[3])]
                        resul = int(oper1) * int(oper2)
                        global_mem[int(quad[4])] = resul
                    elif int(quad[2])in global_mem.keys():
                        oper1 = global_mem[int(quad[2])]
                        if int(quad[3]) in ctes.keys():
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem.keys():
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem.keys():
                            oper2 = temp_mem[int(quad[3])]
                        resul = int(oper1) * int(oper2)
                        global_mem[int(quad[4])] = resul
                    elif int(quad[2]) in temp_mem.keys():
                        oper1 = temp_mem[int(quad[2])]
                        if int(quad[3]) in ctes.keys():
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem.keys():
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem.keys():
                            oper2 = temp_mem[int(quad[3])]
                        resul = int(oper1) * int(oper2)
                        global_mem[int(quad[4])] = resul

            if quad[1] == '+':
                if int(quad[4]) > 0 and int(quad[4]) < 3999:
                    print(quad[2])
                    if int(quad[2]) in ctes.keys():
                        oper1 = ctes[int(quad[2])]
                        if int(quad[3]) in ctes.keys():
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem.keys():
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem.keys():
                            oper2 = temp_mem[int(quad[3])]
                        resul = int(oper1) + int(oper2)
                        global_mem[int(quad[4])] = resul
                    elif int(quad[2]) in global_mem.keys():
                        oper1 = global_mem[int(quad[2])]
                        if int(quad[3]) in ctes.keys():
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem.keys():
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem.keys():
                            oper2 = temp_mem[int(quad[3])]
                        resul = int(oper1) + int(oper2)
                        global_mem[int(quad[4])] = resul
                    elif int(quad[2]) in temp_mem.keys():
                        oper1 = temp_mem[int(quad[2])]
                        if int(quad[3]) in ctes.keys():
                            oper2 = ctes[int(quad[3])]
                        if int(quad[3]) in global_mem.keys():
                            oper2 = global_mem[int(quad[3])]
                        if int(quad[3]) in temp_mem.keys():
                            oper2 = temp_mem[int(quad[3])]
                        resul = int(oper1) + int(oper2)
                        global_mem[int(quad[4])] = resul

    else:
        cont += 1

    i += 1
