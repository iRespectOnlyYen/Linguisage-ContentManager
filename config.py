from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")


static_path = "app/static"
static_access_http_path = os.environ.get("SERVER_HTTP")
neural_module_url = os.environ.get("NEURAL_MODULE_URL")
