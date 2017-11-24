#!/usr/bin/env python
import json
import csv
from pathlib import Path

class CsvBd():

    def get_card(card_id):
        with open(CsvBd.db, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['GathererId'] == card_id:
                    return row
        
        return None
    
    def write_card(card):
        new_file = False
        my_file = Path(CsvBd.db)
        if not my_file.is_file():
            new_file = True

        with open(CsvBd.db, 'a') as csv_file:
            csvwriter = csv.writer(csv_file)
            if new_file:
                header = card.keys()
                csvwriter.writerow(header)
                new_file = False
            
            csvwriter.writerow(card.values())

    db = "/tmp/cards_db.txt"
