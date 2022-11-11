program_name = open("dataVirtualMachine.txt", "r")
dict_funciones=[]
dict_cuadruplos=[]
dict_constantes=[]
cont_func = 0
data_num = 1

data = ''
virtual_dir = ''
for line in program_name:
    for ch in line:
        if ch != ":" and ch != "," and cont_func == 0 and ch != '\n':
            data = data + ch
            #if data_num == 1:
                #virtual_dir = virtual_dir + ch
            print(data)
        if (ch == ":" or ch == ",") and cont_func == 0:
            #if ch == ":":
            dict_funciones.append(data)
                #data_num += 1
            data = ''
        elif ch == '#':
            cont_func += 1



print (dict_funciones)