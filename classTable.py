from clase import Clase
class classTable:
    def __init__(self):
        self.table = {}

    def add(self, name, type):
        currentVar = Clase(type)
        if name in self.table:
            print(f"The class {name} already exists")
        else:
            self.table[name] = currentVar
            print(f"Class {name} saved successfully")

    def search(self, name):
        if name in self.table:
            return self.table[name], None
        else:
            return None, "Variable undeclared"

    def toString(self):
        for key in self.table:
            print(f"{key}: {self.table[key].type} ")
