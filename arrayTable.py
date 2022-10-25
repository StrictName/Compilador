from arreglo import Array

class arrayTable:
    def __init__(self):
        self.table = {}
    
    def add(self, name, type, scope, size, data):
        currentArr = Array(type, scope, size, data)
        if name in self.table:
            print(f"Array {name} already exists")
        else:
            self.table[name] = currentArr
            print(f"Array {name} saved")
    
    def search(self, name):
        if name in self.table:
            return self.table[name], None
        else:
            return None, "Variable undeclared"
    
    def toString(self):
        for key in self.table:
            print(f"{key}: {self.table[key].type}, {self.table[key].scope}, {self.table[key].size}, {self.table[key].data} ")
