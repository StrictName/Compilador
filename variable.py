# Variable Table

#The key is the name od the variable and their atributes are scope and type
class Var:
    def __init__(self, type, scope, direccion, direccion_funcion):
        self.type = type
        self.scope = scope
        self.direccion = direccion
        self.direccion_funcion = direccion_funcion
        