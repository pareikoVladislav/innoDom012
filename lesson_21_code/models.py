from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    TIMESTAMP,
    ForeignKey,
    Boolean,
    func
)
from sqlalchemy.orm import (
    relationship,
    declarative_base,
)
from lesson_21_code.db_conn import DBConnector

import environ
import os
from urllib.parse import quote

BASE_DIR = "/home/vladislav/Desktop/innoDom012"

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))


# db_url = f"postgresql://[user]:[password]@[host]:[port]/[db_name]"
db_url = f"postgresql://{env('DB_USER_POS')}:{quote(env('DB_PASSWORD_POS'))}@{env('DB_HOST_POS')}:\
{env('DB_PORT_POS')}/{env('DB_NAME_POS')}"

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    surname = Column(String(30))
    age = Column(Float, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    country = Column(String(40), nullable=False)
    city = Column(String(30))
    deleted = Column(Boolean, server_default="False")
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP)

    phone_numbers = relationship("PhoneBook", back_populates="user")


class PhoneBook(Base):
    __tablename__ = 'phonebook'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    number = Column(String(50))
    deleted = Column(Boolean, server_default="False")
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP)

    user = relationship('User', back_populates="phone_numbers")


db_connector = DBConnector(db_url=db_url)
db_connector.create_tables(Base)
