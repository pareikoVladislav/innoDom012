import os
from dotenv import load_dotenv

BASE_DIR = "/home/vladislav/Desktop/innoDom012"
env = load_dotenv(os.path.join(BASE_DIR, ".env"))
url_engine = f"postgresql://{os.getenv('DB_USER_POS')}:{os.getenv('DB_PASSWORD_POS')}\
@{os.getenv('DB_HOST_POS')}:{os.getenv('DB_PORT_POS')}/{os.getenv('DB_NAME_POS')}"
