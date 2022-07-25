from term import Term
class Variable(Term):
	
	def __init__(self, id_term):
		super().__init__(id_term, None)