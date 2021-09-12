from restbase_types import DatabaseTable
from restbase_types import DatabaseColumn
from restbase_types import DatabaseSchema
from restbase_types import Database
from restbase_types import DatabaseConnectionData
from typing import List
import socket


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


async def health_check(db_con_data: DatabaseConnectionData) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((db_con_data.host, db_con_data.port))

    if result != 0:
        return False
    return True
