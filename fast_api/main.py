from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional
import httpx # for async call

app = FastAPI()

class AnalyzePRRequest(BaseModel):
    repo_url : str
    pr_number : int
    github_token : Optional[str] = None

@app.post("/start-task")
async def start_task_endpoint(task_request: AnalyzePRRequest):
    data = {
        'repo_url' : task_request.repo_url,
        'pr_number' : task_request.pr_number,
        'github_token' : task_request.github_token
    }

    print(data)
    return {"task_id" : "123", "status" : "Task started"}