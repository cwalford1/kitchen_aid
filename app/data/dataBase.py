"""Module containing DataBase object"""

from __future__ import annotations
import sqlite3 as sl
from typing import List

class Table(object):
    """reference to database table"""
    def __init__(self,database: str,tablename: str) -> None:
        """forms database connection"""
        self.name=tablename
        self.connection=sl.connect(database)
        self.cursor=self.connection.cursor()

    def add_field(self,fieldname: str ,modifiers: List[str])->None:
        modstring=""
        for mod in modifiers:
            modstring+=mod
        self.cursor.execute(f"""
        ALTER TABLE {self.name}
        ADD {fieldname} {modstring}
        """)

    def add_entry(self):
        pass
    
    def get_fields(self)->List:
        return [description[0] for description in self.cursor.description]


class DataBase(object):
    """Object representing SQL database"""

    def __init__(self,dbase:str)->None:
        """creates connection to <dbase>
        Args:
            dbase (str): [name of database to connect]
        """
        self.connection=sl.connect(dbase)
        self.cursor=self.connection.cursor()
        self.name=dbase
    
    def create_table(self,table_name:str)->Table:
        """Creates SQL table."""
        self.cursor.execute(f"""CREATE TABLE {table_name} (
            id int PRIMARY KEY
        );""")
        self.connection.commit()
        return self.get_table(table_name)
    
    def get_tables(self)->list:
        return self.cursor.execute("""SELECT name FROM sqlite_master WHERE type='table';""").fetchall()

    def get_table(self,table_name: str)->Table:
        return Table(self.name,table_name)

    def query(self,query)->str:
        return self.cursor.execute(query).fetchall()

if __name__ == "__main__":
    db=DataBase('Ingredients_Inventory.db')
    t_table=db.create_table('test_table')
    tables=db.get_tables()
    print(tables)
