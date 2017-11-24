#!/usr/bin/env python
import json
import csv
from rabbit_mq import RabbitMq
from pathlib import Path
from csv_bd import CsvBd

def callback(ch, method, properties, body):   
    card = json.loads(body)
    CsvBd.write_card(card)

RabbitMq.receive(callback)
