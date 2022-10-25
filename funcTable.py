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

    def toString(self):
        for key in self.table:
            print(f"{key}: {self.table[key].type}")
            for parameter in self.table[key].parameters:
                print(f"{parameter.id}: {parameter.type}")
            self.table[key].varsTable.toString()
