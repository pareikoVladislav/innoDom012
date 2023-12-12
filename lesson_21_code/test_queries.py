# import psycopg2
# import environ
# import os
# from urllib.parse import quote
#
# BASE_DIR = "/home/vladislav/Desktop/innoDom012"
#
# env = environ.Env()
# environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
#
#
# connection = psycopg2.connect(
#     dbname=env('DB_NAME_POS'),
#     user=env('DB_USER_POS'),
#     password=env('DB_PASSWORD_POS'),
#     host=env('DB_HOST_POS'),
#     port=env('DB_PORT_POS')
# )
#
# cursor = connection.cursor()
#
# #
# # cursor.execute("""
# #     CREATE TABLE IF NOT EXISTS "user" (
# #         id INT PRIMARY KEY,
# #         name VARCHAR(25) NOT NULL,
# #         surname VARCHAR(30),
# #         age FLOAT NOT NULL,
# #         email VARCHAR(80) UNIQUE NOT NULL,
# #         country VARCHAR(35) NOT NULL,
# #         city VARCHAR(25),
# #         deleted BOOLEAN DEFAULT FALSE,
# #         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# #         updated_at TIMESTAMP DEFAULT NULL
# #     )
# # """)
# #
# # cursor.execute(
# #     """
# #     CREATE TABLE IF NOT EXISTS Phone_book (
# #         id INT PRIMARY KEY,
# #         user_id INT,
# #         number VARCHAR(50),
# #         deleted BOOLEAN DEFAULT FALSE,
# #         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# #         updated_at TIMESTAMP DEFAULT NULL,
# #         FOREIGN KEY (user_id) REFERENCES "user"(id)
# #     )
# #     """
# # )
# #
# # connection.commit()
# # connection.close()
#
# # cursor.execute(
# #     """
# #     INSERT INTO "user" (id, name, surname, age, email, country, city)
# #     VALUES
# #     (1, 'Alex', 'Storm', 24, 'a.storm99@gmail.com', 'USA', 'Texas'),
# #     (2, 'Julia', 'Morrow', 29, 'jull.morrow94@gmail.com', 'Canada', 'Ottawa'),
# #     (3, 'Kseniya', 'Michurik', 21, 'ksu.michurik02@mail.ru', 'Russia', 'Moscow'),
# #     (4, 'Dmitry', 'Schypak', 32, 'dmitry.schypak89@mail.ru', 'Belarus', 'Minsk')
# #     """
# # )
# #
# # cursor.execute(
# #     """
# #     INSERT INTO Phone_book (id, user_id, number)
# #     VALUES
# #     (1, 2, '+1 (252) 789-21-11'),
# #     (2, 3, '+17 646-123-78'),
# #     (3, 1, '+7 931 656-78-89'),
# #     (4, 4, '+375 29 878-45-22')
# #     """
# # )
#
#
# def select_all_data_from_table(table_name):
#     return f"SELECT * FROM {table_name}"
#
#
# cursor.execute(select_all_data_from_table("Phone_book"))
# rows = cursor.fetchall()
#
# for row in rows:
#     print(row)
#
# # connection.commit()
# connection.close()
