""" Starts a session for the DB call """
import enum
import uuid

# from pgsql.database import SessionLocal
from sqlalchemy import create_engine, ForeignKey, BIGINT, TypeDecorator, CHAR, Enum, inspect
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Float, Integer, Boolean
import json

from src.backend.Secret import pw, pw_dev

# connection
DATABASE_URL = "mysql+pymysql://root:" + pw_dev + "@localhost:3306/dev"
# "mysql+pymysql://admin:"+pw+"@database-1-instance-1.cqbbxkouucyk.us-east-1.rds.amazonaws.com:3306/cs301_scis_bank"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_session():
    """ Creates a db session """
    try:
        _db = SessionLocal()
        return _db
    finally:
        _db.close()


class GUID(TypeDecorator):
    """Platform-independent GUID type.

    Uses Postgresql's UUID type, otherwise uses
    CHAR(32), storing as stringified hex values.

    https://docs.sqlalchemy.org/en/14/core/custom_types.html?highlight=uuid#backend-agnostic-guid-type
    """
    impl = CHAR

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(UUID())
        else:
            return dialect.type_descriptor(CHAR(64))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == 'postgresql':
            return str(value)
        else:
            if not isinstance(value, uuid.UUID):
                return uuid.UUID(value)
            else:
                # hexstring
                return value

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            return uuid.UUID(value)


class CardType(enum.Enum):
    scis_platinummiles = 1
    scis_shopping = 2
    scis_freedom = 3
    scis_premiummiles = 4


class RewardType(enum.Enum):
    Points = 1
    Miles = 2
    Cashback = 3


class UserCard(Base):
    """
    Our user table storing the users and their cards
    """
    __tablename__ = 'usercard'
    card_id = Column(GUID, primary_key=True)
    user_id = Column(GUID, nullable=False)
    card_pan = Column(String(16), nullable=False)
    card_type = Column(Enum(CardType), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Decorator(Base):
    """
    A special table storing the special 'decorator' attributes of a Transaction and Exclusion
    """
    __tablename__ = 'decorator'
    id = Column(Integer, primary_key=True)
    total_active = Column(Integer)
    is_foreign = Column(Boolean)
    is_online = Column(Boolean)
    transaction = relationship("Transaction")
    rewardsprogram = relationship("RewardsProgram")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Transaction(Base):
    """
    Transactions received from user and processed before storing.
    """
    __tablename__ = 'transaction'
    id = Column(GUID, primary_key=True)
    transaction_id = Column(String(255), nullable=False)
    card_pan = Column(String(16), nullable=False)
    merchant = Column(String(255), nullable=False)
    mcc = Column(Integer, nullable=True)
    currency = Column(String(3), nullable=False)
    amount = Column(BIGINT, nullable=False)
    transaction_date: datetime = Column(DateTime, nullable=False)
    # Optional fields. If supplied we will validate regardless
    card_id = Column(GUID)
    card_type = Column(Enum(CardType))
    # Internal fields. We add them on our own
    user_id = Column(GUID)
    decorator_id = Column(Integer, ForeignKey("decorator.id"))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class RewardsProgram(Base):
    __tablename__ = 'rewardsprogram'
    id = Column(GUID, primary_key=True)
    card_type = Column(Enum(CardType), nullable=False)
    decorator_id = Column(Integer, ForeignKey("decorator.id"), nullable=False)
    Reward_Type = Column(Enum(RewardType), nullable=False)
    reward = Column(BIGINT, nullable=False)
    min_spend = Column(BIGINT, nullable=False)
    is_stackable = Column(Boolean, nullable=False)
    merchant = Column(String(255))


class Exclusions(Base):
    __tablename__ = 'exclusions'
    mcc = Column(Integer, primary_key=True)
    percentage = Column(Integer, nullable=False)


Base.metadata.create_all(engine)
