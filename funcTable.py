from funcion import Function
from varTable import varTable

class funcTable:
    def __init__(self):
        self.table = {}

    def add(self, name, type, parameters, varsTable):
        currentFunc = Function(type, parameters, varsTable)
        if name in self.table:
            print("The function is already declarated")
        else:
            self.table[name] = currentFunc
            print(f"Function {name} saved successfully")

    def search(self, name):
        if name in self.table:
            return self.table[name], None
        else:
            return None, "Function undeclared"

    