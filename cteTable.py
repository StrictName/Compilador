from cte import Cte

class cteTable:
    def __init__(self):
        self.table = {}

    def add(self, name, type, direccion):
        currentCte = Cte(name, type)
        self.table[direccion] = currentCte
       #print(f"Constant {name} saved successfully, direction {direccion}")

    def find_address(self, name):
        if name in self.table:
            return self.table[name].direccion

    def find_type(self, name):
        if name in self.table:
            return self.table[name].type

    def toString(self):
        for key in self.table:
            print(f"{key}: {self.table[key].name}, {self.table[key].type}")

    def writeCtes(self, f):
        for key in self.table:
            f.write(f"{key},{self.table[key].name},{self.table[key].type}\n")