from funcion import Function
from varTable import varTable

class funcTable:
    def __init__(self):
        self.table = {}

    def add(self, name, type, address, inicio_cuad, tam, parameters):
        currentFunc = Function(type, address, inicio_cuad, tam, parameters)
        if name in self.table:
            print(f"The function {name} is already declared")
        else:
            self.table[name] = currentFunc
            print(f"Function {name} saved successfully")

    def fillTam(self, name, tam):
        if name in self.table:
            self.table[name].tam = tam

    def search(self, name):
        if name in self.table:
            return self.table[name]
        else:
            return "Function undeclared"

    def find_address(self, name):
        if name in self.table:
            return self.table[name].address

    def return_tam(self, name):
        if name in self.table:
            return self.table[name].tam

    def find_parameters(self, name):
        if name in self.table:
            return self.table[name].parameters

    def find_param(self, name, num):
        if name in self.table:
            return self.table[name].parameters[num]

    def find_initial_quad(self, name):
        if name in self.table:
            return self.table[name].inicio_cuad

    def find_type(self, name):
        if name in self.table:
            return self.table[name].type

    def toString(self):
        for key in self.table:
            print(f"{key}: {self.table[key].type}, {self.table[key].address}, {self.table[key].inicio_cuad}, {self.table[key].tam}")
            print("  Parametros:")
            for parameter in self.table[key].parameters:
                print(f"  {parameter}")

    def writeFile(self, f):
        for key in self.table:
            f.write(f"{self.table[key].address},{key},{self.table[key].type},{self.table[key].inicio_cuad},")
            for varia in self.table[key].tam:
                f.write(f"{varia},")
            for parameter in self.table[key].parameters:
                f.write(f"{parameter},")
            f.write('\n')
