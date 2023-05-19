from fastapi import FastAPI, Request, Response
import uvicorn
import nest_asyncio
from pyngrok import ngrok
api= FastAPI()
@api .get('/')
def index(request : Request):
    return "Hinga weze Greenhouse"
@api.get('/bmi')
def bmi_calculator(request: Request, height: int, weight: int):
    bmi = float(weight)/float(height)**2
    return f"Your BMI is {bmi}"

api =FastAPI()
#Run the API
if __name__== "__main__":
    ngrok_tunnel=ngrok.connect(5050)
    print(f"Your Domain Name is {ngrok_tunnel.public_url}")
    nest_asyncio.apply()
    uvicorn.run(api,host="localhost", port=5050)