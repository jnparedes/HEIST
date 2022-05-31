from Ontological.OntQuery import OntQuery
from constant import Constant
from variable import Variable
from atom import Atom
from ontological_netder.homomorphism import Homomorphism
from ATLAST.parsing import parser
from ATLAST.codegen.symtable import SymTable
from ATLAST.codegen.ir_generator import IRGenerator
from ATLAST.codegen.sql_generator import SQLGenerator
from ATLAST.dbbackend import schema as schema
import copy
import json
import mariadb
class AtomsHomomorphism(Homomorphism):

	#obtiene todos los posibles mapeos de un atomo "atom" en una base de datos "data_base"
	#la salida es un diccionario donde la clave es una transformacion en string del mapeo considerado y el valor el mapeo en si, este formato se utiliza para optimizar las busquedas posteriores
	#cada mapeo tiene la forma {'id_term_1': term_1, ... , 'id_term_n': term_n} donde term_1,...,term_n son objetos de la clase general Term
	#Variable, Constant y Null son tipos de Term
	#la transformacion de un mapeo resulta de contatenar la transformacion de cada elemento del mapeo
	#un elemento id_term:term del mapeo se transforma como '(' + str(id_term) + ',' + str(term) + ')'
	#ver clase Term para mas detalles de str(term)
	def get_atom_mapping(self, atom, data_base):
		result = {}
		for data in data_base:
			if atom.is_mapped(data):
				mapping = atom.get_mapping(data)
				key_mapping = ""
				for key in mapping.keys():
					key_mapping = key_mapping + '(' + str(key) + ',' + str(mapping[key]) + ')'
				result[key_mapping] = mapping
				if mapping == {}:
					break
		if len(result) == 0:
			result = None
		
		return result

	#busca todos los posibles mapeos entre un conjunto de atomos (atoms) y una base de datos (data_base)
	def get_atoms_mapping(self, atoms, data_base):
		#"aux_result" es un diccionario que almacena los posibles mapeos (podrian ser mapeos parciales, tal vez no todos los atomos fueron mapeados aun) que se van obteniendo
		#por lo tanto cada elemento del diccionario es un mapeo candidato
		#la clave del diccionario es un transformacion del mapeo a string (ver arriba "get_atom_mapping(self, atom, data_base)") y el valor el mapeo en si
		#inicialmente se tiene un unico elemento con clave '' y como valor un diccionario vacio
		aux_result = {'': {}}
		#"aux_mapped_atoms" es diccionario donde cada valor contiene los atomos "atoms" mapeados de acuerdo a cada posible mapeo de "aux_result"
		#las claves son transformaciones de los mapeos a strings
		#por lo tanto por cada posible mapeo hay un elemento en el diccionario con los atomos mapeados (tal vez parcialmente)
		#inicialmente no se ha realizado ningun mapeo por lo cual el diccionario tiene solo un elemento cuya clave es '' y
		#el valor es una copia de los atomos "atoms"
		aux_mapped_atoms = {'': copy.deepcopy(atoms)}

		for index in range(0, len(atoms)):
			#por cada iteracion se guardan todas la posibles formas (hasta el momento) de mapear los atomos en otro diccionario
			mapped_atoms = aux_mapped_atoms
			#por cada iteracion se guardan todos los posibles mapeos (hasta el momento) en otro diccionario
			result = aux_result
			#"aux_mapped_atoms" y "aux_result" se inicializan como diccionarios vacios y se recalculan en cada iteracion
			aux_mapped_atoms = {}
			aux_result = {}
			for ma_key in mapped_atoms.keys():
				#por cada posible forma de mapear la lista de atomos "atoms" (ma_key indica cual se esta considerando),
				#se elige el siguiente atomo (index indica cual atomo se elige) y se buscan todos sus posibles mapeos en "data_base"
				mapping = self.get_atom_mapping(mapped_atoms[ma_key][index], data_base)
				#se verifica si hay algun mapeo, si no hay tener en cuenta que "aux_mapped_atoms" y "aux_result" no se modifican
				#por lo tanto se descarta continuar con ese posible mapeo
				if (not mapping is None):
					for mapping_key in mapping.keys():
						#por cada nuevo mapeo obtenido "mapping_atom"
						#se copia en "other_mapping" el mapeo parcial "result[ma_key]" que se tiene hasta el momento
						other_mapping = copy.deepcopy(result[ma_key])
						#se actualiza "other_mapping" con el nuevo mapeo obtenido "mapping[mapping_key]"
						other_mapping.update(mapping[mapping_key])
						#cada nuevo mapeo agrega un nueva posibilidad de mapeo candidato, que se actualiza en "aux_result"
						aux_result[ma_key + mapping_key] = other_mapping
						#se crea un copia de la forma posible de mapear los atomos considerada "mapped_atoms[ma_key]"
						cloned_mapped_atoms = copy.deepcopy(mapped_atoms[ma_key])
						#cada atomo mapeado (tal vez parcialmente) es mapeado segun "mapping[mapping_key]"
						for otherAtom in cloned_mapped_atoms:
							otherAtom.map(mapping[mapping_key])
						#cada nueva forma posible de mapear los atomos, crea un nuevo elemento en "aux_mapped_atoms"
						aux_mapped_atoms[ma_key + mapping_key] = cloned_mapped_atoms

		return aux_result

