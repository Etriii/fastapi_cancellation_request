from fastapi import APIRouter, Depends
from ..dependencies import cancellation_request

import asyncio

router = APIRouter(tags=["LongTask"])

@router.get("/long-task/")
async def long_task(
    check_cancel=Depends(cancellation_request.get_disconnection_checker),
):
    for i in range(10):#10 seconds
        await check_cancel()
        await asyncio.sleep(1)
        print(f"Task {i+1}")
    return {"message": "Completed"}


# @router.get("/long-task/")
# async def long_task(check_cancel=Depends(cancellation_request.get_disconnection_checker)):
#     await check_cancel()  # right at the start
#     await loop(4)
#     await check_cancel()  # maybe after heavy step
#     await loop(4)
#     await check_cancel()  # maybe next time
#     await loop(4)
#     await check_cancel()  # before returning
#     return {"message": "done"}


async def loop(n, message):
    for i in range(n):
        print(f"{message} {i}")
        await asyncio.sleep(1)
        print(f"Task {i+1}")  # e commment if sa 3rd suggestion na


# @router.get("/long-task/")
# async def task(check_cancel=Depends(request_cancellation.get_disconnection_checker)):
#     async def load_data():
#         await loop(3, "loading date: ")
#         print("✅ Data loaded")

#     async def process_data():
#         await loop(3, "processing data...: ")
#         print("✅ Data processed")

#     async def save_results():
#         await asyncio.sleep(1)
#         print("✅ Results saved")

#     async def work():
#         await load_data()
#         await process_data()
#         await save_results()

#     return await request_cancellation.run_with_cancellation_check(work, check_cancel)
