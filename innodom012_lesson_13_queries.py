import sqlite3


class Database:
    _instance = None

    def __init__(self):
        self.connection = sqlite3.connect('test.db')
        self.cursor = self.connection.cursor()
        # Инициализация базы данных, например, создание таблиц.

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def execute(self, query, params=None):
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        return self.cursor

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()


db_instance1 = Database.get_instance()
db_instance2 = Database.get_instance()

print(f"Обе переменные ссылаются на один и тот же объект класса? - {db_instance1 is db_instance2}")


def create_table_if_not_exists(table_name):
    return f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, data TEXT)"


def insert_data_in_table(table_name, user_text):
    return f"INSERT INTO {table_name} (data) VALUES (?)", (user_text,)


def get_all_data_from_the_table(table_name):
    return f"SELECT * FROM {table_name}"


user_text = input("Enter some text: ")

db_instance1.execute(create_table_if_not_exists("example"))

query, params = insert_data_in_table("example", user_text)
db_instance1.execute(query, params)
db_instance1.commit()

for row in db_instance2.execute(get_all_data_from_the_table("example")):
    print(row)
# HELLO FROM THE DATABASE IN MEMORY
