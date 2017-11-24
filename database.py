#!flask/bin/python
import peewee
from peewee import *
import pymysql
from playhouse.shortcuts import *
from models import *
from connection import Connection


class Database():
    def get_expansion(expansion_id):
        Connection.db.get_conn()
        expansions = magicexpansion.select().where(magicexpansion.ExpansionId == expansion_id).limit(1)
        Connection.db.close()

        if  len(expansions) > 0:
            return expansions[0]
        else:
            return None

    def get_all_expansions():
        Connection.db.get_conn()
        expansions = magicexpansion.select()
        Connection.db.close()
        return expansions

    def get_cards(expansion_id):
        Connection.db.get_conn()
        cards = magiccard.select().where(magiccard.ExpansionId == expansion_id)
        Connection.db.close()
        return cards
    