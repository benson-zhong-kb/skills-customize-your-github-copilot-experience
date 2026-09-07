# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with the FastAPI framework. Practice defining HTTP endpoints, validating request data with Pydantic models, and returning appropriate JSON responses for a simple task-tracking service.

## 📝 Tasks

### 🛠️ Create a Health Check Endpoint

#### Description

Use the provided starter code to create a FastAPI application and add an endpoint that confirms the API is running.

#### Requirements

Completed program should:

- Create a `FastAPI` application instance.
- Define a `GET /health` endpoint.
- Return JSON containing the key `status` with the value `ok`.
- Return an HTTP 200 response from the health check.

Example response:

```json
{"status": "ok"}
```

### 🛠️ Add Task Data and Endpoints

#### Description

Create a Pydantic model for a task and use an in-memory list to implement endpoints for viewing and adding tasks.

#### Requirements

Completed program should:

- Define a Pydantic `Task` model with an integer `id`, a string `title`, and a boolean `completed` field.
- Define a separate request model that requires a non-empty `title` and defaults `completed` to `false`.
- Implement `GET /tasks` to return all tasks as a JSON list.
- Implement `POST /tasks` to add a task with a unique ID and return the created task.
- Return an HTTP 201 response when a task is created.
- Reject a request with a missing or empty title using FastAPI validation.

Example request:

```json
{"title": "Practice FastAPI"}
```

Example response:

```json
{"id": 1, "title": "Practice FastAPI", "completed": false}
```

### 🛠️ Complete and Test Task Updates

#### Description

Add an endpoint for updating a task's completion state and verify the API behavior using FastAPI's interactive documentation or a test client.

#### Requirements

Completed program should:

- Implement `PATCH /tasks/{task_id}` to update the selected task's `completed` value.
- Return the updated task when the task exists.
- Return an HTTP 404 response with a useful error message when the task ID does not exist.
- Keep task data in memory while the application is running.
- Verify the health check, task listing, task creation, successful update, validation failure, and missing-task response.

Run the API with:

```bash
uvicorn starter-code:app --reload
```

Then open `http://127.0.0.1:8000/docs` to try the endpoints.
