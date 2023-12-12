import environ
import os
from urllib.parse import quote

from sqlalchemy.exc import DisconnectionError

from lesson_21_code.db_conn import DBConnector
from lesson_21_code.models import User, PhoneBook

BASE_DIR = "/home/vladislav/Desktop/innoDom012"

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))


# db_url = f"postgresql://[user]:[password]@[host]:[port]/[db_name]"
db_url = f"postgresql://{env('DB_USER_POS')}:{quote(env('DB_PASSWORD_POS'))}@{env('DB_HOST_POS')}:\
{env('DB_PORT_POS')}/{env('DB_NAME_POS')}"


# front_user_form_data = {
#     "name": "Alex",
#     "surname": "John",
#     "age": 24,
#     "email": "alex.john@icloud.com",
#     "country": "USA",
#     "city": "Minnesota",
# }
#
# front_phone_form_data = {
#     "user_id": 1,
#     "number": "+1 787 55 41",
# }


# def create_new_user(manager, form_data):
#     user = User(**form_data)
#
#     manager.add(user)
#
#     manager.commit()
#
#
# def write_user_number(manager, form_data):
#     phone_number_data = PhoneBook(**form_data)
#
#     manager.add(phone_number_data)
#
#     manager.commit()
#
#
# with DBConnector(db_url=db_url) as session:
#     create_new_user(manager=session, form_data=front_user_form_data)
#     raise DisconnectionError("Something went wrong")
#     write_user_number(manager=session, form_data=front_phone_form_data)

front_user_form_data = {
    "name": "Andrew",
    "age": 30,
    "email": "andrew93@gmail.com",
    "country": "Belarus",
    "city": "Minsk",
}

front_phone_form_data = {
    "user_id": 2,
    "number": "+375 44 737 02 01",
}


def create_new_user(manager, form_data):
    user = User(**form_data)

    manager.add(user)
    raise DisconnectionError("Something went wrong")
    manager.commit()


def write_user_number(manager, form_data):
    phone_number_data = PhoneBook(**form_data)

    manager.add(phone_number_data)

    manager.commit()


with DBConnector(db_url=db_url) as session:
    try:
        create_new_user(manager=session, form_data=front_user_form_data)
        write_user_number(manager=session, form_data=front_phone_form_data)
    except DisconnectionError:
        session.rollback()

