import sqlite3
from sqlite3 import Error
from datetime import datetime
import time


# Constants
FILE = "applications.db"
APPLICATIONS_TABLE = "Applications"
USERS_TABLE = "Users"


class Database:
    """
    used to connect, write to and read from a local sqlite3 database
    """
    def __init__(self):
        """
        try to connect to file and create cursor
        """
        self.conn = None
        try:
            self.conn = sqlite3.connect(FILE)
        except Error as e:
            print(e)

        self.cursor = self.conn.cursor()
        self.create_app_table()
        self.create_user_table()

    def close(self):
        """
        close the db connection
        :return: None
        """
        self.conn.close()

    def create_app_table(self):
        """
        create new app database table if one doesn't exist
        :return: None
        """
        query = f"""CREATE TABLE IF NOT EXISTS {APPLICATIONS_TABLE}
                    (username TEXT, content TEXT, time Date, id INTEGER PRIMARY KEY AUTOINCREMENT)"""
        self.cursor.execute(query)
        self.conn.commit()

    def create_user_table(self):
        """
        create new user database table if one doesn't exist
        :return: None
        """
        query = f"""CREATE TABLE IF NOT EXISTS {USERS_TABLE}
                    (name TEXT NOT NULL, email TEXT NOT NULL, password TEXT, time Date, id INTEGER PRIMARY KEY AUTOINCREMENT)"""
        self.cursor.execute(query)
        self.conn.commit()
    
    def save_new_user(self, name, email, password):
        """
        create new user entry in table
        :param name: str
        :param email: str
        :param password: str
        :return: None
        """
        query = f"INSERT INTO {USERS_TABLE} VALUES (?, ?, ?, ?, ?)"
        self.cursor.execute(query, (name, email, password, datetime.now(), None))
        self.conn.commit()

    def get_user_info(self, email):
        """
        returns specified user information
        :param email: str
        :return: None
        """
        query = f"SELECT * FROM {USERS_TABLE} WHERE EMAIL = ?"
        self.cursor.execute(query, (email,))

        return self.cursor.fetchall()

    