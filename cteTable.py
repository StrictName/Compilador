from cte import Cte

class cteTable:
    def __init__(self):
        self.table = {}

    def add(self, name, type, direccion):
        currentCte = Cte(type, direccion)
        self.table[name] = currentCte
        print(f"Constant {name} saved successfully, direcion {direccion}")

    def find_address(self, name):
        if name in self.table:
            return self.table[name].direccion

    def find_type(self, name):
        if name in self.table:
            return self.table[name].type

    def toString(self):
        for key in self.table:
            print(f"{key}: {self.table[key].type}, {self.table[key].direccion}")