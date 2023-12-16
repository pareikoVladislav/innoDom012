from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnector:
    def __init__(self, db_url):
        self.db_url = db_url
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def __enter__(self):
        self.session = self.Session()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def create_tables(self, base):
        base.metadata.create_all(self.engine)
