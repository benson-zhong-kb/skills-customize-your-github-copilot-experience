# 📘 Assignment: Testing a FastAPI REST API

## 🎯 Objective

Write automated tests for the task-tracking REST API from the FastAPI assignment. Practice organizing tests with Python's standard-library `unittest` module, checking successful behavior, validating bad input, and confirming that errors return the correct result.

## 📝 Tasks

### 🛠️ Test the API's Successful Responses

#### Description

Use the provided test starter code to load the task API and write unit tests for its healthy and successful request paths. Reset the in-memory task list before each test so that tests do not depend on their execution order.

#### Requirements

Completed program should:

- Use `unittest.TestCase` and give each test a descriptive name.
- Test that `health_check()` returns `{"status": "ok"}`.
- Test that creating a task returns the expected title, default completion state, and a unique integer ID.
- Test that `list_tasks()` returns tasks that were created.
- Clear the shared in-memory task list before each test.

Run the tests with:

```bash
python -m unittest test_api.py -v
```

### 🛠️ Test Validation and Task Updates

#### Description

Add tests for invalid task data and for changing a task's completion state. Use assertions that check both the result and the important values in it.

#### Requirements

Completed program should:

- Verify that an empty task title raises Pydantic validation for `TaskCreate`.
- Verify that a task can be marked completed with `update_task()`.
- Verify that updating one task does not change a different task.
- Include at least one test for a task ID that does not exist.
- Use specific assertions such as `assertEqual`, `assertIsInstance`, `assertFalse`, or `assertTrue` instead of only checking that code runs.

### 🛠️ Return and Test the Correct Error

#### Description

Update the API's missing-task behavior so that an unknown task ID produces an HTTP 404 error, then complete the test for that behavior. This makes the API contract explicit and prevents a missing task from being treated as a successful response.

#### Requirements

Completed program should:

- Raise FastAPI's `HTTPException` with status code `404` when `update_task()` cannot find the requested ID.
- Include a useful detail message such as `Task not found` in the exception.
- Assert both the exception type and status code in the missing-task test.
- Keep all tests independent so they pass when run individually or as a complete suite.
- Run the full test file successfully with Python's built-in `unittest` runner.

Example test pattern:

```python
with self.assertRaises(HTTPException) as context:
    starter_code.update_task(999, True)

self.assertEqual(context.exception.status_code, 404)
```
