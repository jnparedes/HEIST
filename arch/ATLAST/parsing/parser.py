# -*- coding=utf-8 -*-

#import ply.yacc as yacc
from .ply import yacc
import sys
import os
from .lexer import *
import ATLAST.ast_atlast as ast
import ATLAST.error.parser_exceptions as pe
import ATLAST.error.exception_group as eg

precedence = (
  ('left', 'IFF'),
  ('left', 'IMPLIES'),
  ('left', 'OR'),
  ('left', 'AND'),
  ('right', 'NOT')
)

errors = []

# Formula grammar

def p_formula_atomic_formula(p):
  'formula : atomicFormula'
  p[0] = p[1]

def p_formula_bracketed(p):
  'formula : LBRACKET formula RBRACKET'
  p[0] = p[2]

#Automatically turn A <=> B into (A^B)V(~A^~B) #firstyearlogicbro
def p_formula_iff(p):
  'formula : formula IFF formula'
  lineNo = p.lineno(1)
  pos = p.lexpos(1) + 1
  p[0] = ast.OrNode(lineNo, pos, ast.AndNode(lineNo, pos, p[1], p[3]), \
                                 ast.AndNode(lineNo, pos, \
                                   ast.NotNode(lineNo, pos, p[1]), \
                                   ast.NotNode(lineNo, pos, p[3])))

#Automatically turn A=>B into ~A V B into ~ (A /\ ~ B)
def p_formula_implies(p):
  'formula : formula IMPLIES formula'
  lineNo = p.lineno(1)
  pos = p.lexpos(1) + 1
  p[0] = ast.NotNode(lineNo, pos, ast.AndNode(lineNo, pos, p[1], \
                                              ast.NotNode(lineNo, pos, p[3])))

### A \/ B ###
## using logical equivalence
## P \/ Q === ~(~P /\ ~Q)
def p_formula_or(p):
  'formula : formula OR formula'
  lineNo = p.lineno(1)
  pos = p.lexpos(1) + 1
  p[0] = ast.NotNode(lineNo, pos, ast.AndNode(lineNo, pos, \
                                              ast.NotNode(lineNo, pos, p[1]), \
                                              ast.NotNode(lineNo, pos, p[3])))

### A /\ B ###
def p_formula_and(p):
  'formula : formula AND formula'
  lineNo = p.lineno(1)
  pos = p.lexpos(1) + 1
  p[0] = ast.AndNode(lineNo, pos, p[1], p[3])

### ~ A ###
def p_formula_not(p):
  'formula : NOT formula'
  print('Reducing to NOT(' + str(p[2]) + ')')
  lineNo = p.lineno(1)
  pos = p.lexpos(1) + 1
  p[0] = ast.NotNode(lineNo, pos, p[2])


#### QUANTIFIER FORMULAS
def p_quantifier_list(p):
  'quantifierList : quantifierList COMMA IDENTIFIER'
  p[0] = p[1] + [p[3]]

def p_quantifier_single(p):
  'quantifierList : IDENTIFIER'
  p[0] = [p[1]]

def p_formula_forall(p):
  'formula : FORALL quantifierList LBRACKET formula RBRACKET'
  lineNo = p.lineno(1)
  pos = p.lexpos(1) + 1
  p[0] = ast.ForAllNode(lineNo, pos, p[2], p[4])

def p_formula_thereexists(p):
  'formula : THEREEXISTS quantifierList LBRACKET formula RBRACKET'
  lineNo = p.lineno(1)
  pos = p.lexpos(1) + 1
  p[0] = ast.ThereExistsNode(lineNo, pos, p[2], p[4])

# Atomic Formula grammar
# Creates a shift reduce conflict
# def p_bracketed_atomic_formula(p):
#    'atomicFormula : LBRACKET atomicFormula RBRACKET'
#     p[0] = p[2]

def p_atomic_formula_predicate(p):
  'atomicFormula : IDENTIFIER LBRACKET termList RBRACKET'
  lineNo = p.lineno(1)
  pos = p.lexpos(1) + 1
  p[0] = ast.PredicateNode(lineNo, pos, p[1], p[3])

def p_atomic_formula_eq(p):
  '''atomicFormula : expression EQ expression
                   | expression EQ term
                   | term EQ expression
                   | term EQ term'''
  lineNo = p.lineno(1)
  pos = p.lexpos(1) + 1
  p[0] = ast.BinaryOperatorNode(lineNo, pos, p[1], p[3], \
                                ast.BinaryOperatorNode.EQ)

def p_expression_plus(p):
  'expression : expression PLUS term'
  lineNo = p.lineno(1)
  pos = p.lexpos(1) + 1

  p[0] = ast.PlusNode(lineNo, pos, p[1], p[3])

def p_atomic_expression_plus(p):
  'expression : term PLUS term'
  lineNo = p.lineno(1)
  pos = p.lexpos(1) + 1

  p[0] = ast.PlusNode(lineNo, pos, p[1], p[3])

def p_atomic_formula_lt(p):
  '''atomicFormula : expression LT expression
                   | expression LT term
                   | term LT expression
                   | term LT term'''
  lineNo = p.lineno(1)
  pos = p.lexpos(1) + 1
  p[0] = ast.BinaryOperatorNode(lineNo, pos, p[1], p[3], \
                                ast.BinaryOperatorNode.LT)

def p_atomic_formula_lte(p):
  '''atomicFormula : expression LTE expression
                   | expression LTE term
                   | term LTE expression
                   | term LTE term'''
  lineNo = p.lineno(1)
  pos = p.lexpos(1) + 1
  p[0] = ast.BinaryOperatorNode(lineNo, pos, p[1], p[3], \
                                ast.BinaryOperatorNode.LTE)

def p_atomic_formula_gt(p):
  '''atomicFormula : expression GT expression
                   | expression GT term
                   | term GT expression
                   | term GT term'''
  'atomicFormula : term GT term'
  lineNo = p.lineno(1)
  pos = p.lexpos(1) + 1
  p[0] = ast.BinaryOperatorNode(lineNo, pos, p[1], p[3], \
                                ast.BinaryOperatorNode.GT)

def p_atomic_formula_gte(p):
  '''atomicFormula : expression GTE expression
                   | expression GTE term
                   | term GTE expression
                   | term GTE term'''
  lineNo = p.lineno(1)
  pos = p.lexpos(1) + 1
  p[0] = ast.BinaryOperatorNode(lineNo, pos, p[1], p[3], \
                                ast.BinaryOperatorNode.GTE)

def p_atomic_formula_neq(p):
  '''atomicFormula : expression NEQ expression
                   | expression NEQ term
                   | term NEQ expression
                   | term NEQ term'''
  lineNo = p.lineno(1)
  pos = p.lexpos(1) + 1
  p[0] = ast.BinaryOperatorNode(lineNo, pos, p[1], p[3], \
                                ast.BinaryOperatorNode.NEQ)




# Term list grammar

def p_term_list(p):
  'termList : termList COMMA term'
  p[0] = p[1] + [p[3]]

def p_term_list_single(p):
  'termList : term'
  p[0] = [p[1]]

# Term grammar

def p_term_constant(p):
  'term : CONSTANT'
  lineNo = p.lineno(1)
  pos = p.lexpos(1) + 1
  p[0] = ast.ConstantNode(lineNo, pos, p[1])

def p_term_variable(p):
  'term : IDENTIFIER'
  lineNo = p.lineno(1)
  pos = p.lexpos(1) + 1
  p[0] = ast.VariableNode(lineNo, pos, p[1])

def p_term_stringlit(p):
  'term : STRINGLIT'
  lineNo = p.lineno(1)
  pos = p.lexpos(1) + 1
  p[0] = ast.StringLitNode(lineNo, pos, p[1])

def p_term_true(p):
  'term : TRUE'
  lineNo = p.lineno(1)
  pos = p.lexpos(1) + 1
  p[0] = ast.BooleanNode(lineNo, pos, True)

def p_term_false(p):
  'term : FALSE'
  lineNo = p.lineno(1)
  pos = p.lexpos(1) + 1
  p[0] = ast.BooleanNode(lineNo, pos, False)

# Parsing and error functions

def p_error(p):
  global errors
  if p is None:
    errors.append(pe.ParserEOIException())
  else:
    pos = getPosition(p.lexer) - len(p.value)
    errors.append(pe.ParserTokenException(p.lineno, pos, str(p.value)))

def parse_input(input):
  global errors
  errors = []
  lexer = getLexer()
  parser = yacc.yacc()
  result = parser.parse(input, lexer=lexer, tracking=True)
  if lexer.errors or errors:
    raise eg.ExceptionGroup(lexer.errors + errors)
  return result
