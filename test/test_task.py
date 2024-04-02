from datetime import datetime, timedelta

from src.entity.task import Task


def test_creation():
    # assert that regular creation will work
    task = Task("Test Task", datetime.now(), timedelta(days=1), "Test User")
    assert task.id == None
    assert task.name == "Test Task"
    assert task.frequency == timedelta(days=1)
    assert task.nextup.date() == datetime.now().date()


def test_register():
    # assert that the register method will work
    task = Task("Test Task", datetime.now(), timedelta(days=1), "Test User")
    task.assign_id(1)
    assert task.id == 1
    # str and repr
    assert (
        str(task)
        == f"Task: {task.name} - Next up: {task.nextup} - Frequency: {task.frequency} - Assigned: {task.assigned}"
    )
    assert repr(task) == f"<Task {task.id:>5} name {task.name[:8]}>"


def test_complete():
    # assert that the complete method will work
    task = Task("Test Task", datetime.now(), timedelta(days=1), "Test User")
    task.complete()
    assert task.nextup.date() == (datetime.now() + timedelta(days=1)).date()