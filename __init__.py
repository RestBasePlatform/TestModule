from restbase_types import DatabaseTable
from restbase_types import DatabaseColumn
from restbase_types import DatabaseSchema
from restbase_types import Database
from restbase_types import DatabaseConnectionData
from restbase_types.server import ServerConnectionData
from typing import IO, List

def create_user():
    pass

def delete_user():
    pass


async def read_table_data(db_con_data: DatabaseConnectionData) -> List[DatabaseTable]:
    columns = [DatabaseColumn("column1", "text"), DatabaseColumn("column2", "integer")]
    table_names = ["table1", "table2"]
    schema_names = ["schema1", "schema2"]
    db_names = ["db1", "db2"]

    res = []

    for db in db_names:
        db_object = Database(db)
        for schema in schema_names:
            schema_object = DatabaseSchema(schema)
            for table in table_names:
                res.append(DatabaseTable(table, schema_object, db_object, columns))
    return res


async def healt_check(db_con_data: DatabaseConnectionData) -> bool:
    return True


async def create_on_server(db_con_data: DatabaseConnectionData, server_con_data: ServerConnectionData) -> bool:
    pass
