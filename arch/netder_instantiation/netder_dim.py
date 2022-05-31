from data_ingestion_module import DataIngestionModule

class NetDERDIM(DataIngestionModule):

	def __init__(self):
		self._kb = KnowledgeBase(rules = [], atoms = [])

	def get_kb(self):
		return self._kb

	def start(self):
		pass
