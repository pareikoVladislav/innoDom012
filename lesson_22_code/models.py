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
from lesson_22_code.db_engine import url_engine

Base = declarative_base()


class User(Base):
    __tablename__: str = 'user'

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
    deleted_at = Column(TIMESTAMP)

    user = relationship('User', back_populates="phone_numbers")


db_connector = DBConnector(db_url=url_engine)
db_connector.create_tables(Base)
