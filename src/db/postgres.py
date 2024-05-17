# connect to postgres db using psycopg2

from functools import wraps
from typing import Generator, Any

import psycopg2

from src.typing import StrDict
from src.usecase.interfaces import DBInterface
from src.usecase.session import SessionDBInterface
from src.usecase.task import TaskDBInterface
from src.usecase.user import UserDBInterface

class PostgresDB():
    def __init__(self, dbname: str, dbuser: str, dbpass: str, dbhost: str, dbport: str):
        self.dbname = dbname
        self.user = dbuser
        self.password = dbpass
        self.host = dbhost
        self.port = dbport
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

class PostgresSessionDB(PostgresDB, SessionDBInterface):

    def create_table(self) -> None:
        assert (
            self.cursor is not None and self.connection is not None
        ), "Database not open"
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS sessions ("
            "   id SERIAL PRIMARY KEY,"
            "   user_id INT NOT NULL,"
            "   token TEXT NOT NULL,"
            "   expires_at TIMESTAMP NOT NULL,"
            "   created_at TIMESTAMP NOT NULL,"
            "   updated_at TIMESTAMP NOT NULL,"
            "   FOREIGN KEY (user_id) REFERENCES users(id)"
            ");"
        )
        self.connection.commit()

    def new_session(self, session: StrDict) -> None:
        assert (
            self.cursor is not None and self.connection is not None
        ), "Database not open"
        self.cursor.execute(
            "INSERT INTO sessions (user_id, token, expires_at, created_at, updated_at) VALUES (%s, %s, %s, %s, %s);",
            (
                session["user_id"],
                session["token"],
                session["expires_at"],
                session["created_at"],
                session["updated_at"],
            ),
        )
        self.connection.commit()
    
    def close_session(self, token: str) -> None:
        assert (
            self.cursor is not None and self.connection is not None
        ), "Database not open"
        self.cursor.execute("DELETE FROM sessions WHERE token = %s;", (token,))
        self.connection.commit()

    def get_session(self, token: str) -> dict:
        assert (
            self.cursor is not None and self.connection is not None
        ), "Database not open"
        self.cursor.execute("SELECT * FROM sessions WHERE token = %s;", (token,))
        result = self.cursor.fetchone()
        if result is not None:
            return {
                "id": result[0],
                "user_id": result[1],
                "token": result[2],
                "expires_at": result[3],
                "created_at": result[4],
                "updated_at": result[5],
            }
        else:
            raise ValueError("Session not found")


class PostgresUserDB(PostgresDB, UserDBInterface):

    def create_table(self) -> None:
        assert (
            self.cursor is not None and self.connection is not None
        ), "Database not open"
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS users ("
            "   id SERIAL PRIMARY KEY,"
            "   username TEXT NOT NULL,"
            "   password TEXT NOT NULL"
            ");"
        )
        self.connection.commit()

    def add_user(self, user: StrDict) -> int:
        assert (
            self.cursor is not None and self.connection is not None
        ), "Database not open"
        self.cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s) RETURNING id;",
            (user["username"], user["password"]),
        )
        self.connection.commit()
        result = self.cursor.fetchone()
        if result is not None:
            return result[0]
        else:
            raise Exception("User not added")

    def get_user(self, user_id: int) -> StrDict:
        assert (
            self.cursor is not None and self.connection is not None
        ), "Database not open"
        self.cursor.execute("SELECT * FROM users WHERE id = %s;", (user_id,))
        result = self.cursor.fetchone()
        if result is not None:
            return {
                "id": result[0],
                "username": result[1],
                "password": result[2],
            }
        else:
            raise Exception("User not found")

    def update_user(self, user_id: int, data: StrDict) -> None:
        assert (
            self.cursor is not None and self.connection is not None
        ), "Database not open"
        self.cursor.execute(
            "UPDATE users SET username = %s, password = %s WHERE id = %s;",
            (data["username"], data["password"], user_id),
        )
        self.connection.commit()

    def delete_user(self, user_id: int) -> None:
        assert (
            self.cursor is not None and self.connection is not None
        ), "Database not open"
        self.cursor.execute("DELETE FROM users WHERE id = %s;", (user_id,))
        self.connection.commit()

    def list_users(self) -> Generator[StrDict, None, None]:
        assert (
            self.cursor is not None and self.connection is not None
        ), "Database not open"
        self.cursor.execute("SELECT * FROM users;")
        result = self.cursor.fetchall()
        for user in result:
            yield {
                "id": user[0],
                "username": user[1],
                "password": user[2],
            }

    def get_id_from_username(self, username: str) -> int:
        assert (
            self.cursor is not None and self.connection is not None
        ), "Database not open"
        self.cursor.execute("SELECT id FROM users WHERE username = %s;", (username,))
        result = self.cursor.fetchone()
        if result is not None:
            return result[0]
        else:
            raise Exception("User not found")

class PostgresTaskDB(PostgresDB, TaskDBInterface):
    def create_table(self) -> None:
        assert (
            self.cursor is not None and self.connection is not None
        ), "Database not open"
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS tasks ("
            "   id SERIAL PRIMARY KEY,"
            "   name TEXT NOT NULL,"
            "   nextup TIMESTAMP NOT NULL,"
            "   timedelta INTERVAL NOT NULL,"
            "   assigned TEXT NOT NULL"
            ");"
        )
        self.connection.commit()

    def add_task(self, task: dict) -> int:
        assert (
            self.cursor is not None and self.connection is not None
        ), "Database not open"
        self.cursor.execute(
            "INSERT INTO tasks (name, nextup, timedelta, assigned) VALUES (%s, %s, %s, %s) RETURNING id;",
            (task["name"], task["nextup"], task["timedelta"], task["assigned"]),
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
                "timedelta": result[3],
                "assigned": result[4],
            }
        else:
            raise Exception("Task not found")

    def update_task(self, task_id: int, data: dict) -> None:
        assert (
            self.cursor is not None and self.connection is not None
        ), "Database not open"
        self.cursor.execute(
            "UPDATE tasks SET name = %s, nextup = %s, timedelta = %s, assigned = %s WHERE id = %s;",
            (
                data["name"],
                data["nextup"],
                data["timedelta"],
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

    def list_tasks(self) -> Generator[StrDict, None, None]:
        assert (
            self.cursor is not None and self.connection is not None
        ), "Database not open"
        self.cursor.execute("SELECT * FROM tasks;")
        result = self.cursor.fetchall()
        for task in result:
            yield {
                "id": task[0],
                "name": task[1],
                "nextup": task[2],
                "timedelta": task[3],
                "assigned": task[4],
            }
