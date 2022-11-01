class SemanticCube:
    def __init__(self):
        self.cube = {
            'int':{
                'int':{
                    '+': 'int',
                    '-': 'int',
                    '/': 'float',
                    '*': 'int',
                    '<': 'bool',
                    '>': 'bool',
                    'and': 'err',
                    'or': 'err',
                    'not': 'bool',
                    'equal': 'bool',
                    '=': True
                    },
                'float':{
                    '+': 'float',
                    '-': 'float',
                    '/': 'float',
                    '*': 'float',
                    '<': 'bool',
                    '>': 'bool',
                    'and': 'err',
                    'or': 'err',
                    'not': 'bool',
                    'equal': 'bool',
                    '=': False
                },
                'bool':{
                    '+': 'err',
                    '-': 'err',
                    '/': 'err',
                    '*': 'err',
                    '<': 'err',
                    '>': 'err',
                    'and': 'err',
                    'or': 'err',
                    'not': 'err',
                    'equal': 'err',
                    '=': False
                },
                'char':{
                    '+': 'err',
                    '-': 'err',
                    '/': 'err',
                    '*': 'err',
                    '<': 'err',
                    '>': 'err',
                    'and': 'err',
                    'or': 'err',
                    'not': 'err',
                    'equal': 'err',
                    '=': False
                }
             },

            'float':{
                'int':{
                    '+': 'float',
                    '-': 'float',
                    '/': 'float',
                    '*': 'float',
                    '<': 'bool',
                    '>': 'bool',
                    'and': 'err',
                    'or': 'err',
                    'not': 'bool',
                    'equal': 'bool',
                    '=': True
                },
                'float':{
                    '+': 'float',
                    '-': 'float',
                    '/': 'float',
                    '*': 'float',
                    '<': 'bool',
                    '>': 'bool',
                    'and': 'err',
                    'or': 'err',
                    'not': 'bool',
                    'equal': 'bool',
                    '=': True
                },
                'bool':{
                    '+': 'err',
                    '-': 'err',
                    '/': 'err',
                    '*': 'err',
                    '<': 'err',
                    '>': 'err',
                    'and': 'err',
                    'or': 'err',
                    'not': 'err',
                    'equal': 'err',
                    '=': False
                },
                'char':{
                    '+': 'err',
                    '-': 'err',
                    '/': 'err',
                    '*': 'err',
                    '<': 'err',
                    '>': 'err',
                    'and': 'err',
                    'or': 'err',
                    'not': 'err',
                    'equal': 'err',
                    '=': False
                }
            },

            'bool':{
                'int':{
                    '+': 'err',
                    '-': 'err',
                    '/': 'err',
                    '*': 'err',
                    '<': 'err',
                    '>': 'err',
                    'and': 'err',
                    'or': 'err',
                    'not': 'err',
                    'equal': 'err',
                    '=': False
                },
                'float':{
                    '+': 'err',
                    '-': 'err',
                    '/': 'err',
                    '*': 'err',
                    '<': 'err',
                    '>': 'err',
                    'and': 'err',
                    'or': 'err',
                    'not': 'err',
                    'equal': 'err',
                    '=': False
                },
                'bool':{
                    '+': 'err',
                    '-': 'err',
                    '/': 'err',
                    '*': 'err',
                    '<': 'err',
                    '>': 'err',
                    'and': 'bool',
                    'or': 'bool',
                    'not': 'bool',
                    'equal': 'bool',
                    '=': True
                },
                'char':{
                    '+': 'err',
                    '-': 'err',
                    '/': 'err',
                    '*': 'err',
                    '<': 'err',
                    '>': 'err',
                    'and': 'err',
                    'or': 'err',
                    'not': 'err',
                    'equal': 'err',
                    '=': False
                }
            },
            'char':{
                'int':{
                    '+': 'err',
                    '-': 'err',
                    '/': 'err',
                    '*': 'err',
                    '<': 'err',
                    '>': 'err',
                    'and': 'err',
                    'or': 'err',
                    'not': 'err',
                    'equal': 'err',
                    '=': False
            },
                'float':{
                    '+': 'err',
                    '-': 'err',
                    '/': 'err',
                    '*': 'err',
                    '<': 'err',
                    '>': 'err',
                    'and': 'err',
                    'or': 'err',
                    'not': 'err',
                    'equal': 'err',
                    '=': False
                },
                'bool':{
                    '+': 'err',
                    '-': 'err',
                    '/': 'err',
                    '*': 'err',
                    '<': 'err',
                    '>': 'err',
                    'and': 'err',
                    'or': 'err',
                    'not': 'err',
                    'equal': 'err',
                    '=': False
                },
                'char':{
                    '+': 'err',
                    '-': 'err',
                    '/': 'err',
                    '*': 'err',
                    '<': 'err',
                    '>': 'err',
                    'and': 'err',
                    'or': 'err',
                    'not': 'bool',
                    'equal': 'bool',
                    '=': True
                }
            }
    }

    def type_cube(self, oper1, oper2, operador):
        if oper1 in self.cube and oper2 in self.cube[oper1] and operador in self.cube[oper1][oper2]:
            return self.cube[oper1][oper2][operador]
        else: return "Type mismatch"