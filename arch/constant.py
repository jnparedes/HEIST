from term import Term
class Constant(Term):

	def __init__(self, value):
		super().__init__(value, value)