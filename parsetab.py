
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ATTRIBUTE CHAR CLASS COMA CORCHETEDER CORCHETEIZQ CTECH CTEF CTEI DIV DO DOSPUNTOS ELSE EQUAL FLOAT FROM FUNC GREATERTHAN ID IF IGUAL INT LESSTHAN LETRERO LLAVEDER LLAVEIZQ MAIN MAS MENOS METHOD NOT OR PARENTESISDER PARENTESISIZQ POR PRIVATE PROGRAM PROTECTED PUBLIC PUNTO PUNTOCOMA READ RETURN TO VAR VOID WHILE WRITEprograma : PROGRAM ID PUNTOCOMA main\n                | PROGRAM ID PUNTOCOMA clase main\n                | PROGRAM ID PUNTOCOMA clase var main\n                | PROGRAM ID PUNTOCOMA clase var funcion main\n                | PROGRAM ID PUNTOCOMA clase funcion main\n                | PROGRAM ID PUNTOCOMA var main\n                | PROGRAM ID PUNTOCOMA var funcion main\n                | PROGRAM ID PUNTOCOMA funcion mainmain : MAIN PARENTESISIZQ PARENTESISDER LLAVEIZQ LLAVEDER\n            | MAIN PARENTESISIZQ PARENTESISDER LLAVEIZQ estatuto LLAVEDERclase : CLASS ID DOSPUNTOS tipo_clase ID LLAVEIZQ bloque_clase LLAVEDER PUNTOCOMA\n            | CLASS ID DOSPUNTOS tipo_clase ID LLAVEIZQ bloque_clase LLAVEDER PUNTOCOMA clase\n            | CLASS ID DOSPUNTOS tipo_clase ID LLAVEIZQ LLAVEDER PUNTOCOMA\n            | CLASS ID DOSPUNTOS tipo_clase ID LLAVEIZQ LLAVEDER PUNTOCOMA clase\n            | CLASS ID LLAVEIZQ bloque_clase LLAVEDER PUNTOCOMA\n            | CLASS ID LLAVEIZQ bloque_clase LLAVEDER PUNTOCOMA clase\n            | CLASS ID LLAVEIZQ LLAVEDER PUNTOCOMA\n            | CLASS ID LLAVEIZQ LLAVEDER PUNTOCOMA clasetipo_clase : PUBLIC\n                    | PROTECTED\n                    | PRIVATEvar : VAR varpvarp : tipo_compuesto ID PUNTOCOMA\n            | tipo_compuesto ID PUNTOCOMA varp\n            | tipo_simple ID PUNTOCOMA\n            | tipo_simple ID PUNTOCOMA varp\n            | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA\n            | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA varp\n            | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA\n            | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA varptipo_simple : INT\n                    | FLOAT\n                    | CHARtipo_compuesto : IDfuncion : FUNC tipo_simple ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var cuerpo\n                | FUNC tipo_simple ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var cuerpo funcion\n                | FUNC tipo_simple ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA cuerpo\n                | FUNC tipo_simple ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA cuerpo funcion\n                | FUNC VOID ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var cuerpo\n                | FUNC VOID ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var cuerpo funcion\n                | FUNC VOID ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA cuerpo\n                | FUNC VOID ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA cuerpo funciondec_var : VAR dec_varpdec_varp : tipo_simple ID PUNTOCOMA dec_varp\n                | tipo_simple ID PUNTOCOMA\n                | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA dec_varp\n                | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA\n                | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA dec_varp\n                | tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMAparametros : tipo_simple ID\n                    | tipo_simple ID COMA parametroscuerpo : LLAVEIZQ estatuto RETURN exp PUNTOCOMA LLAVEDER\n                | LLAVEIZQ estatuto LLAVEDERbloque_clase : ATTRIBUTE DOSPUNTOS atributo METHOD DOSPUNTOS metodoatributo : tipo_clase tipo_simple ID PUNTOCOMA\n                | tipo_clase tipo_simple ID PUNTOCOMA atributometodo : tipo_clase tipo_simple ID PARENTESISIZQ parametros PARENTESISDER cuerpo\n            | tipo_clase tipo_simple ID PARENTESISIZQ parametros PARENTESISDER cuerpo metodo\n            | tipo_clase VOID ID PARENTESISIZQ parametros PARENTESISDER cuerpo\n            | tipo_clase VOID ID PARENTESISIZQ parametros PARENTESISDER cuerpo metodoestatuto : asignacion PUNTOCOMA\n                | asignacion PUNTOCOMA estatuto\n                | llamada PUNTOCOMA\n                | llamada PUNTOCOMA estatuto\n                | lee PUNTOCOMA\n                | lee PUNTOCOMA estatuto\n                | escribe PUNTOCOMA\n                | escribe PUNTOCOMA estatuto\n                | condicion\n                | condicion estatuto\n                | ciclo_w\n                | ciclo_w estatuto\n                | ciclo_f\n                | ciclo_f estatuto\n                | llamada_metodo PUNTOCOMA estatuto\n                | llamada_atributo PUNTOCOMA estatutoasignacion : variable IGUAL expllamada :  ID PARENTESISIZQ llamadap PARENTESISDERllamadap : exp\n                | exp COMA llamadaplee : READ PARENTESISIZQ leep PARENTESISDERleep : variable\n            | variable COMA leepvariable : ID\n                | ID CORCHETEIZQ exp CORCHETEDER\n                | ID CORCHETEIZQ exp CORCHETEDER CORCHETEIZQ exp CORCHETEDERescribe : WRITE PARENTESISIZQ escribep PARENTESISDERescribep : exp\n                | exp COMA escribep\n                | LETRERO\n                | LETRERO COMA escribepcondicion : IF PARENTESISIZQ exp PARENTESISDER LLAVEIZQ estatuto LLAVEDER\n                | IF PARENTESISIZQ exp PARENTESISDER LLAVEIZQ estatuto LLAVEDER ELSE LLAVEIZQ estatuto LLAVEDERciclo_w : WHILE PARENTESISIZQ exp PARENTESISDER DO LLAVEIZQ estatuto LLAVEDERciclo_f : FROM variable IGUAL exp TO exp DO LLAVEIZQ estatuto LLAVEDERexp : t_exp\n            | t_exp OR expt_exp : g_exp\n            | g_exp AND t_expg_exp : m_exp\n            | m_exp EQUAL m_exp\n            | m_exp NOT m_exp\n            | m_exp GREATERTHAN m_exp\n            | m_exp LESSTHAN m_expm_exp : t\n            | t MAS m_exp\n            | t MENOS m_expt : f\n        | f POR t\n        | f DIV tf : PARENTESISIZQ exp PARENTESISDER\n        | CTEI\n        | CTEF\n        | CTECH\n        | variable\n        | llamada\n        | llamada_metodo\n        | llamada_atributollamada_metodo : ID PUNTO ID PARENTESISIZQ llamada_metodop PARENTESISDERllamada_metodop : CTEI\n                        | CTEI COMA llamada_metodop\n                        | CTEF\n                        | CTEF COMA llamada_metodop\n                        | CTECH\n                        | CTECH COMA llamada_metodop\n                        | ID\n                        | ID COMA llamada_metodopllamada_atributo : ID PUNTO ID'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,5,13,16,18,30,32,33,41,55,83,],[0,-1,-2,-6,-8,-3,-5,-7,-4,-9,-10,]),'ID':([2,10,11,22,23,24,25,26,27,28,29,42,43,44,45,46,50,51,61,62,63,72,80,84,85,86,87,91,92,93,94,95,96,97,98,99,100,125,144,149,151,155,156,157,158,159,160,161,162,163,164,167,168,171,173,174,188,208,212,214,224,228,230,231,232,235,238,239,241,244,252,262,263,269,276,281,],[3,20,23,37,-34,38,-31,-32,-33,39,40,67,73,-19,-20,-21,23,23,67,67,67,102,109,67,67,67,67,67,67,132,132,135,132,102,132,132,132,132,132,181,23,132,132,132,132,132,132,132,132,132,132,132,203,102,132,132,67,132,67,132,243,203,203,203,203,67,255,256,23,132,-92,-94,67,67,-95,-93,]),'PUNTOCOMA':([3,37,38,48,57,58,59,60,64,65,74,108,110,111,118,119,120,121,122,123,124,126,127,128,129,130,131,132,135,146,166,169,170,172,178,181,191,192,193,194,195,196,197,198,199,200,201,220,229,243,251,260,273,288,],[4,50,51,75,84,85,86,87,91,92,104,151,153,154,-115,-77,-96,-98,-100,-105,-108,-112,-113,-114,-116,-117,-118,-84,-128,179,-78,-85,-81,-87,215,219,-97,-99,-101,-102,-103,-104,-106,-107,-109,-110,-111,241,-119,258,-86,268,280,289,]),'MAIN':([4,6,7,8,14,15,17,21,31,50,51,75,77,78,104,105,147,151,179,183,186,190,215,216,221,222,226,227,237,241,242,245,246,257,274,],[9,9,9,9,9,9,9,-22,9,-23,-25,-17,-24,-26,-15,-18,-16,-27,-13,-28,-37,-41,-11,-14,-35,-38,-39,-42,-12,-29,-36,-53,-40,-30,-52,]),'CLASS':([4,75,104,179,215,],[10,10,10,10,10,]),'VAR':([4,6,75,104,105,147,153,154,179,215,216,237,],[11,11,-17,-15,-18,-16,187,187,-13,-11,-14,-12,]),'FUNC':([4,6,7,14,21,50,51,75,77,78,104,105,147,151,179,183,186,190,215,216,221,226,237,241,245,257,274,],[12,12,12,12,-22,-23,-25,-17,-24,-26,-15,-18,-16,-27,-13,-28,12,12,-11,-14,12,12,-12,-29,-53,-30,-52,]),'PARENTESISIZQ':([9,39,40,67,68,69,70,71,93,94,96,98,99,100,125,132,135,144,155,156,157,158,159,160,161,162,163,164,167,173,174,208,214,244,255,256,],[19,53,54,94,97,98,99,100,125,125,125,125,125,125,125,94,168,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,264,265,]),'INT':([11,12,44,45,46,50,51,53,54,107,151,152,187,218,241,258,264,265,280,289,],[25,25,-19,-20,-21,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'FLOAT':([11,12,44,45,46,50,51,53,54,107,151,152,187,218,241,258,264,265,280,289,],[26,26,-19,-20,-21,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'CHAR':([11,12,44,45,46,50,51,53,54,107,151,152,187,218,241,258,264,265,280,289,],[27,27,-19,-20,-21,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'VOID':([12,44,45,46,218,],[29,-19,-20,-21,239,]),'PARENTESISDER':([19,81,82,102,109,118,120,121,122,123,124,126,127,128,129,130,131,132,133,134,135,137,138,139,140,141,142,143,165,166,169,184,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,209,210,211,229,247,248,249,250,251,271,272,],[34,110,111,-84,-50,-115,-96,-98,-100,-105,-108,-112,-113,-114,-116,-117,-118,-84,166,-79,-128,170,-82,172,-88,-90,175,176,201,-78,-85,-51,-97,-99,-101,-102,-103,-104,-106,-107,-109,-110,-111,-80,-126,229,-120,-122,-124,-83,-89,-91,-119,-127,-121,-123,-125,-86,277,278,]),'DOSPUNTOS':([20,49,148,],[35,76,180,]),'LLAVEIZQ':([20,34,73,153,154,175,185,189,213,223,254,258,261,266,277,278,280,285,289,290,],[36,42,103,188,188,212,188,188,235,-43,263,-45,269,-44,188,188,-47,-46,-49,-48,]),'PUBLIC':([35,76,180,219,245,274,282,283,],[44,44,44,44,-53,-52,44,44,]),'PROTECTED':([35,76,180,219,245,274,282,283,],[45,45,45,45,-53,-52,45,45,]),'PRIVATE':([35,76,180,219,245,274,282,283,],[46,46,46,46,-53,-52,46,46,]),'LLAVEDER':([36,42,47,56,61,62,63,84,85,86,87,88,89,90,103,112,113,114,115,116,117,145,217,225,234,245,252,253,262,268,270,274,275,276,281,282,283,286,287,],[48,55,74,83,-69,-71,-73,-61,-63,-65,-67,-70,-72,-74,146,-62,-64,-66,-68,-75,-76,178,-54,245,252,-53,-92,262,-94,274,276,-52,281,-95,-93,-57,-59,-58,-60,]),'ATTRIBUTE':([36,103,],[49,49,]),'CORCHETEIZQ':([38,67,102,108,132,169,243,273,],[52,96,96,150,96,208,259,279,]),'READ':([42,61,62,63,84,85,86,87,91,92,188,212,235,252,262,263,269,276,281,],[68,68,68,68,68,68,68,68,68,68,68,68,68,-92,-94,68,68,-95,-93,]),'WRITE':([42,61,62,63,84,85,86,87,91,92,188,212,235,252,262,263,269,276,281,],[69,69,69,69,69,69,69,69,69,69,69,69,69,-92,-94,69,69,-95,-93,]),'IF':([42,61,62,63,84,85,86,87,91,92,188,212,235,252,262,263,269,276,281,],[70,70,70,70,70,70,70,70,70,70,70,70,70,-92,-94,70,70,-95,-93,]),'WHILE':([42,61,62,63,84,85,86,87,91,92,188,212,235,252,262,263,269,276,281,],[71,71,71,71,71,71,71,71,71,71,71,71,71,-92,-94,71,71,-95,-93,]),'FROM':([42,61,62,63,84,85,86,87,91,92,188,212,235,252,262,263,269,276,281,],[72,72,72,72,72,72,72,72,72,72,72,72,72,-92,-94,72,72,-95,-93,]),'CTEI':([52,93,94,96,98,99,100,125,144,150,155,156,157,158,159,160,161,162,163,164,167,168,173,174,208,214,228,230,231,232,244,259,279,],[79,126,126,126,126,126,126,126,126,182,126,126,126,126,126,126,126,126,126,126,126,205,126,126,126,126,205,205,205,205,126,267,284,]),'RETURN':([61,62,63,84,85,86,87,88,89,90,112,113,114,115,116,117,225,252,262,276,281,],[-69,-71,-73,-61,-63,-65,-67,-70,-72,-74,-62,-64,-66,-68,-75,-76,244,-92,-94,-95,-93,]),'IGUAL':([66,67,101,102,169,251,],[93,-84,144,-84,-85,-86,]),'PUNTO':([67,132,],[95,95,]),'CORCHETEDER':([79,118,120,121,122,123,124,126,127,128,129,130,131,132,135,136,166,169,182,191,192,193,194,195,196,197,198,199,200,201,229,233,251,267,284,],[108,-115,-96,-98,-100,-105,-108,-112,-113,-114,-116,-117,-118,-84,-128,169,-78,-85,220,-97,-99,-101,-102,-103,-104,-106,-107,-109,-110,-111,-119,251,-86,273,288,]),'CTEF':([93,94,96,98,99,100,125,144,155,156,157,158,159,160,161,162,163,164,167,168,173,174,208,214,228,230,231,232,244,],[127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,206,127,127,127,127,206,206,206,206,127,]),'CTECH':([93,94,96,98,99,100,125,144,155,156,157,158,159,160,161,162,163,164,167,168,173,174,208,214,228,230,231,232,244,],[128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,207,128,128,128,128,207,207,207,207,128,]),'LETRERO':([98,173,174,],[141,141,141,]),'COMA':([102,109,118,120,121,122,123,124,126,127,128,129,130,131,132,134,135,138,140,141,166,169,191,192,193,194,195,196,197,198,199,200,201,203,205,206,207,229,251,],[-84,152,-115,-96,-98,-100,-105,-108,-112,-113,-114,-116,-117,-118,-84,167,-128,171,173,174,-78,-85,-97,-99,-101,-102,-103,-104,-106,-107,-109,-110,-111,228,230,231,232,-119,-86,]),'METHOD':([106,219,240,],[148,-55,-56,]),'POR':([118,124,126,127,128,129,130,131,132,135,166,169,201,229,251,],[-115,163,-112,-113,-114,-116,-117,-118,-84,-128,-78,-85,-111,-119,-86,]),'DIV':([118,124,126,127,128,129,130,131,132,135,166,169,201,229,251,],[-115,164,-112,-113,-114,-116,-117,-118,-84,-128,-78,-85,-111,-119,-86,]),'MAS':([118,123,124,126,127,128,129,130,131,132,135,166,169,199,200,201,229,251,],[-115,161,-108,-112,-113,-114,-116,-117,-118,-84,-128,-78,-85,-109,-110,-111,-119,-86,]),'MENOS':([118,123,124,126,127,128,129,130,131,132,135,166,169,199,200,201,229,251,],[-115,162,-108,-112,-113,-114,-116,-117,-118,-84,-128,-78,-85,-109,-110,-111,-119,-86,]),'EQUAL':([118,122,123,124,126,127,128,129,130,131,132,135,166,169,197,198,199,200,201,229,251,],[-115,157,-105,-108,-112,-113,-114,-116,-117,-118,-84,-128,-78,-85,-106,-107,-109,-110,-111,-119,-86,]),'NOT':([118,122,123,124,126,127,128,129,130,131,132,135,166,169,197,198,199,200,201,229,251,],[-115,158,-105,-108,-112,-113,-114,-116,-117,-118,-84,-128,-78,-85,-106,-107,-109,-110,-111,-119,-86,]),'GREATERTHAN':([118,122,123,124,126,127,128,129,130,131,132,135,166,169,197,198,199,200,201,229,251,],[-115,159,-105,-108,-112,-113,-114,-116,-117,-118,-84,-128,-78,-85,-106,-107,-109,-110,-111,-119,-86,]),'LESSTHAN':([118,122,123,124,126,127,128,129,130,131,132,135,166,169,197,198,199,200,201,229,251,],[-115,160,-105,-108,-112,-113,-114,-116,-117,-118,-84,-128,-78,-85,-106,-107,-109,-110,-111,-119,-86,]),'AND':([118,121,122,123,124,126,127,128,129,130,131,132,135,166,169,193,194,195,196,197,198,199,200,201,229,251,],[-115,156,-100,-105,-108,-112,-113,-114,-116,-117,-118,-84,-128,-78,-85,-101,-102,-103,-104,-106,-107,-109,-110,-111,-119,-86,]),'OR':([118,120,121,122,123,124,126,127,128,129,130,131,132,135,166,169,192,193,194,195,196,197,198,199,200,201,229,251,],[-115,155,-98,-100,-105,-108,-112,-113,-114,-116,-117,-118,-84,-128,-78,-85,-99,-101,-102,-103,-104,-106,-107,-109,-110,-111,-119,-86,]),'TO':([118,120,121,122,123,124,126,127,128,129,130,131,132,135,166,169,177,191,192,193,194,195,196,197,198,199,200,201,229,251,],[-115,-96,-98,-100,-105,-108,-112,-113,-114,-116,-117,-118,-84,-128,-78,-85,214,-97,-99,-101,-102,-103,-104,-106,-107,-109,-110,-111,-119,-86,]),'DO':([118,120,121,122,123,124,126,127,128,129,130,131,132,135,166,169,176,191,192,193,194,195,196,197,198,199,200,201,229,236,251,],[-115,-96,-98,-100,-105,-108,-112,-113,-114,-116,-117,-118,-84,-128,-78,-85,213,-97,-99,-101,-102,-103,-104,-106,-107,-109,-110,-111,-119,254,-86,]),'ELSE':([252,],[261,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'main':([4,6,7,8,14,15,17,31,],[5,13,16,18,30,32,33,41,]),'clase':([4,75,104,179,215,],[6,105,147,216,237,]),'var':([4,6,],[7,14,]),'funcion':([4,6,7,14,186,190,221,226,],[8,15,17,31,222,227,242,246,]),'varp':([11,50,51,151,241,],[21,77,78,183,257,]),'tipo_compuesto':([11,50,51,151,241,],[22,22,22,22,22,]),'tipo_simple':([11,12,50,51,53,54,107,151,152,187,218,241,258,264,265,280,289,],[24,28,24,24,80,80,149,24,80,224,238,24,224,80,80,224,224,]),'tipo_clase':([35,76,180,219,282,283,],[43,107,218,107,218,218,]),'bloque_clase':([36,103,],[47,145,]),'estatuto':([42,61,62,63,84,85,86,87,91,92,188,212,235,263,269,],[56,88,89,90,112,113,114,115,116,117,225,234,253,270,275,]),'asignacion':([42,61,62,63,84,85,86,87,91,92,188,212,235,263,269,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'llamada':([42,61,62,63,84,85,86,87,91,92,93,94,96,98,99,100,125,144,155,156,157,158,159,160,161,162,163,164,167,173,174,188,208,212,214,235,244,263,269,],[58,58,58,58,58,58,58,58,58,58,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,58,129,58,129,58,129,58,58,]),'lee':([42,61,62,63,84,85,86,87,91,92,188,212,235,263,269,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'escribe':([42,61,62,63,84,85,86,87,91,92,188,212,235,263,269,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'condicion':([42,61,62,63,84,85,86,87,91,92,188,212,235,263,269,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'ciclo_w':([42,61,62,63,84,85,86,87,91,92,188,212,235,263,269,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'ciclo_f':([42,61,62,63,84,85,86,87,91,92,188,212,235,263,269,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'llamada_metodo':([42,61,62,63,84,85,86,87,91,92,93,94,96,98,99,100,125,144,155,156,157,158,159,160,161,162,163,164,167,173,174,188,208,212,214,235,244,263,269,],[64,64,64,64,64,64,64,64,64,64,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,64,130,64,130,64,130,64,64,]),'llamada_atributo':([42,61,62,63,84,85,86,87,91,92,93,94,96,98,99,100,125,144,155,156,157,158,159,160,161,162,163,164,167,173,174,188,208,212,214,235,244,263,269,],[65,65,65,65,65,65,65,65,65,65,131,131,131,131,131,131,131,131,131,131,131,131,131,131,131,131,131,131,131,131,131,65,131,65,131,65,131,65,65,]),'variable':([42,61,62,63,72,84,85,86,87,91,92,93,94,96,97,98,99,100,125,144,155,156,157,158,159,160,161,162,163,164,167,171,173,174,188,208,212,214,235,244,263,269,],[66,66,66,66,101,66,66,66,66,66,66,118,118,118,138,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,138,118,118,66,118,66,118,66,118,66,66,]),'parametros':([53,54,152,264,265,],[81,82,184,271,272,]),'atributo':([76,219,],[106,240,]),'exp':([93,94,96,98,99,100,125,144,155,167,173,174,208,214,244,],[119,134,136,140,142,143,165,177,191,134,140,140,233,236,260,]),'t_exp':([93,94,96,98,99,100,125,144,155,156,167,173,174,208,214,244,],[120,120,120,120,120,120,120,120,120,192,120,120,120,120,120,120,]),'g_exp':([93,94,96,98,99,100,125,144,155,156,167,173,174,208,214,244,],[121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,]),'m_exp':([93,94,96,98,99,100,125,144,155,156,157,158,159,160,161,162,167,173,174,208,214,244,],[122,122,122,122,122,122,122,122,122,122,193,194,195,196,197,198,122,122,122,122,122,122,]),'t':([93,94,96,98,99,100,125,144,155,156,157,158,159,160,161,162,163,164,167,173,174,208,214,244,],[123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,199,200,123,123,123,123,123,123,]),'f':([93,94,96,98,99,100,125,144,155,156,157,158,159,160,161,162,163,164,167,173,174,208,214,244,],[124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,]),'llamadap':([94,167,],[133,202,]),'leep':([97,171,],[137,209,]),'escribep':([98,173,174,],[139,210,211,]),'dec_var':([153,154,],[185,189,]),'cuerpo':([153,154,185,189,277,278,],[186,190,221,226,282,283,]),'llamada_metodop':([168,228,230,231,232,],[204,247,248,249,250,]),'metodo':([180,282,283,],[217,286,287,]),'dec_varp':([187,258,280,289,],[223,266,285,290,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAM ID PUNTOCOMA main','programa',4,'p_programa','scpa.py',123),
  ('programa -> PROGRAM ID PUNTOCOMA clase main','programa',5,'p_programa','scpa.py',124),
  ('programa -> PROGRAM ID PUNTOCOMA clase var main','programa',6,'p_programa','scpa.py',125),
  ('programa -> PROGRAM ID PUNTOCOMA clase var funcion main','programa',7,'p_programa','scpa.py',126),
  ('programa -> PROGRAM ID PUNTOCOMA clase funcion main','programa',6,'p_programa','scpa.py',127),
  ('programa -> PROGRAM ID PUNTOCOMA var main','programa',5,'p_programa','scpa.py',128),
  ('programa -> PROGRAM ID PUNTOCOMA var funcion main','programa',6,'p_programa','scpa.py',129),
  ('programa -> PROGRAM ID PUNTOCOMA funcion main','programa',5,'p_programa','scpa.py',130),
  ('main -> MAIN PARENTESISIZQ PARENTESISDER LLAVEIZQ LLAVEDER','main',5,'p_main','scpa.py',134),
  ('main -> MAIN PARENTESISIZQ PARENTESISDER LLAVEIZQ estatuto LLAVEDER','main',6,'p_main','scpa.py',135),
  ('clase -> CLASS ID DOSPUNTOS tipo_clase ID LLAVEIZQ bloque_clase LLAVEDER PUNTOCOMA','clase',9,'p_clase','scpa.py',138),
  ('clase -> CLASS ID DOSPUNTOS tipo_clase ID LLAVEIZQ bloque_clase LLAVEDER PUNTOCOMA clase','clase',10,'p_clase','scpa.py',139),
  ('clase -> CLASS ID DOSPUNTOS tipo_clase ID LLAVEIZQ LLAVEDER PUNTOCOMA','clase',8,'p_clase','scpa.py',140),
  ('clase -> CLASS ID DOSPUNTOS tipo_clase ID LLAVEIZQ LLAVEDER PUNTOCOMA clase','clase',9,'p_clase','scpa.py',141),
  ('clase -> CLASS ID LLAVEIZQ bloque_clase LLAVEDER PUNTOCOMA','clase',6,'p_clase','scpa.py',142),
  ('clase -> CLASS ID LLAVEIZQ bloque_clase LLAVEDER PUNTOCOMA clase','clase',7,'p_clase','scpa.py',143),
  ('clase -> CLASS ID LLAVEIZQ LLAVEDER PUNTOCOMA','clase',5,'p_clase','scpa.py',144),
  ('clase -> CLASS ID LLAVEIZQ LLAVEDER PUNTOCOMA clase','clase',6,'p_clase','scpa.py',145),
  ('tipo_clase -> PUBLIC','tipo_clase',1,'p_tipo_clase','scpa.py',148),
  ('tipo_clase -> PROTECTED','tipo_clase',1,'p_tipo_clase','scpa.py',149),
  ('tipo_clase -> PRIVATE','tipo_clase',1,'p_tipo_clase','scpa.py',150),
  ('var -> VAR varp','var',2,'p_var','scpa.py',153),
  ('varp -> tipo_compuesto ID PUNTOCOMA','varp',3,'p_varp','scpa.py',156),
  ('varp -> tipo_compuesto ID PUNTOCOMA varp','varp',4,'p_varp','scpa.py',157),
  ('varp -> tipo_simple ID PUNTOCOMA','varp',3,'p_varp','scpa.py',158),
  ('varp -> tipo_simple ID PUNTOCOMA varp','varp',4,'p_varp','scpa.py',159),
  ('varp -> tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA','varp',6,'p_varp','scpa.py',160),
  ('varp -> tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA varp','varp',7,'p_varp','scpa.py',161),
  ('varp -> tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA','varp',9,'p_varp','scpa.py',162),
  ('varp -> tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA varp','varp',10,'p_varp','scpa.py',163),
  ('tipo_simple -> INT','tipo_simple',1,'p_tipo_simple','scpa.py',166),
  ('tipo_simple -> FLOAT','tipo_simple',1,'p_tipo_simple','scpa.py',167),
  ('tipo_simple -> CHAR','tipo_simple',1,'p_tipo_simple','scpa.py',168),
  ('tipo_compuesto -> ID','tipo_compuesto',1,'p_tipo_compuesto','scpa.py',171),
  ('funcion -> FUNC tipo_simple ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var cuerpo','funcion',9,'p_funcion','scpa.py',174),
  ('funcion -> FUNC tipo_simple ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var cuerpo funcion','funcion',10,'p_funcion','scpa.py',175),
  ('funcion -> FUNC tipo_simple ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA cuerpo','funcion',8,'p_funcion','scpa.py',176),
  ('funcion -> FUNC tipo_simple ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA cuerpo funcion','funcion',9,'p_funcion','scpa.py',177),
  ('funcion -> FUNC VOID ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var cuerpo','funcion',9,'p_funcion','scpa.py',178),
  ('funcion -> FUNC VOID ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA dec_var cuerpo funcion','funcion',10,'p_funcion','scpa.py',179),
  ('funcion -> FUNC VOID ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA cuerpo','funcion',8,'p_funcion','scpa.py',180),
  ('funcion -> FUNC VOID ID PARENTESISIZQ parametros PARENTESISDER PUNTOCOMA cuerpo funcion','funcion',9,'p_funcion','scpa.py',181),
  ('dec_var -> VAR dec_varp','dec_var',2,'p_dec_var','scpa.py',184),
  ('dec_varp -> tipo_simple ID PUNTOCOMA dec_varp','dec_varp',4,'p_dec_varp','scpa.py',187),
  ('dec_varp -> tipo_simple ID PUNTOCOMA','dec_varp',3,'p_dec_varp','scpa.py',188),
  ('dec_varp -> tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA dec_varp','dec_varp',7,'p_dec_varp','scpa.py',189),
  ('dec_varp -> tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA','dec_varp',6,'p_dec_varp','scpa.py',190),
  ('dec_varp -> tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA dec_varp','dec_varp',10,'p_dec_varp','scpa.py',191),
  ('dec_varp -> tipo_simple ID CORCHETEIZQ CTEI CORCHETEDER CORCHETEIZQ CTEI CORCHETEDER PUNTOCOMA','dec_varp',9,'p_dec_varp','scpa.py',192),
  ('parametros -> tipo_simple ID','parametros',2,'p_parametros','scpa.py',195),
  ('parametros -> tipo_simple ID COMA parametros','parametros',4,'p_parametros','scpa.py',196),
  ('cuerpo -> LLAVEIZQ estatuto RETURN exp PUNTOCOMA LLAVEDER','cuerpo',6,'p_cuerpo','scpa.py',199),
  ('cuerpo -> LLAVEIZQ estatuto LLAVEDER','cuerpo',3,'p_cuerpo','scpa.py',200),
  ('bloque_clase -> ATTRIBUTE DOSPUNTOS atributo METHOD DOSPUNTOS metodo','bloque_clase',6,'p_bloque_clase','scpa.py',203),
  ('atributo -> tipo_clase tipo_simple ID PUNTOCOMA','atributo',4,'p_atributo','scpa.py',206),
  ('atributo -> tipo_clase tipo_simple ID PUNTOCOMA atributo','atributo',5,'p_atributo','scpa.py',207),
  ('metodo -> tipo_clase tipo_simple ID PARENTESISIZQ parametros PARENTESISDER cuerpo','metodo',7,'p_metodo','scpa.py',210),
  ('metodo -> tipo_clase tipo_simple ID PARENTESISIZQ parametros PARENTESISDER cuerpo metodo','metodo',8,'p_metodo','scpa.py',211),
  ('metodo -> tipo_clase VOID ID PARENTESISIZQ parametros PARENTESISDER cuerpo','metodo',7,'p_metodo','scpa.py',212),
  ('metodo -> tipo_clase VOID ID PARENTESISIZQ parametros PARENTESISDER cuerpo metodo','metodo',8,'p_metodo','scpa.py',213),
  ('estatuto -> asignacion PUNTOCOMA','estatuto',2,'p_estatuto','scpa.py',217),
  ('estatuto -> asignacion PUNTOCOMA estatuto','estatuto',3,'p_estatuto','scpa.py',218),
  ('estatuto -> llamada PUNTOCOMA','estatuto',2,'p_estatuto','scpa.py',219),
  ('estatuto -> llamada PUNTOCOMA estatuto','estatuto',3,'p_estatuto','scpa.py',220),
  ('estatuto -> lee PUNTOCOMA','estatuto',2,'p_estatuto','scpa.py',221),
  ('estatuto -> lee PUNTOCOMA estatuto','estatuto',3,'p_estatuto','scpa.py',222),
  ('estatuto -> escribe PUNTOCOMA','estatuto',2,'p_estatuto','scpa.py',223),
  ('estatuto -> escribe PUNTOCOMA estatuto','estatuto',3,'p_estatuto','scpa.py',224),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','scpa.py',225),
  ('estatuto -> condicion estatuto','estatuto',2,'p_estatuto','scpa.py',226),
  ('estatuto -> ciclo_w','estatuto',1,'p_estatuto','scpa.py',227),
  ('estatuto -> ciclo_w estatuto','estatuto',2,'p_estatuto','scpa.py',228),
  ('estatuto -> ciclo_f','estatuto',1,'p_estatuto','scpa.py',229),
  ('estatuto -> ciclo_f estatuto','estatuto',2,'p_estatuto','scpa.py',230),
  ('estatuto -> llamada_metodo PUNTOCOMA estatuto','estatuto',3,'p_estatuto','scpa.py',231),
  ('estatuto -> llamada_atributo PUNTOCOMA estatuto','estatuto',3,'p_estatuto','scpa.py',232),
  ('asignacion -> variable IGUAL exp','asignacion',3,'p_asignacion','scpa.py',235),
  ('llamada -> ID PARENTESISIZQ llamadap PARENTESISDER','llamada',4,'p_llamada','scpa.py',238),
  ('llamadap -> exp','llamadap',1,'p_llamadap','scpa.py',241),
  ('llamadap -> exp COMA llamadap','llamadap',3,'p_llamadap','scpa.py',242),
  ('lee -> READ PARENTESISIZQ leep PARENTESISDER','lee',4,'p_lee','scpa.py',245),
  ('leep -> variable','leep',1,'p_leep','scpa.py',248),
  ('leep -> variable COMA leep','leep',3,'p_leep','scpa.py',249),
  ('variable -> ID','variable',1,'p_variable','scpa.py',252),
  ('variable -> ID CORCHETEIZQ exp CORCHETEDER','variable',4,'p_variable','scpa.py',253),
  ('variable -> ID CORCHETEIZQ exp CORCHETEDER CORCHETEIZQ exp CORCHETEDER','variable',7,'p_variable','scpa.py',254),
  ('escribe -> WRITE PARENTESISIZQ escribep PARENTESISDER','escribe',4,'p_escribe','scpa.py',257),
  ('escribep -> exp','escribep',1,'p_escribep','scpa.py',260),
  ('escribep -> exp COMA escribep','escribep',3,'p_escribep','scpa.py',261),
  ('escribep -> LETRERO','escribep',1,'p_escribep','scpa.py',262),
  ('escribep -> LETRERO COMA escribep','escribep',3,'p_escribep','scpa.py',263),
  ('condicion -> IF PARENTESISIZQ exp PARENTESISDER LLAVEIZQ estatuto LLAVEDER','condicion',7,'p_condicion','scpa.py',266),
  ('condicion -> IF PARENTESISIZQ exp PARENTESISDER LLAVEIZQ estatuto LLAVEDER ELSE LLAVEIZQ estatuto LLAVEDER','condicion',11,'p_condicion','scpa.py',267),
  ('ciclo_w -> WHILE PARENTESISIZQ exp PARENTESISDER DO LLAVEIZQ estatuto LLAVEDER','ciclo_w',8,'p_ciclo_w','scpa.py',270),
  ('ciclo_f -> FROM variable IGUAL exp TO exp DO LLAVEIZQ estatuto LLAVEDER','ciclo_f',10,'p_ciclo_f','scpa.py',273),
  ('exp -> t_exp','exp',1,'p_exp','scpa.py',276),
  ('exp -> t_exp OR exp','exp',3,'p_exp','scpa.py',277),
  ('t_exp -> g_exp','t_exp',1,'p_t_exp','scpa.py',280),
  ('t_exp -> g_exp AND t_exp','t_exp',3,'p_t_exp','scpa.py',281),
  ('g_exp -> m_exp','g_exp',1,'p_g_exp','scpa.py',284),
  ('g_exp -> m_exp EQUAL m_exp','g_exp',3,'p_g_exp','scpa.py',285),
  ('g_exp -> m_exp NOT m_exp','g_exp',3,'p_g_exp','scpa.py',286),
  ('g_exp -> m_exp GREATERTHAN m_exp','g_exp',3,'p_g_exp','scpa.py',287),
  ('g_exp -> m_exp LESSTHAN m_exp','g_exp',3,'p_g_exp','scpa.py',288),
  ('m_exp -> t','m_exp',1,'p_m_exp','scpa.py',291),
  ('m_exp -> t MAS m_exp','m_exp',3,'p_m_exp','scpa.py',292),
  ('m_exp -> t MENOS m_exp','m_exp',3,'p_m_exp','scpa.py',293),
  ('t -> f','t',1,'p_t','scpa.py',296),
  ('t -> f POR t','t',3,'p_t','scpa.py',297),
  ('t -> f DIV t','t',3,'p_t','scpa.py',298),
  ('f -> PARENTESISIZQ exp PARENTESISDER','f',3,'p_f','scpa.py',301),
  ('f -> CTEI','f',1,'p_f','scpa.py',302),
  ('f -> CTEF','f',1,'p_f','scpa.py',303),
  ('f -> CTECH','f',1,'p_f','scpa.py',304),
  ('f -> variable','f',1,'p_f','scpa.py',305),
  ('f -> llamada','f',1,'p_f','scpa.py',306),
  ('f -> llamada_metodo','f',1,'p_f','scpa.py',307),
  ('f -> llamada_atributo','f',1,'p_f','scpa.py',308),
  ('llamada_metodo -> ID PUNTO ID PARENTESISIZQ llamada_metodop PARENTESISDER','llamada_metodo',6,'p_llamada_metodo','scpa.py',311),
  ('llamada_metodop -> CTEI','llamada_metodop',1,'p_llamada_metodop','scpa.py',314),
  ('llamada_metodop -> CTEI COMA llamada_metodop','llamada_metodop',3,'p_llamada_metodop','scpa.py',315),
  ('llamada_metodop -> CTEF','llamada_metodop',1,'p_llamada_metodop','scpa.py',316),
  ('llamada_metodop -> CTEF COMA llamada_metodop','llamada_metodop',3,'p_llamada_metodop','scpa.py',317),
  ('llamada_metodop -> CTECH','llamada_metodop',1,'p_llamada_metodop','scpa.py',318),
  ('llamada_metodop -> CTECH COMA llamada_metodop','llamada_metodop',3,'p_llamada_metodop','scpa.py',319),
  ('llamada_metodop -> ID','llamada_metodop',1,'p_llamada_metodop','scpa.py',320),
  ('llamada_metodop -> ID COMA llamada_metodop','llamada_metodop',3,'p_llamada_metodop','scpa.py',321),
  ('llamada_atributo -> ID PUNTO ID','llamada_atributo',3,'p_llamada_atributo','scpa.py',324),
]
