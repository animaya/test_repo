import psycopg2
from config import config

def conn():
    params = config()
    return psycopg2.connect(**params)


if __name__ == '__main__':
    conn()

#changes