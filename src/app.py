from src.usecase.task import TaskUsecases
from src.db.postgres import PostgresDB
from src.web.fastapi import create_app

def task_usecase(
    **dbconfig
) -> TaskUsecases:
    db = PostgresDB(**dbconfig)
    db.open()
    db.create_table()
    u = TaskUsecases(db)
    return u

def assembler(**config):
    dbconfig = {
        "dbname": config.get("dbname", "db"),
        "dbuser": config.get("dbuser", "user"),
        "dbpass": config.get("dbpass", "password"),
        "dbhost": config.get("dbhost", "docker-db-1"),
        "dbport": config.get("dbport", "5432"),
    }
    u = task_usecase(**dbconfig)
    return create_app(u)