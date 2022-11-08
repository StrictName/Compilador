from funcion import Function
from varTable import varTable

class funcTable:
    def __init__(self):
        self.table = {}

    def add(self, name, type, address, inicio_cuad, tam, parameters):
        currentFunc = Function(type, address, inicio_cuad, tam, parameters)
        if name in self.table:
            print("The function is already declarated")
        else:
            self.table[name] = currentFunc
            print(f"Function {name} saved successfully")

    def search(self, name):
        if name in self.table:
            return self.table[name]
        else:
            return "Function undeclared"

    def find_address(self, name):
        if name in self.table:
            return self.table[name].address

    def find_parameters(self, name):
        if name in self.table:
            return self.table[name].parameters

    def find_param(self, name, num):
        if name in self.table:
            return self.table[name].parameters[num]

    def toString(self):
        for key in self.table:
            print(f"{key}: {self.table[key].type}, {self.table[key].address}, {self.table[key].inicio_cuad}, {self.table[key].tam}")
            print("  Parametros:")
            for parameter in self.table[key].parameters:
                print(f"  {parameter}")