from src.entity.user import User
from src.usecase.session import SessionUsecases
from src.usecase.task import TaskUsecases
from src.db.postgres import PostgresSessionDB, PostgresTaskDB, PostgresUserDB
from src.usecase.user import UserUsecases
from src.web.fastapi import core_api, create_app
from src.web.session import session_api
from src.web.task import task_api
from src.web.user import user_api

def task_usecase(
    config,
    dbconfig
) -> TaskUsecases:
    db = PostgresTaskDB(**dbconfig)
    db.open()
    db.create_table()
    u = TaskUsecases(db)
    return u

def user_usecase(
    config,
    dbconfig
) -> UserUsecases:
    db = PostgresUserDB(**dbconfig)
    db.open()
    db.create_table()

    # add default users
    for k, v in config.get("users", {}).items():
        u = User(id=None, username=k, password=v)
        db.add_user(u.model_dump())

    u = UserUsecases(db)
    return u

def session_usecase(
    config,
    dbconfig
) -> SessionUsecases:
    sessiondb = PostgresSessionDB(**dbconfig)
    userdb = PostgresUserDB(**dbconfig)
    for db in [sessiondb, userdb]:
        db.open()
        db.create_table()
    u = SessionUsecases(sessiondb=sessiondb, userdb=userdb)
    return u

def assembler(config: dict):
    dbconfig = {
        "dbname": config.get("dbname", "db"),
        "dbuser": config.get("dbuser", "user"),
        "dbpass": config.get("dbpass", "password"),
        "dbhost": config.get("dbhost", "docker-db-1"),
        "dbport": config.get("dbport", "5432"),
    }
    print(config)
    return create_app([
        core_api(),
        task_api(task_usecase(config, dbconfig)),
        user_api(user_usecase(config, dbconfig), config),
        session_api(session_usecase(config, dbconfig)),  # safe to run because new table is only created if it doesn't exist
    ])