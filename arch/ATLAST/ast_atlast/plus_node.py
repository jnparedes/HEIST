'''
And Node
This class implements the AST node of a first order logic formula, in the form
formula AND formula.

Child structure:
  0 = left formula
  1 = right formula
'''

from .binary_operator_node import BinaryOperatorNode
from .variable_node import VariableNode
from .constant_node import ConstantNode

class PlusNode(BinaryOperatorNode):
  def __init__(self, lineNo, position, left, right):
    super(PlusNode, self).__init__(lineNo, position, left, right, BinaryOperatorNode.PLUS)


  def getIdentifier(self):
    left = self.getLeft()
    right = self.getRight()
    id1 = ""
    id2 = ""
    if isinstance(left, ConstantNode):
      id1 = left.getValue()
    else:
      id1 = left.getIdentifier()

    if isinstance(right, ConstantNode):
      id2 = right.getValue()
    else:
      id2 = right.getIdentifier()
    return str(id1) + "_plus_" +  str(id2)

 

  def getBoundValue(self):
    left = self.getLeft()
    right = self.getRight()
    value1 = ""
    value2 = ""
    if isinstance(left, ConstantNode):
      value1 = left.getValue()
    elif isinstance(left, VariableNode):
      value1 = left.getBoundValue()
      relation_sin_num = ''.join([i for i in str(value1.getRelation()) if not i.isdigit()])
      value1 = relation_sin_num + "." + str(value1.getAttribute())
    elif isinstance(left, PlusNode):
      value1 = left.getBoundValue()
      

    if isinstance(right, ConstantNode):
      value2 = right.getValue()
    elif isinstance(right, VariableNode):
      value2 = right.getBoundValue()
      relation_sin_num = ''.join([i for i in str(value2.getRelation()) if not i.isdigit()])
      value2 = relation_sin_num + "." + str(value2.getAttribute())
    elif isinstance(right, PlusNode):
      value2 = right.getBoundValue()

    return str(value1) + " + " + str(value2)

  def setBoundValue(self, boundValue):
    self._boundValue = boundValue

  def isFree(self):
      return False
