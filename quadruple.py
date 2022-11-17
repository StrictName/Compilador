class quadruplesList:
    def __init__(self):
        self.quadsList = []
        self.cont = 1

    def addQuadruple(self, operador, left_operand, right_operand, result):
        if operador != '=':
            cuadruplo = quadruple(self.cont, operador, left_operand, right_operand, result)
            self.quadsList.append(cuadruplo)
            self.cont += 1
            #print("contador", self.cont)
            

    def addQuadrupleIgual(self, operador, left_operand, right_operand):
        cuadruplo = quadruple(self.cont, operador, right_operand, -1, left_operand)
        self.quadsList.append(cuadruplo)
        self.cont += 1
        #print(cuadruplo.printQuad())

    def addGotoMain(self):
        cuadruplo = quadruple(self.cont, 'GOTO', -1, -1, 'main')
        self.quadsList.append(cuadruplo)
        self.cont += 1
        #print(cuadruplo.printQuad())

    def addQuadIf(self, result):
        cuadruplo = quadruple(self.cont,'GotoF', result, -1, -1)
        self.quadsList.append(cuadruplo)
        self.cont += 1
        #print(cuadruplo.printQuad())

    def addQuadGOTO(self):
        cuadruplo = quadruple(self.cont, 'GOTO', -1, -1, -1)
        self.quadsList.append(cuadruplo)
        self.cont += 1

    def fill(self, end):
        self.quadsList[end].result = self.cont

    def fillMain(self, end):
        self.quadsList[end].result = self.cont
    
    def addQuadGotoF(self, result):
        cuadruplo = quadruple(self.cont, 'GOTOF', result, -1, -1)
        self.quadsList.append(cuadruplo)
        self.cont += 1
    
    def addQuadWhile(self, retorno):
        cuadruplo = quadruple(self.cont, 'GOTO', -1, -1, retorno)
        self.quadsList.append(cuadruplo)
        self.cont += 1

    def printQuads(self):
        for i in self.quadsList:
            i.printQuad()

    def writeQuads(self, f):
        for i in self.quadsList:
            i.writeQuad(f)
            f.write('\n')
    
    def addQuadRead(self, variable):
        cuadruplo = quadruple(self.cont,'READ', -1, -1, variable)
        self.quadsList.append(cuadruplo)
        self.cont += 1

    def addQuadWrite(self, variable):
        cuadruplo = quadruple(self.cont,'WRITE', -1, -1, variable)
        self.quadsList.append(cuadruplo)
        self.cont += 1


class quadruple:
    def __init__(self, contador, operador, left_operand, right_operand, result):
        self.contador = contador
        self.operador = operador
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result

    def printQuad(self):
        print(f"{self.contador},{self.operador},{self.left_operand}, {self.right_operand}, {self.result}")

    def writeQuad(self, f):
        f.write(f"{self.contador},{self.operador},{self.left_operand},{self.right_operand},{self.result}")
