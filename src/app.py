from src.usecase.task import TaskUsecases
from src.db.postgres import PostgresDB
from src.web.fastapi import create_app

def task_usecase() -> TaskUsecases:
    db = PostgresDB("db", "user", "password", "docker-db-1", "5432")
    db.open()
    db.create_table()
    u = TaskUsecases(db)
    return u

def assembler():
    u = task_usecase()
    return create_app(u)