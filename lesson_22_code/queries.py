import json
from datetime import datetime

from sqlalchemy.orm import joinedload

from lesson_22_code.db_conn import DBConnector
from lesson_22_code.models import User, PhoneBook
from lesson_22_code.db_engine import url_engine
from sqlalchemy import or_, and_

# front_user_form_data = [
#     {"name": "Alex", "surname": "John", "age": 24, "email": "alex.john@icloud.com", "country": "USA", "city": "Oustin"},
#     {"name": "Diana", "surname": "Julis", "age": 18, "email": "di.julis@icloud.com", "country": "USA",
#      "city": "New York"},
#     {"name": "Irina", "surname": None, "age": 26, "email": "irina97@gmail.com", "country": "USA", "city": "Oustin"},
#     {"name": "Artsiom", "surname": "Rart", "age": 30, "email": "art.rart@gmail.com", "country": "USA",
#      "city": "Minnesota"},
#     {"name": "John", "surname": "Black", "age": 18, "email": "johnblack@icloud.com", "country": "USA",
#      "city": "New York"},
#     {"name": "Alex", "surname": "Grey", "age": 18, "email": "alex.g@gmail.com", "country": "USA", "city": "Ohio"},
#     {"name": "Nika", "surname": None, "age": 16, "email": "nika08@icloud.com", "country": "USA", "city": "Oustin"},
#     {"name": "Alexis", "surname": "Steall", "age": 22, "email": "a.steall@icloud.com", "country": "USA",
#      "city": "Ohio"},
#     {"name": "Vlad", "surname": "Novikov", "age": 23, "email": "novikov.vlad@gmail.com", "country": "Canada",
#      "city": "Ontario"},
#     {"name": "Diana", "surname": "Dubruch", "age": 25, "email": "dubrich.di@gmail.com", "country": "USA",
#      "city": "Minnesota"},
#     {"name": "Pavel", "surname": "Yakovlev", "age": 25, "email": "pavel.yakov@mail.ru", "country": "USA",
#      "city": "New York"},
#     {"name": "Sergey", "surname": "Vysocky", "age": 20, "email": "serg.vysocky@mail.ru", "country": "USA",
#      "city": "Oustin"},
#     {"name": "Sergey", "surname": None, "age": 32, "email": "sergey.anon@icloud.com", "country": "USA",
#      "city": "Minnesota"},
#     {"name": "Dima", "surname": None, "age": 24, "email": "dmitry99@gmail.com", "country": "USA", "city": "Minnesota"},
#     {"name": "Valeriya", "surname": None, "age": 28, "email": "valeriya.a@icloud.com", "country": "Canada",
#      "city": "Ontario"},
#     {"name": "Kseniya", "surname": "Borod", "age": 28, "email": "borod.ksu@gmail.com", "country": "USA",
#      "city": "Oustin"},
#     {"name": "Ken", "surname": "Klark", "age": 24, "email": "klark.ken@icloud.com", "country": "USA",
#      "city": "Minnesota"},
#     {"name": "Isak", "surname": "Nuut", "age": 31, "email": "isek.nuut@icloud.com", "country": "USA",
#      "city": "Minnesota"},
#     {"name": "Julia", "surname": "Borsich", "age": 17, "email": "borsich.jul@icloud.com", "country": "Canada",
#      "city": "Ontario"},
#     {"name": "Nasty", "surname": "Golovach", "age": 18, "email": "nancy.golovach@icloud.com", "country": "USA",
#      "city": "Ohio"},
#     {"name": "Mariya", "surname": "Ambrazh", "age": 18, "email": "amb.masha@icloud.com", "country": "USA",
#      "city": "Minnesota"},
#     {"name": "Julia", "surname": None, "age": 18, "email": "julia05@gmail.com", "country": "USA", "city": "Oustin"},
#     {"name": "Alex", "surname": None, "age": 24, "email": "alex.anon@mail.ru", "country": "USA", "city": "Minnesota"},
#     {"name": "Vlad", "surname": "Kit", "age": 35, "email": "vlad.kit@gmail.com", "country": "USA", "city": "New York"},
#     {"name": "Sergey", "surname": "Bereziovky", "age": 35, "email": "serg.berezovsky@mail.ru", "country": "Canada",
#      "city": "Ontario"},
#     {"name": "Agness", "surname": None, "age": 37, "email": "youragness@mail.ru", "country": "USA",
#      "city": "Minnesota"},
#     {"name": "Mila", "surname": None, "age": 18, "email": "mila05@mail.ru", "country": "USA", "city": "Oustin"},
#     {"name": "Masha", "surname": "Shick", "age": 27, "email": "shick.masha@gmail.com", "country": "USA",
#      "city": "New York"},
#     {"name": "Dima", "surname": "Golubev", "age": 27, "email": "golubevdima@icloud.com", "country": "USA",
#      "city": "Ohio"},
#     {"name": "Vlad", "surname": "Grich", "age": 27, "email": "grichvlad@icloud.com", "country": "USA",
#      "city": "Minnesota"},
# ]
#
# front_phone_form_data = [
#     {"user_id": 2, "number": "+1 787 55 41"},
#     {"user_id": 2, "number": "+1 848 54 41"},
#     {"user_id": 3, "number": "+1 112 12 84"},
#     {"user_id": 4, "number": "+1 88 225 21"},
#     {"user_id": 5, "number": "+1 77 121 223"},
#     {"user_id": 6, "number": "+1 454 11 23"},
#     {"user_id": 5, "number": "+1 888 55 55"},
#     {"user_id": 7, "number": "+1 11 125 77"},
#     {"user_id": 8, "number": "+1 555 98 99"},
#     {"user_id": 9, "number": "+1 121 87 21"},
#     {"user_id": 10, "number": "+1 887 332 11"},
#     {"user_id": 11, "number": "+1 122 89 88"},
#     {"user_id": 12, "number": "+1 777 112 25"},
#     {"user_id": 13, "number": "+1 891 56 52"},
#     {"user_id": 13, "number": "+1 358 74 12"},
#     {"user_id": 14, "number": "+1 874 69 32"},
#     {"user_id": 15, "number": "+1 528 27 74"},
#     {"user_id": 16, "number": "+1 735 91 98"},
#     {"user_id": 17, "number": "+1 537 95 16"},
#     {"user_id": 18, "number": "+1 987 12 13"},
#     {"user_id": 19, "number": "+1 144 55 88"},
#     {"user_id": 20, "number": "+1 17 774 55"},
#     {"user_id": 21, "number": "+1 159 54 365"},
#     {"user_id": 22, "number": "+1 444 98 88"},
#     {"user_id": 23, "number": "+1 12 774 655"},
#     {"user_id": 24, "number": "+1 454 441 323"},
#     {"user_id": 25, "number": "+1 445 55 31"},
#     {"user_id": 26, "number": "+1 999 11 11"},
#     {"user_id": 27, "number": "+1 40 151 131"},
#     {"user_id": 28, "number": "+1 99 484 666"},
#     {"user_id": 29, "number": "+1 666 66 66"},
#     {"user_id": 30, "number": "+1 551 551 5"},
#     {"user_id": 22, "number": "+1 121 198 73"},
#     {"user_id": 17, "number": "+1 645 56 35"},
#     {"user_id": 9, "number": "+1 25 73 745"},
# ]
#
#
# def create_user(manager, form_data):
#     try:
#         for row in form_data:
#             user = User(**row)
#             manager.add(user)
#         manager.commit()
#     except:
#         manager.rollback()
#
#
# def write_users_numbers(manager, form_data):
#     try:
#         for row in form_data:
#             phone_obj = PhoneBook(**row)
#
#             manager.add(phone_obj)
#         manager.commit()
#     except:
#         manager.rollback()
#
#
# with DBConnector(db_url=url_engine) as session:
#     create_user(manager=session, form_data=front_user_form_data)
#     write_users_numbers(manager=session, form_data=front_phone_form_data)

# with DBConnector(db_url=url_engine) as session:
    # users = session.query(User).all()
    #
    # for user in users:
    #     print(f"User's name - {user.name}. User's email - {user.email}")
    # user = session.query(User).filter(
    #     User.id == 551
    # ).all()

    # print(user)

    # if user:
    #     print(f"User's name - {user.name}. User's email - {user.email}")
    # else:
    #     print([])


# with DBConnector(db_url=url_engine) as session:
    # users = session.query(User).filter(
    #     User.email.endswith('mail.ru')
    # )

    # users = session.query(User).filter(
    #     User.email.like("%mail.ru")
    # )

    # users = session.query(User).filter_by(
    #     name='Julia'
    # )

    # users = session.query(User).where(
    #     and_(User.age < 19, User.name.like('A%'))
    # ).count()

    # users = session.query(User).where(
    #     User.email.like('%gmail.com')
    # ).count()
    #
    # print(f"Кол-во пользователей младше 19, или с опр. именем - {users}")

    # users = session.query(User).filter(
    #     or_(User.age < 18, User.name.like('N%'))
    # )  #.order_by(User.age)

    # if users:
    #     for user in users:
    #         print(f"User's name - {user.name}. User's age - {user.age} User's email - {user.email}")
    # else:
    #     print([])

# with DBConnector(db_url=url_engine) as session:
    # user = session.query(User).options(
    #     joinedload(User.phone_numbers)
    # ).filter(User.id == 17).one()

    # user = session.query(User).options(
    #     joinedload(User.phone_numbers)
    # ).filter(User.id == 17).one()
    #
    # user_data = {
    #     "id": user.id,
    #     "name": user.name,
    #     "surname": user.surname,
    #     "age": user.age,
    #     "email": user.email,
    #     "country": user.country,
    #     "city": user.city,
    #     "phone_numbers": [phone.number for phone in user.phone_numbers]
    # }
    #
    # user_json_data = json.dumps(user_data, indent=4)

# print(user_json_data)

# where category in {(', '.join(category for category in request.get('film').get("categories")}))


# def update_user_data(manager, request):
#     try:
#         user = manager.query(User).filter(
#             User.id == request.get('user_id')
#         ).one()
#
#         phone = manager.query(PhoneBook).filter(
#             PhoneBook.user_id == user.id,
#             PhoneBook.number == request.get('body').get('old_number')
#         ).one()
#
#         if user:
#             user.surname = request.get('body').get('surname')
#             user.age = request.get('body').get('age')
#             user.updated_at = datetime.now()
#
#             manager.commit()
#
#         if phone:
#             phone.number = request.get('body').get('new_number')
#             phone.updated_at = datetime.now()
#
#             manager.commit()
#     except:
#         manager.rollback()
#
#
# request_data = {
#     "user_id": 21,
#     "body": {
#         "email": "amb.masha@icloud.com",
#         "surname": "TEST SURNAME",
#         "age": 19,
#         "old_number": "+2 787 46 218",
#         "new_number": "+3 777 555 666"
#     }
# }
#
# with DBConnector(db_url=url_engine) as session:
#     update_user_data(
#         manager=session,
#         request=request_data
#     )
