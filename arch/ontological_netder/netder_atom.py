from atom import Atom
class NetDerAtom(Atom):


	
	def is_mapped(self, atom):
		result = False
		aux_result = True and self._id == atom.getId()
		if (len(self._terms) == len(atom.get_terms())):
			for x in range(0, len(self._terms)):
				aux_result = aux_result and (self._terms[x].getValue() == atom.get_terms()[x].getValue() or (not self._terms[x].isInstanced()))
			result = aux_result

		return result

	def get_mapping(self, atom):
		result = {}
		if self.is_mapped(atom):
			for x in range(0, len(self._terms)):
				if (not self._terms[x].isInstanced()):
					result[self._terms[x].getId()] = atom.get_terms()[x]
				elif (not atom.get_terms()[x].isInstanced()):
					result[atom.get_terms()[x].getId()] = self._terms[x]
		
		return result

	def map(self, mapping):
		success = True
		for i in range(0, len(self._terms)):
			otherTerm = mapping.get(self._terms[i].getId())
			if (otherTerm != None):
				if (self._terms[i].can_be_instanced()):
					self._terms.remove(self._terms[i])
					self._terms.insert(i, otherTerm)
				elif (not self._terms[i].getValue() == otherTerm.getValue()):
					success = False
		return success

	def __str__(self):
		result = self._id
		for term in self._terms:
			result = result + '\n' +str(term)

		return result

	def __eq__(self, atom):
		result = self._id == atom.getId()
		if len(self._terms) == len(atom.get_terms()):
			for x in range(0, len(self._terms)):
				result = result and self._terms[x] == atom.get_terms()[x]
		else:
			result = False

		result = result or (self is atom)
		
		return result

	def __hash__(self):
		string = str(self._id)
		for term in self._terms:
			string = string + str(term)

		return hash(string)

	def is_equivalent(self, atom):
		result = True
		if (self._id == atom.getId()) and (len(self._terms) == len(atom.get_terms())):
			aux_terms = copy.deepcopy(atom.get_terms())
			index = 0
			for term in self._terms:
				if (not (term.getValue() == aux_terms[index].getValue())):
					result = False
					break
				index += 1					
		else:
			result = False


		return result
