class varTable:
    def __init__(self):
        self.tabla = {
            0 : {
                "bloque_codigo" : "program", "nombre" : "proyectocompilador", "tipo" : "program", "vars" : {}
            }
        }

    def agregaFunc(self, num, bloque_codigo, nombre, tipo):
        self.tabla[num] = {}
        self.tabla[num]["bloque_codigo"] = bloque_codigo
        self.tabla[num]["nombre"] = nombre
        self.tabla[num]["tipo"] = tipo
        self.tabla[num]["vars"] = {}

    