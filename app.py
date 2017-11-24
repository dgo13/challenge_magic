#!flask/bin/python
from flask import Flask, jsonify, abort
from models import *
from csv_bd import CsvBd
import threading
from database import Database
from rabbit_mq import RabbitMq

app = Flask(__name__)

@app.route('/movecards/<int:expansion_id>', methods=['POST'])
def move_cards(expansion_id):
    expansion = Database.get_expansion(expansion_id)

    if expansion is None:
        abort(404)

    count_cards = send_cards_to_exchange(expansion.ExpansionId)
    return jsonify(expansion_name=expansion.Name, count=count_cards), 200

@app.route('/card/<string:card_id>', methods=['GET'])
def get_card(card_id):
    card = CsvBd.get_card(card_id)
    return jsonify(card), 200


@app.route("/moveall/", methods=['GET'])
def moveall():
    t = threading.Thread(target=move_expansions)
    t.start()
    return jsonify(result='success'), 202

def move_expansions():
    expansions = Database.get_all_expansions()
    for expansion in expansions:
        count_cards = send_cards_to_exchange(expansion.ExpansionId)
        print('Enviado {} cards do expansion id {}'.format(count_cards, expansion.ExpansionId))

def send_cards_to_exchange(expansion_id):
    cards = Database.get_cards(expansion_id)
    count_cards = cards.wrapped_count()

    RabbitMq.send(cards)
    
    return count_cards

if __name__ == '__main__':
    app.run()