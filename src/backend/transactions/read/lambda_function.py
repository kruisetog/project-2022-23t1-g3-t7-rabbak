from src.backend.transactions.add_bulk.database import get_session, Transaction


def lambda_handler():
    res = []
    db = get_session()
    user_id = '54e19318-17e9-44f7-bea7-7d291d060540'
    data = db.query(Transaction).where(Transaction.user_id == user_id).all()
    for i in data:
        res.append(i.as_dict())
    return res


if __name__ == "__main__":
    print('end read', lambda_handler())
