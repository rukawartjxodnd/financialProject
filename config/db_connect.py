import config.dbConfig as dbConfig
import psycopg2 as pg2

def dataBaseConnect(area = "test"):
    # DB Connect

    # 테스트 DB
    if area == "test":
        config = dbConfig.TestingDbConfig
        connection = pg2.connect(host=config.HOST, dbname=config.DB_NAME, user=config.USER, password=config.PASSWORD)

    return connection