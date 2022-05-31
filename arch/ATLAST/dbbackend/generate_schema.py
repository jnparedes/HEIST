import xml.etree.cElementTree as ET
import lxml.etree as etree
import psycopg2
from postgres import postgres_backend as pg
import config_parser as cp
import mariadb
import os

dbname_query = \
    """
    SELECT database() AS dbname
    """
'''
table_query = \
    """
    SELECT table_name
    FROM   information_schema.tables
    WHERE  table_schema = 'public'
  """'''
table_query = \
    """
    SHOW TABLES FROM test
    """

'''
primary_key_query = \
  """
    SELECT pg_attribute.attname,
           format_type(pg_attribute.atttypid, pg_attribute.atttypmod)
    FROM   pg_index, pg_class, pg_attribute
    WHERE  pg_class.oid = '%s'::regclass AND
           indrelid = pg_class.oid AND
           pg_attribute.attrelid = pg_class.oid AND
           pg_attribute.attnum = any(pg_index.indkey) AND
           indisprimary
  """
'''

primary_key_query = \
  """
    SELECT kcu.column_name FROM information_schema.table_constraints tco JOIN information_schema.key_column_usage kcu on tco.constraint_schema = kcu.constraint_schema 
    AND tco.constraint_name = kcu.constraint_name AND tco.table_name = kcu.table_name WHERE tco.constraint_type = 'PRIMARY KEY' 
    AND tco.table_schema not in ('sys','information_schema', 'mysql', 'performance_schema') 
    AND tco.table_schema = 'test' AND tco.table_name = ?

  """

columns_query = \
  """
    SELECT column_name, data_type, ordinal_position
    FROM information_schema.columns
    WHERE table_name = ?
    ORDER BY ordinal_position
  """

def generate_db_schema(con):
  # Create schema entries for each table
  cur = con.cursor()
  #dbname = pg.query(con, dbname_query)['rows'][0][0]
  
  root = etree.Element("root")
  cur.execute(dbname_query)
  for dbname in cur:
    print('-------dbname-------', dbname[0])
    dbname_node = etree.SubElement(root, "dbname")
    dbname_node.text = dbname[0]
  
  #tables = pg.query(con, table_query).get('rows')
  cur.execute(table_query)
  tables = cur.fetchall()
  '''
  if tables is None:
    msg = "ERROR: Tables query returned no data in generate_db_schema."
    print(msg)
    raise Exception(msg)'''

  for table in tables:
    # Create a structure with the name of the table
    print('------------table[0])------', table[0])
    xmltable = etree.SubElement(root, "table")
    xmltable.set("name", table[0])

    # Fetch all the primary keys and update the XML accordingly
    #keys = pg.query(con, primary_key_query % table)['rows']
    cur.execute(primary_key_query, (table[0],))
    for key in cur:
      print('---por aca---')
      print('----key[0]----', key[0])
      xml_primary_key = etree.SubElement(xmltable, "primaryKey")
      xml_primary_key.text = key[0]

    # Fetch all the columns and update the XML accordingly
    #columns = pg.query(con, columns_query % table)['rows']
    cur.execute(columns_query, (table[0],))
    for column in cur:
      xml_column = etree.SubElement(xmltable, "column")
      xml_column.set("name", column[0])
      xml_column_type = etree.SubElement(xml_column, "type")
      xml_column_type.text = column[1]
      xml_column_ordinal = etree.SubElement(xml_column, "ordinal")
      xml_column_ordinal.text = str(column[2])

  # Write the xml to a file
  tree = ET.ElementTree(root)
  tree.write(os.path.dirname(os.path.realpath(__file__)) +  '/' + "schema.xml")

  # TODO add try - catch to catch errors

if __name__ == "__main__":
  config_data = cp.parse_file('dbbackend/db.cfg')
  #con = pg.connect(config_data)
  try:
    con = mariadb.connect(
        user="root",
        password="",
        host="localhost",
        port=3306,
        database="test"

    )
  except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
  if con is None:
    print('HOLAAAAAAAAA')
  generate_db_schema(con)
