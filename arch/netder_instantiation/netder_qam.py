from query_answering_module import QueryAnsweringModule

class NetDERQAM(QueryAnsweringModule):

	def __init__(self):
		super.__init__()

	def answer_query(self, query):
		pass

	def get_sources(self):
		self._symbolic.get_sources()
