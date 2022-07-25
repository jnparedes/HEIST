from ontological_netder.netder_query import NetDERQuery
from constant import Constant
from variable import Variable
from query import Query
from quantifier import Quantifier
from atom import Atom
from ontological_netder.homomorphism import Homomorphism
from ontological_netder.null import Null
from ATLAST.parsing import parser
from ATLAST.codegen.symtable import SymTable
from ATLAST.codegen.ir_generator import IRGenerator
from ATLAST.codegen.sql_generator import SQLGenerator
from ATLAST.dbbackend import schema as schema
from datetime import datetime
import copy
import json
import mariadb
import hashlib

class Mapping:
	    
		def __init__(self, terms, data):
			self._terms = terms
			self._data = data
			self._position = 0
	  
		def __iter__(self):
			return self

		def __next__(self): 
			if self._position == len(self._data):
				raise StopIteration
			else:
				result = {}
				new_mapping = {}
				index = 0
				key_mapping = ""

				for term in self._terms:
					value = self._data[self._position][index]
					if str(value)[:1] == "z" and str(value)[1:].isdigit():
						new_mapping[term.get_id()] = Null(value)
					else:
						new_mapping[term.get_id()] = Constant(value)
					key_mapping = key_mapping + '(' + str(term.get_id()) + ',' + str(new_mapping[term.get_id()]) + ')'
					index += 1
	            
				result[key_mapping] = new_mapping
				self._position += 1
	            
				return result
	    
		def __len__(self):
			return len(self._data)

class RDBHomomorphism(Homomorphism):
	NAME = "mapping"
	PK = "1_primary_key"
	TRANSLATE_TIME = datetime.strptime('00:00:00', '%H:%M:%S')
	HOMOMORPH_BUILT_TIME = datetime.strptime('00:00:00', '%H:%M:%S')
	HOMOMORPH_SQL_QUERY = datetime.strptime('00:00:00', '%H:%M:%S')
	def __init__(self, netder_kb):
		self._netder_kb = netder_kb
		self._sql_queries = {}

	def to_SQL(self, query):
		inicio_trans = datetime.now()
		string_query = str(query)
		if not (string_query in self._sql_queries):
			result = parser.parse_input(string_query)
			# Set up a symbol table and code generation visitor
		
			symbolTable = SymTable()
			codegenVisitor = IRGenerator(schema.Schema())
			sqlGeneratorVisitor = SQLGenerator()
			# Generate the symbol table
			
			result.generateSymbolTable(symbolTable)

			# Perform the code generation into SQLIR using the visitor
			result.accept(codegenVisitor)

			codegenVisitor._IR_stack[0].accept(sqlGeneratorVisitor)
			self._sql_queries[string_query] = sqlGeneratorVisitor._sql

		fin_trans = datetime.now()
		RDBHomomorphism.TRANSLATE_TIME += (fin_trans - inicio_trans)

		return self._sql_queries[string_query]
	
	
	#busca todos los posibles mapeos entre un conjunto de atomos (atoms) y una base de datos asociada a la base de conocimiento netder
	#historical_included indica si mapeos que ya hayan sido utilizados pueden ser incluidos en la respuesta
	#el parametro "id_atoms" se utiliza para diferenciar dos conjuntos de atomos sintacticamente iguales pero que corresponden a reglas diferentes
	#esto evita que una vez que un mapeo sea utilizado para el cuerpo de una regla luego ya no pueda ser utilizado para otra con un cuerpo sintacticamente igual
	def get_atoms_mapping(self, atoms):
		inicio_homomorph = datetime.now()
		
		exist_var = []
		for atom in atoms:
			pk_variable = atom.get_pk_variable()
			if not pk_variable is None:
				exist_var.append(pk_variable)

		query = Query(quantification = {Quantifier.EXISTENTIAL: exist_var}, atoms = {"ont_cond":atoms})
		
		sql_query = self.to_SQL(query)
		
		var_list = query.get_free_variables()

		con = self._netder_kb.get_connection()
		cur = con.cursor()

		inicio_sql = datetime.now()
		cur.execute(sql_query)
		fin_sql = datetime.now()
		RDBHomomorphism.HOMOMORPH_SQL_QUERY += (fin_sql - inicio_sql)

		data = cur.fetchall()
		con.commit()
		con.close()


		result = Mapping(var_list, data)


		fin_homomorph = datetime.now()
		RDBHomomorphism.HOMOMORPH_BUILT_TIME += (fin_homomorph - inicio_homomorph)

		return result
