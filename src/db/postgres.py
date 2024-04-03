# connect to postgres db using psycopg2

from functools import wraps
from typing import Callable

import psycopg2

from src.usecase.interfaces import DBInterface


class PostgresDB(DBInterface):
    def __init__(self, dbname: str, user: str, password: str, host: str, port: str):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None

    def open(self):
        self.connection = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )
        self.cursor = self.connection.cursor()

    def close(self) -> None:
        assert self.connection is not None
        if self.cursor is not None:
            self.cursor.close()
        self.connection.close()


    def create_table(self) -> None:
        assert (
            self.cursor is not None and self.connection is not None
        ), "Database not open"
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS tasks ("
            "   id SERIAL PRIMARY KEY,"
            "   name TEXT NOT NULL,"
            "   nextup TIMESTAMP NOT NULL,"
            "   frequency INTERVAL NOT NULL,"
            "   assigned TEXT NOT NULL"
            ");"
        )
        self.connection.commit()

    def add_task(self, task: dict) -> int:
        assert (
            self.cursor is not None and self.connection is not None
        ), "Database not open"
        self.cursor.execute(
            "INSERT INTO tasks (name, nextup, frequency, assigned) VALUES (%s, %s, %s, %s) RETURNING id;",
            (task["name"], task["nextup"], task["frequency"], task["assigned"]),
        )
        self.connection.commit()
        result = self.cursor.fetchone()
        if result is not None:
            return result[0]
        else:
            raise Exception("Task not added")

    def get_task(self, task_id: int) -> dict:
        assert (
            self.cursor is not None and self.connection is not None
        ), "Database not open"
        self.cursor.execute("SELECT * FROM tasks WHERE id = %s;", (task_id,))
        result = self.cursor.fetchone()
        if result is not None:
            return {
                "id": result[0],
                "name": result[1],
                "nextup": result[2],
                "frequency": result[3],
                "assigned": result[4],
            }
        else:
            raise Exception("Task not found")

    def update_task(self, task_id: int, data: dict) -> None:
        assert (
            self.cursor is not None and self.connection is not None
        ), "Database not open"
        self.cursor.execute(
            "UPDATE tasks SET name = %s, nextup = %s, frequency = %s, assigned = %s WHERE id = %s;",
            (
                data["name"],
                data["nextup"],
                data["frequency"],
                data["assigned"],
                task_id,
            ),
        )
        self.connection.commit()

    def delete_task(self, task_id: int) -> None:
        assert (
            self.cursor is not None and self.connection is not None
        ), "Database not open"
        self.cursor.execute("DELETE FROM tasks WHERE id = %s;", (task_id,))
        self.connection.commit()

    def list_tasks(self) -> list[dict]:
        assert (
            self.cursor is not None and self.connection is not None
        ), "Database not open"
        self.cursor.execute("SELECT * FROM tasks;")
        result = self.cursor.fetchall()
        return [
            {
                "id": task[0],
                "name": task[1],
                "nextup": task[2],
                "frequency": task[3],
                "assigned": task[4],
            } for task in result
        ]

