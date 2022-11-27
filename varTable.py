from variable import Var

class varTable:
    def __init__(self):
        self.table = {}

    def add(self, name, type, scope, direccion, direccion_funcion, dim_nonatomics):
        currentVar = Var(type, scope, direccion, direccion_funcion, dim_nonatomics)
        if name in self.table:
            print(f"The variable {name} already exists")
        else:
            self.table[name] = currentVar
            print(f"Variable {name} saved successfully, direccion {direccion}")

    def search(self, name):
        if name in self.table:
            return name
        else:
            return "Variable undeclared"

    def find_address(self, name):
        if name in self.table:
            return self.table[name].direccion

    def deleteKey(self, name):
        del self.table[name]

    def find_type(self, name):
        if name in self.table:
            return self.table[name].type

    def size_array(self, name):
        if name in self.table:
            print(self.table[name].dim_nonatomics)
            return self.table[name].dim_nonatomics[-1]

    def delete_var(self, name):
        self.table.pop(name)

    def toString(self):
        for key in self.table:
            print(f"{key}: {self.table[key].type}, {self.table[key].scope}, {self.table[key].direccion}, {self.table[key].direccion_funcion}, {self.table[key].dim_nonatomics}")