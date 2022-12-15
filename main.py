# import uvicorn as uvicorn
from mod.login import login
from mod.scrap import scrap_attend
from mod.dummy.val import dum
from fastapi import FastAPI, Body

app = FastAPI()


@app.get("/api/samvidha/attend/dis/v1")
def attend(username=None, password=None):
    if username is not None and password is not None:
        if username == "dummy" and password == "dummy":
            return {
                "message": "The DUMMY data is fetched successfully",
                "data": dum()

            }
        session, check = login(username, password)

        if check['status'] == '1':
            df = scrap_attend(session)
            return {
                "message": "The attendance data is fetched successfully",
                "data": df.to_dict(orient='records')

            }
        else:
            return {
                "message": "Invalid Credentials",
                "data": []

            }
    else:
        return {
            "message": "Please provide username and password",
            "data": []

        }

#
# if __name__ == "__main__":
#     uvicorn.run("main:app", port=8080)
