from fastapi import FastAPI

from traductor import traducirEsp, traducirQch

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/es-qu")
async def spanishQuechua(txt):
    txt_traducido = traducirEsp(txt)
    return txt

@app.post("/qu-es")
async def quechuaSpanish(txt):
    txt_traducido = traducirQch(txt)
    return txt


