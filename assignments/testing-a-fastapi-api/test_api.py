import importlib.util
import unittest
from pathlib import Path

from fastapi import HTTPException
from pydantic import ValidationError


API_PATH = Path(__file__).with_name("starter-code.py")
SPEC = importlib.util.spec_from_file_location("starter_code", API_PATH)
starter_code = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(starter_code)


class TaskApiTests(unittest.TestCase):
    def setUp(self):
        starter_code.tasks.clear()

    def test_health_check_returns_ok(self):
        self.assertEqual(starter_code.health_check(), {"status": "ok"})

    def test_create_task_uses_defaults_and_unique_id(self):
        first_task = starter_code.create_task(
            starter_code.TaskCreate(title="First task")
        )
        second_task = starter_code.create_task(
            starter_code.TaskCreate(title="Second task")
        )

        self.assertEqual(first_task.id, 1)
        self.assertFalse(first_task.completed)
        self.assertEqual(second_task.id, 2)

    def test_list_tasks_returns_created_tasks(self):
        starter_code.create_task(starter_code.TaskCreate(title="Study"))

        tasks = starter_code.list_tasks()

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Study")

    def test_empty_title_fails_validation(self):
        with self.assertRaises(ValidationError):
            starter_code.TaskCreate(title="")

    def test_update_task_changes_only_selected_task(self):
        first_task = starter_code.create_task(
            starter_code.TaskCreate(title="First task")
        )
        second_task = starter_code.create_task(
            starter_code.TaskCreate(title="Second task")
        )

        updated_task = starter_code.update_task(first_task.id, True)

        self.assertTrue(updated_task.completed)
        self.assertFalse(second_task.completed)

    def test_update_missing_task_returns_not_found_error(self):
        with self.assertRaises(HTTPException) as context:
            starter_code.update_task(999, True)

        self.assertEqual(context.exception.status_code, 404)
        self.assertEqual(context.exception.detail, "Task not found")


if __name__ == "__main__":
    unittest.main()
