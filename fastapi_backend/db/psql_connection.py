import os
from dotenv import load_dotenv
from psycopg_pool import ConnectionPool

env_mode = os.getenv("ENV", "dev")
env_file= f".env.{env_mode}"

load_dotenv(env_file)

pool = ConnectionPool()