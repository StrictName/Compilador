#class varTable:
""" def __init__(self):
        self.tabla = {
            0 : {
                "bloque_codigo" : "program", "nombre" : "proyectocompilador", "tipo" : "program", "vars" : {}
            }
        }

    def agregaFila(self, num, bloque_codigo, nombre, tipo):
        self.tabla[num] = {}
        self.tabla[num]["bloque_codigo"] = bloque_codigo
        self.tabla[num]["nombre"] = nombre
        self.tabla[num]["tipo"] = tipo
        self.tabla[num]["vars"] = {}
"""


#Function Directory 
from tkinter.messagebox import NO
from variable import Var

class varTable:
    def __init__(self):
        self.table = {}

    def add(self, name, type, scope):
        currentVar = Var(type, scope)
        if name in self.table:
            print("The variable already exists")
        else:
            self.table[name] = currentVar
            print(f"Variable {name} saved successfully")

    def search(self, name):
        if name in self.table:
            return self.table[name], None
        else:
            return None, "Variable undeclared"

    def toString(self):
        for key in self.table:
            print(f"{key}: {self.table[key].type}, {self.table[key].scope} ")

