import uuid

from src.backend.transactions.add_bulk.database import Exclusions, Decorator, UserCard, CardType, RewardType, User


def seed_db(db):
    db.add(Exclusions(mcc=6051, reward_type=RewardType(1)))
    db.add(Exclusions(mcc=6051, reward_type=RewardType(2)))
    db.add(Exclusions(mcc=9399, reward_type=RewardType(1)))
    db.add(Exclusions(mcc=9399, reward_type=RewardType(2)))
    db.add(Exclusions(mcc=6540, reward_type=RewardType(1)))
    db.add(Exclusions(mcc=6540, reward_type=RewardType(2)))

    db.add(Decorator(total_active=0))
    db.add(Decorator(total_active=1, is_online=1))
    db.add(Decorator(total_active=1, is_foreign=1))
    db.add(Decorator(total_active=1, is_hotel=1))
    db.add(Decorator(total_active=2, is_online=1, is_foreign=1))
    db.add(Decorator(total_active=2, is_online=1, is_hotel=1))
    db.add(Decorator(total_active=2, is_foreign=1, is_hotel=1))
    db.add(Decorator(total_active=3, is_online=1, is_foreign=1, is_hotel=1))

    import boto3
    import pandas as pd
    from io import StringIO
    import regex as re

    client = boto3.client('s3')
    bucket_name = 'databaseseeding'
    object_key = 'users.csv'
    csv_obj = client.get_object(Bucket=bucket_name, Key=object_key)
    body = csv_obj['Body']
    csv_string = body.read().decode('utf-8')
    df = pd.read_csv(StringIO(csv_string))

    users = {}
    for row_dict in df.to_dict(orient="records"):
        card_pan = str(re.sub('[^0-9]', '', row_dict['card_pan']))
        card_pan_hash = hash(card_pan)
        card_pan_last = int(card_pan[-4:])
        card_type = row_dict['card_type']
        user_id = uuid.uuid4()
        db.add(UserCard(card_pan_hash=card_pan_hash, card_pan_last=card_pan_last, card_type=card_type,
                        user_id=user_id))
        if user_id not in users:
            users[user_id] = row_dict['email']

    for k, v in users.items():
        db.add(User(user_id=k, email=v))

    db.commit()
