#!flask/bin/python
import peewee
from peewee import *
import pymysql
from playhouse.shortcuts import *
from connection import Connection

class MySQLModel(peewee.Model):
    class Meta:
        database = Connection.db

class magiccard(MySQLModel):
    GathererId = CharField(primary_key=True)
    Variation = SmallIntegerField()
    SearchName = TextField()
    PtBRSearchName = TextField()
    EnglishName = TextField()
    PtBRName = TextField()
    LinkName = TextField()
    Color = IntegerField()
    ManaCost = CharField()
    CollectionNumber = SmallIntegerField()
    ConvertedManaCost = FloatField()
    Rarity = CharField()
    Rules = TextField()
    FlavorText = TextField()
    SuperTypes = IntegerField()
    CardTypes = IntegerField()
    UnseriousSubTypes = CharField()
    Power = CharField()
    Toughness = CharField()
    Loyalty = CharField()
    ExpansionId = IntegerField()
    ArtistId = IntegerField()
    FlipName = TextField()
    FlipRules = TextField()
    FlipSuperTypes = IntegerField()
    FlipTypes = IntegerField()
    FlipPower = CharField()
    FlipToughness = CharField()
    FlipGathererId = CharField()
    SplitManaCost = CharField()
    SplitConvertedManaCost = FloatField()

class magicexpansion(MySQLModel):
    ExpansionId = IntegerField(primary_key=True)
    Name = TextField()
    PtBRName = TextField()
    LinkName = TextField()
    Code = CharField()
    LaunchDate = DateTimeField()
    ExpansionCategoryId = SmallIntegerField()
    IsPromo = BooleanField()
    IsLegal = BooleanField()