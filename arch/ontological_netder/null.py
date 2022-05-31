import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from term import Term

class Null(Term):
	_counter = 0
	
	def __init__(self, value = None):
		if value is None:
			value = 'z' + str(Null._counter)
			Null._counter = Null._counter + 1
		
		super().__init__(str(value), str(value))

	def can_be_instanced(self):
		return True

