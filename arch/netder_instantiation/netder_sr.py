from symbolic_reasoning import SymbolicReasoning

class NetDERSR(SymbolicReasoning):

	def __init__(self):
		super().__init__()

	def answer_query(self, query):
		answer = self._qam.answer_query(query)
		return answer

	def get_sources(self):
		sources = []
		for task in self._tasks:
			sources += task.get_sources()

		return sources

	def get_tasks(self):
		return self._tasks

	def get_services(self):
		return self._services

	def add_service(self, symbol, service):
		self._services[symbol] = service

	def get_service(self, symbol):
		return self._services[symbol]
