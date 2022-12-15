# import uvicorn as uvicorn
from mod.login import login
from mod.scrap import scrap_attend
from auth.secure import decrypt
from fastapi import FastAPI, Body

app = FastAPI()


@app.get("/api/samvidha/attend/dis/v1")
def attend(code=None):
    if code is not None:
        username, password = decrypt(code)

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
