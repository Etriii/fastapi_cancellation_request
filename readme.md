# fastapi-cancellation-task

This repository demonstrates how to implement cancellation checks in a long-running task with FastAPI. The task simulates a time-consuming process and checks whether the client has disconnected during the execution.

### Features:
- Long-running task simulation (prints progress every second).
- Checks for client disconnection to gracefully cancel the task.
- FastAPI-powered backend.
- Simple async cancellation logic.

## Requirements

To run the project, you'll need the following Python packages:

- **fastapi**: For creating the API.
- **uvicorn**: For running the app locally.

```bash
pip install fastapi uvicorn

or 

pip install -r requirements.txt
```

## How to Run the Application

1. Run the app

```bash
python -m uvicorn app.main:app --reload
```

2. Visit http://127.0.0.1:8000/api/v1/long-task/ to test the long-running task. or go to documentation:
```bash
http://127.0.0.1:8000/docs
```

