import uuid

from src.backend.transactions.add_bulk.database import Exclusions, Decorator, UserCard, CardType


def seed_db(db):
    db.add(Exclusions(mcc=6051, percentage=100))
    db.add(Exclusions(mcc=9399, percentage=100))
    db.add(Exclusions(mcc=6540, percentage=100))

    db.add(Decorator(total_active=0, is_foreign=0, is_online=0))
    db.add(Decorator(total_active=1, is_foreign=0, is_online=1))
    db.add(Decorator(total_active=1, is_foreign=1, is_online=0))
    db.add(Decorator(total_active=2, is_foreign=1, is_online=1))

    import boto3
    import pandas as pd
    from io import StringIO
    import regex as re

    client = boto3.client('s3')
    bucket_name = 'batchuploadbucket'
    object_key = 'public/Project B (Appendix 2a) - spend.first.1000.csv'
    csv_obj = client.get_object(Bucket=bucket_name, Key=object_key)
    body = csv_obj['Body']
    csv_string = body.read().decode('utf-8')
    df = pd.read_csv(StringIO(csv_string))

    card_seeder = {}
    for row_dict in df.to_dict(orient="records"):
        if row_dict['card_id'] not in card_seeder:
            card_pan = re.sub('[^0-9]', '', row_dict['card_pan'])
            card_seeder[row_dict['card_id']] = [card_pan, row_dict['card_type']]
    for k, v in card_seeder.items():
        db.add(UserCard(card_id=k, user_id=uuid.uuid4(), card_pan=v[0], card_type=v[1]))

    db.commit()
