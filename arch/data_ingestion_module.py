from abc import ABC, abstractmethod
from KnowledgeBase import KnowledgeBase
class DataIngestionModule(ABC):

	def __init__(self):
		self._kb = KnowledgeBase(rules = [], atoms = [])

	def get_kb(self):
		return self._kb

	#Main method wich is responsible for carrying out each task of the Data Ingestion Module
	#Of course, each task can be delegated to several other methods
	@abstractmethod
	def start(self):
		pass
