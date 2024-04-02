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


def test_to_dict():
    # assert that the to_dict method will work
    task = Task("Test Task", datetime.now(), timedelta(days=1), "Test User")
    task.assign_id(1)
    dict_format = task.to_dict()
    assert dict_format == {
        "id": 1,
        "name": "Test Task",
        "nextup": task.nextup.strftime(Task.timeformat),
        "frequency": task.frequency.total_seconds(),
        "assigned": "Test User",
    }

    # manually reconstruct the task
    task_reconstructed = Task(
        dict_format["name"],
        datetime.strptime(dict_format["nextup"], Task.timeformat),
        timedelta(seconds=dict_format["frequency"]),
        dict_format["assigned"],
    )

    assert task_reconstructed.id == None
    assert task_reconstructed.name == "Test Task"
    assert task_reconstructed.frequency == timedelta(days=1)
    assert task_reconstructed.nextup.date() == datetime.now().date()