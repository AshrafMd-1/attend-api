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

def attend(username=None,password=None):
    
    if username is not None and password is not None:
        
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
