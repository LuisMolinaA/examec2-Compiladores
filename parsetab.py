
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BRACD BRACI COMA FOR GATO ID IGUAL INCLUDE INT MAIN NEWLINE NUM OPLOG OPMAT PARED PAREI PUNTOCOMA RETURN STRINGinit : include functioninclude : GATO INCLUDE OPLOG ID OPLOGfunction : INT MAIN PAREI PARED BRACI statement_list BRACDstatement_list : statement statement_list\n                          | statementstatement : variable_declaration\n                     | assignment\n                     | for_loop\n                     | return_statementvariable_declaration : INT var_list PUNTOCOMAvar_list : ID\n                    | ID IGUAL expression\n                    | var_list COMA ID\n                    | var_list COMA ID IGUAL expressionassignment : INT ID IGUAL expression PUNTOCOMA\n                    | ID IGUAL expression PUNTOCOMAexpression : term\n                      | expression OPMAT termterm : NUM\n                | IDfor_loop : FOR PAREI ID IGUAL NUM PUNTOCOMA ID OPLOG NUM PUNTOCOMA ID OPMAT PARED BRACI statement_list BRACDcondition : expression OPLOG expressionreturn_statement : RETURN NUM PUNTOCOMA\n                            | RETURN ID PUNTOCOMA'
    
_lr_action_items = {'GATO':([0,],[3,]),'$end':([1,4,26,],[0,-1,-3,]),'INT':([2,12,13,16,17,18,19,20,32,40,41,44,48,60,62,],[5,-2,14,14,-6,-7,-8,-9,-10,-23,-24,-16,-15,14,-21,]),'INCLUDE':([3,],[6,]),'MAIN':([5,],[7,]),'OPLOG':([6,10,53,],[8,12,54,]),'PAREI':([7,22,],[9,29,]),'ID':([8,13,14,16,17,18,19,20,23,28,29,32,33,34,40,41,44,45,47,48,52,56,60,62,],[10,21,25,21,-6,-7,-8,-9,31,35,39,-10,42,35,-23,-24,-16,35,35,-15,53,57,21,-21,]),'PARED':([9,58,],[11,59,]),'BRACI':([11,59,],[13,60,]),'FOR':([13,16,17,18,19,20,32,40,41,44,48,60,62,],[22,22,-6,-7,-8,-9,-10,-23,-24,-16,-15,22,-21,]),'RETURN':([13,16,17,18,19,20,32,40,41,44,48,60,62,],[23,23,-6,-7,-8,-9,-10,-23,-24,-16,-15,23,-21,]),'BRACD':([15,16,17,18,19,20,27,32,40,41,44,48,61,62,],[26,-5,-6,-7,-8,-9,-4,-10,-23,-24,-16,-15,62,-21,]),'IGUAL':([21,25,39,42,],[28,34,46,47,]),'NUM':([23,28,34,45,46,47,54,],[30,38,38,38,50,38,55,]),'PUNTOCOMA':([24,25,30,31,35,36,37,38,42,43,49,50,51,55,],[32,-11,40,41,-20,44,-17,-19,-13,48,-18,52,-14,56,]),'COMA':([24,25,35,37,38,42,43,49,51,],[33,-11,-20,-17,-19,-13,-12,-18,-14,]),'OPMAT':([35,36,37,38,43,49,51,57,],[-20,45,-17,-19,45,-18,45,58,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'include':([0,],[2,]),'function':([2,],[4,]),'statement_list':([13,16,60,],[15,27,61,]),'statement':([13,16,60,],[16,16,16,]),'variable_declaration':([13,16,60,],[17,17,17,]),'assignment':([13,16,60,],[18,18,18,]),'for_loop':([13,16,60,],[19,19,19,]),'return_statement':([13,16,60,],[20,20,20,]),'var_list':([14,],[24,]),'expression':([28,34,47,],[36,43,51,]),'term':([28,34,45,47,],[37,37,49,37,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> include function','init',2,'p_init','semantico.py',7),
  ('include -> GATO INCLUDE OPLOG ID OPLOG','include',5,'p_include','semantico.py',10),
  ('function -> INT MAIN PAREI PARED BRACI statement_list BRACD','function',7,'p_function','semantico.py',13),
  ('statement_list -> statement statement_list','statement_list',2,'p_statement_list','semantico.py',17),
  ('statement_list -> statement','statement_list',1,'p_statement_list','semantico.py',18),
  ('statement -> variable_declaration','statement',1,'p_statement','semantico.py',21),
  ('statement -> assignment','statement',1,'p_statement','semantico.py',22),
  ('statement -> for_loop','statement',1,'p_statement','semantico.py',23),
  ('statement -> return_statement','statement',1,'p_statement','semantico.py',24),
  ('variable_declaration -> INT var_list PUNTOCOMA','variable_declaration',3,'p_variable_declaration','semantico.py',27),
  ('var_list -> ID','var_list',1,'p_var_list','semantico.py',38),
  ('var_list -> ID IGUAL expression','var_list',3,'p_var_list','semantico.py',39),
  ('var_list -> var_list COMA ID','var_list',3,'p_var_list','semantico.py',40),
  ('var_list -> var_list COMA ID IGUAL expression','var_list',5,'p_var_list','semantico.py',41),
  ('assignment -> INT ID IGUAL expression PUNTOCOMA','assignment',5,'p_assignment','semantico.py',52),
  ('assignment -> ID IGUAL expression PUNTOCOMA','assignment',4,'p_assignment','semantico.py',53),
  ('expression -> term','expression',1,'p_expression','semantico.py',61),
  ('expression -> expression OPMAT term','expression',3,'p_expression','semantico.py',62),
  ('term -> NUM','term',1,'p_term','semantico.py',65),
  ('term -> ID','term',1,'p_term','semantico.py',66),
  ('for_loop -> FOR PAREI ID IGUAL NUM PUNTOCOMA ID OPLOG NUM PUNTOCOMA ID OPMAT PARED BRACI statement_list BRACD','for_loop',16,'p_for_loop','semantico.py',71),
  ('condition -> expression OPLOG expression','condition',3,'p_condition','semantico.py',83),
  ('return_statement -> RETURN NUM PUNTOCOMA','return_statement',3,'p_return_statement','semantico.py',86),
  ('return_statement -> RETURN ID PUNTOCOMA','return_statement',3,'p_return_statement','semantico.py',87),
]
