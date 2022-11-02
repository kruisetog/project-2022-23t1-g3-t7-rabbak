from sqlalchemy import and_

from src.backend.transactions.add_bulk.database import Transaction, UserCard, Decorator

import regex as re


def process_transaction(db, data: Transaction, msg):
    data['card_pan'] = re.sub('[^0-9]', '', data['card_pan'])
    res = db.query(UserCard).filter(UserCard.card_pan == data['card_pan']).first().as_dict()

    # validate optional fields
    if 'card_id' in data:
        if str(data['card_id']) != str(res['card_id']):
            msg.append({data['transaction_id']: 'Card ID provided does not match the the card PAN provided'})
    else:
        data['card_id'] = str(res['card_id'])

    if 'card_type' in data:
        if str(data['card_type']) != str(res['card_type'].name):
            msg.append({data['transaction_id']: 'Card Type provided does not match the card PAN provided'})
    else:
        data['card_type'] = str(res['card_type'].name)

    # add internal fields
    data['user_id'] = res['user_id']
    if data['currency'] == 'SGD':
        res2 = db.query(Decorator).where(
            and_(Decorator.total_active == 1, Decorator.is_foreign == True)).first().as_dict()
    else:
        res2 = db.query(Decorator).where(Decorator.total_active == 0).first().as_dict()
    data['decorator_id'] = res2['id']

    db.add(Transaction(id=data['id'], transaction_id=data['transaction_id'], card_pan=data['card_pan'],
                       merchant=data['merchant'], mcc=data['mcc'], currency=data['currency'], amount=data['amount'],
                       transaction_date=data['transaction_date'], card_id=data['card_id'],
                       card_type=data['card_type'], user_id=data['user_id'], decorator_id=data['decorator_id']))

    db.commit()
