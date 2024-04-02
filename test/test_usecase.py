import pytest

from datetime import datetime, timedelta

from src.entity.task import Task


@pytest.fixture
def sample_task():
    task = Task("Test Task", datetime.now(), timedelta(days=17), "Test User")
    task.assign_id(6000)
    return task


def test_new(): ...


def test_change(): ...


def test_complete(): ...


def test_delete(): ...


def test_list(): ...