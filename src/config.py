import os

user = "test" # os.environ['POSTGRE_USER']
password = "password" # os.environ['POSTGRES_PASSWORD']
host = "localhost" # os.environ['POSTGRES_HOST']
database = "example" # os.environ['POSTGRES_DB']
port = "5432" # os.environ['POSTGRES_PORT']

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'