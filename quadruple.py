class quadruplesList:
    def __init__(self):
        self.quadsList = []
        self.cont = 0

    def addQuadruple(self, operador, left_operand, right_operand, result):
        cuadruplo = quadruple(operador, left_operand, right_operand, result)
        if operador != '=':
            self.quadsList.append(cuadruplo)
            self.cont += 1
            print(cuadruplo.printQuad())

    def addQuadrupleIgual(self, operador, left_operand, right_operand):
        cuadruplo = quadruple(operador, right_operand, '', left_operand)
        self.quadsList.append(cuadruplo)
        self.cont += 1
        print(cuadruplo.printQuad())



class quadruple:
    def __init__(self, operador, left_operand, right_operand, result):
        self.operador = operador
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result

    def printQuad(self):
        print(f"{self.operador}, {self.left_operand}, {self.right_operand}, {self.result}")
