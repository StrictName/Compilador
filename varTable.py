
from variable import Var

class varTable:
    def __init__(self):
        self.table = {}

    def add(self, name, type, scope, direccion, direccion_funcion):
        currentVar = Var(type, scope, direccion, direccion_funcion)
        if name in self.table:
            print(f"The variable {name} already exists")
        else:
            self.table[name] = currentVar
            #print(f"Variable {name} saved successfully, direccion {direccion}")

    def search(self, name):
        if name in self.table:
            return name
        else:
            return "Variable undeclared"

    def find_address(self, name):
        if name in self.table:
            return self.table[name].direccion

    def find_type(self, name):
        if name in self.table:
            return self.table[name].type

    def toString(self):
        for key in self.table:
            print(f"{key}: {self.table[key].type}, {self.table[key].scope}, {self.table[key].direccion}, {self.table[key].direccion_funcion}")

