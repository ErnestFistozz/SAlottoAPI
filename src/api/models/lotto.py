from pymongo import MongoClient

CONNECTION_STRING = f'mongodb://{MONGO_DB_USER}:{MONGO_DB_PASSWORD}@{MONGO_DB_URL}'


class Database:
    def __init__(self, db_name: str):
        self.database_name = db_name
        self.client = MongoClient(CONNECTION_STRING)
        self.db = self.client[self.database_name]

    def create_database(self):
        return self.db


if __name__ == '__main__':
    db = Database('lotto-api')
    database = db.create_database()
