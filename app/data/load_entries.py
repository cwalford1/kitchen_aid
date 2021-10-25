import dataBase as db
import sqlite3 as sl

database=db.DataBase('Ingredients_Inventory.db')
database.create_table('Ingredients')
