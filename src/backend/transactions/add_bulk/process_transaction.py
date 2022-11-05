import uuid
from datetime import datetime
from currency_converter import CurrencyConverter

from src.backend.transactions.add_bulk.database import UnprocessedTransactions, UserCard, Decorator, CardType

import regex as re


def process_transaction(db, data, msg):
    # validate compulsory fields
    if not isinstance(data['mcc'], int):
        msg.append({data['transaction_id']: f'MCC {data["mcc"]} must be an integer.'})
        return
    if data['mcc'] <= 0:
        msg.append({data['transaction_id']: f'MCC {data["mcc"]} must more than 0.'})
        return

    if not isinstance(data['amount'], float):
        msg.append({data['transaction_id']: f'Amount {data["amount"]} must be an integer.'})
        return
    if data['amount'] <= 0:
        msg.append({data['transaction_id']: f'Amount {data["amount"]} must more than 0.'})
        return

    if not isinstance(data['transaction_date'], datetime):
        msg.append({data['transaction_id']: f'Transaction date {data["transaction_date"]} must be a valid date.'})
        return

    card_pan = re.sub('[^0-9]', '', str(data['card_pan']))
    if len(card_pan) != 16:
        msg.append({data['transaction_id']: f'Card PAN {data["card_pan"]} must be 16 digits long.'})
        return

    res = db.query(UserCard).filter(UserCard.card_pan_hash == hash(card_pan)).first().as_dict()

    # validate optional fields
    if 'card_type' in data:
        if data['card_type'] not in CardType.name:
            msg.append({data['transaction_id']: f'Card Type {data["card_type"]} is invalid.'})
            return
        if str(data['card_type']) != str(res['card_type'].name):
            msg.append({data['transaction_id']: 'Card Type provided does not match the the card PAN provided'})
            return
    data['card_type'] = str(res['card_type'].name)

    # add internal fields
    data['user_id'] = res['user_id']

    is_foreign = data['currency'] == 'SGD'
    is_hotel = 3500 <= int(data['mcc']) <= 3999
    is_online = 5815 <= int(data['mcc']) <= 5818
    total_active = sum([is_foreign, is_hotel, is_online])
    res2 = db.query(Decorator).where((Decorator.total_active == total_active) &
                                     (Decorator.is_foreign == is_foreign) &
                                     (Decorator.is_hotel == is_hotel) &
                                     (Decorator.is_online == is_online)).first().as_dict()
    data['decorator_id'] = res2['decorator_id']

    c = CurrencyConverter()
    data['amount'] = c.convert(data['amount'], data['currency'], 'SGD')

    try:
        db.add(
            UnprocessedTransactions(transaction_id=uuid.uuid4(), merchant=data['merchant'],
                                    mcc=data['mcc'], amount=data['amount'], transaction_date=data['transaction_date'],
                                    card_type=data['card_type'], user_id=data['user_id'],
                                    decorator_id=data['decorator_id']))
    except ValueError:
        msg.append({data['transaction_id']: 'An error occurred while attempting database storage.'})

    db.commit()
