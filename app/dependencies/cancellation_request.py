from fastapi import Request, HTTPException
from typing import Callable, Awaitable
import asyncio

async def get_disconnection_checker(request: Request):
    async def check():
        if await request.is_disconnected():
            print("Request Cancelled")
            raise HTTPException(status_code=499, detail="Request Cancelled")
    return check


async def run_with_cancellation_check(
    task_fn: Callable[[], Awaitable],
    check_cancel: Callable[[], Awaitable[None]],
    interval: float = 1.0,
):
    """
    Runs an async task while periodically checking for client disconnection.
    
    Parameters:
    - task_fn: your async function to run (no args)
    - check_cancel: a function that checks for client disconnect and raises 499
    - interval: how often to check (seconds)
    """
    
    task = asyncio.create_task(task_fn())

    try:
        while not task.done():
            await asyncio.sleep(interval)
            await check_cancel()  # may raise 499

        return await task
    except HTTPException as e:
        if not task.done():
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                print("✅ Background task was cancelled.")
        raise e  # re-raise 499