from Ontological.OntQuery import OntQuery
from Ontological.Constant import Constant
from Ontological.Variable import Variable
from Ontological.Atom import Atom
from ATLAST.parsing import parser
from ATLAST.codegen.symtable import SymTable
from ATLAST.codegen.ir_generator import IRGenerator
from ATLAST.codegen.sql_generator import SQLGenerator
from ATLAST.dbbackend import schema as schema
import copy
import json
import mariadb
class Homomorphism:

#verifica si un objeto de esta clase (conjunto de objetos Atom) es equivalante a otro del mismo tipo
#esto significa verificar si existe un homomorfismo que preserve estructura entre ambos conjuntos
#Por ejemplo los conjuntos A = {p1(X_1, Y_1), p2(X_2, Y_2)} y B = {p1(X_3, Y_3), p2(X_4, Y_4)} son homomorficamente equivalentes porque
#p1(X_1, Y_1) se puede mapear a p1(X_3, Y_3) y p2(X_2, Y_2) se puede mapear a p2(X_4, Y_4)
	def is_equivalent(self, ont_db):
		result = False
		if self._size == ont_db.get_size():
			success = True
			other_atoms = copy.deepcopy(ont_db.get_atoms())
			my_atoms = copy.deepcopy(self._atoms)
			db1 = []
			db2 = []
			for key in other_atoms.keys():
				for atom in other_atoms[key]:
					index = self._get_equivalent_index(my_atoms, atom)
					if not index is None:
						my_atoms[key] = my_atoms[key][:index] + my_atoms[key][index + 1:]
					else:
						success = False
						break
				if key in self._atoms.keys():
					db1 = db1 + self._atoms[key]
				db2 = db2 + other_atoms[key]

			if success:
				h = Homomorphism()
				mapping = h.get_atoms_mapping(db1, db2)
				if len(mapping) > 0:
					
					for key_pos in mapping:
						clone_db1 = copy.deepcopy(db1)
						aux_clone_db1 = copy.deepcopy(clone_db1)
						clone_db2 = copy.deepcopy(db2)
						aux_clone_db2 = copy.deepcopy(clone_db2)
						
						for atom in clone_db1:
							atom.map(mapping[key_pos])
						
						for atom in clone_db2:
							atom.map(mapping[key_pos])

						aux_result = True
						for atom1 in clone_db1:
							found = None
							for atom2 in clone_db2:
								if atom2 == atom1:
									found = atom2
							if not found is None:
								clone_db2.remove(found)
							else:
								aux_result = False
								break

						if aux_result:
							result = True
						

		return result

