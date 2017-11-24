#!flask/bin/python
import peewee
from peewee import *


class Connection():
    db = peewee.MySQLDatabase("tcgplace", host="127.0.0.1", port=3306, user="root", passwd="root")
    