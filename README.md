# **HEIST**
The directory [netder_instantiation](https://github.com/jnparedes/HEIST/tree/netder_from_heist/arch/netder_instantiation) contains all the necessary information required for performing the basic setup of a NetDER instantiation example. Instructions for running this NetDER instantiation are as follows:
- Install all the python dependencies.
- The knowledge base is implemented based on a DBMS, and in this case we use MariaDB; if you wish to use a different DBMS, then you need to adapt the [RDBHomomorphism](https://github.com/jnparedes/HEIST/blob/netder_from_heist/arch/ontological_netder/rdb_homomorphism.py) and [NetDERKB](https://github.com/jnparedes/HEIST/blob/netder_from_heist/arch/ontological_netder/netder_kb.py) classes to support other driver connectors.
- Create a MariaDB instance based on the structure defined in the [test.sql](https://github.com/jnparedes/HEIST/blob/netder_from_heist/arch/netder_instantiation/test.sql) file.
- The DB connection data is defined in the [config_db.json](https://github.com/jnparedes/HEIST/blob/netder_from_heist/arch/netder_instantiation/config_db.json) file.
- The DB schema is defined in [schema.xml](https://github.com/jnparedes/HEIST/blob/netder_from_heist/arch/netder_instantiation/schema.xml).
- [test_main.py](https://github.com/jnparedes/HEIST/blob/netder_from_heist/arch/netder_instantiation/test_main.py) file contains three different tests that can be executed once all the above steps have been completed.
