# import uvicorn as uvicorn
from mod.login import login
from mod.scrap import scrap_attend
from fastapi import FastAPI, Body

app = FastAPI()


@app.get("/api/samvidha/attend/dis/v1")
# async def attend(
#         payload: dict = Body(
#             {
#                 "username": "username",
#                 "password": "password"
#             }
#         )):
#     username = payload['username']
#     password = payload['password']
def attend():

    session, check = login('21951A6612', 'Ashraf0506$$$$4')

    if check['status'] == '1':
        df = scrap_attend(session)
        return {
            "data": df.to_dict(orient='records'),
            "message": "The Attendance"
        }
    else:
        return {
            "data": [],
            "message": "Invalid Credentials"
        }


#
# if __name__ == "__main__":
#     uvicorn.run("main:app", port=8080)
