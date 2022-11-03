class quadruplesList:
    def __init__(self):
        self.quadsList = []
        self.cont = 1

    def addQuadruple(self, operador, left_operand, right_operand, result):
        if operador != '=':
            cuadruplo = quadruple(operador, left_operand, right_operand, result)
            self.quadsList.append(cuadruplo)
            self.cont += 1
            #print(cuadruplo.printQuad())

    def addQuadrupleIgual(self, operador, left_operand, right_operand):
        cuadruplo = quadruple(operador, right_operand, '', left_operand)
        self.quadsList.append(cuadruplo)
        self.cont += 1
        #print(cuadruplo.printQuad())

    def addGotoMain(self):
        cuadruplo = quadruple('Goto', 'main', ' ', ' ')
        self.quadsList.append(cuadruplo)
        self.cont += 1
        #print(cuadruplo.printQuad())

    def addQuadIf(self, result):
        cuadruplo = quadruple('GotoF', result, ' ', ' ')
        self.quadsList.append(cuadruplo)
        self.cont += 1
        #print(cuadruplo.printQuad())

    def addQuadElse(self):
        cuadruplo = quadruple('GOTO', ' ', ' ', ' ')
        self.quadsList.append(cuadruplo)
        self.cont += 1

    def fill(self, end):
        self.quadsList[end].result = self.cont
    
    def addQuadWhileF(self, result):
        cuadruplo = quadruple('GotoF', result, ' ', ' ')
        self.quadsList.append(cuadruplo)
        self.cont += 1
    
    def addQuadWhile(self, retorno):
        cuadruplo = quadruple('GOTO', ' ', ' ', retorno)
        self.quadsList.append(cuadruplo)
        self.cont += 1

    def printQuads(self):
        count = 1
        for i in self.quadsList:
            print(f"{count}, {i.printQuad()}")
            count += 1
    
    def addQuadRead(self, variable):
        cuadruplo = quadruple('READ', '  ', '  ', variable)
        self.quadsList.append(cuadruplo)
        self.cont += 1

    def addQuadWrite(self, variable):
        cuadruplo = quadruple('WRITE', ' ', ' ', variable)
        self.quadsList.append(cuadruplo)
        self.cont += 1


class quadruple:
    def __init__(self, operador, left_operand, right_operand, result):
        self.operador = operador
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result

    def printQuad(self):
        print(f"{self.operador}, {self.left_operand}, {self.right_operand}, {self.result}")
