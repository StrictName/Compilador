from funcion import Function
from varTable import varTable

class funcTable:
    def __init__(self):
        self.table = {}

    def add(self, name, type, parameters):
        currentFunc = Function(type, parameters)
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

    def toString(self):
        for key in self.table:
            print(f"{key}: {self.table[key].type}")
            print("  Parametros:")
            for parameter in self.table[key].parameters:
                print(f"  {parameter.name}: {parameter.type}")