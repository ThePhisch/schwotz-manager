import pytest
from unittest.mock import Mock

from datetime import datetime, timedelta

from src.entity.task import Task


class TestTask:
    def setup_method(self):
        self.task = Task("Test Task", datetime.now(), timedelta(days=1), "Test User")
        self.db = Mock()

    def test_add(self): ...

    def test_change(self): ...

    def test_complete(self): ...

    def test_delete(self): ...

    def test_list(self): ...
