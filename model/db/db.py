# -*- coding: utf-8 -*-
from pymongo import MongoClient
import os


class DB(object):
    """docstring for DB."""

    def __init__(self):
        """Instancia o banco de dados."""
        dbpswd = os.environ["DATABASE_PSWD"]
        dbuser = os.environ["DATABASE_USER"]

        client = MongoClient('localhost', username=dbuser, password=dbpswd,
                             authMechanism='SCRAM-SHA-256')

        self.db = client.bd2

    def get_db_pac(self):
        """Retorna a classe do banco."""
        return self.db.pacientes

    def get_db_img(self):
        """Retorna a classe do banco."""
        return self.db.img
