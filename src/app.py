from src.usecase.task import TaskUsecases
from src.db.postgres import PostgresTaskDB, PostgresUserDB
from src.usecase.user import UserUsecases
from src.web.fastapi import core_api, create_app
from src.web.task import task_api
from src.web.user import user_api

def task_usecase(
    **dbconfig
) -> TaskUsecases:
    db = PostgresTaskDB(**dbconfig)
    db.open()
    db.create_table()
    u = TaskUsecases(db)
    return u

def user_usecase(
    **dbconfig
) -> UserUsecases:
    db = PostgresUserDB(**dbconfig)
    db.open()
    db.create_table()
    u = UserUsecases(db)
    return u

def assembler(**config):
    dbconfig = {
        "dbname": config.get("dbname", "db"),
        "dbuser": config.get("dbuser", "user"),
        "dbpass": config.get("dbpass", "password"),
        "dbhost": config.get("dbhost", "docker-db-1"),
        "dbport": config.get("dbport", "5432"),
    }
    return create_app([
        core_api(),
        task_api(task_usecase(**dbconfig)),
        user_api(user_usecase(**dbconfig))
    ])