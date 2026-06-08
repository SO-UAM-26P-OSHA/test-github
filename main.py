from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "API de ejemplo con FastAPI"}


@app.get("/sumar")
def sumar(a: float, b: float):
    return {
        "operacion": "suma",
        "resultado": a + b
    }


@app.get("/restar")
def restar(a: float, b: float):
    return {
        "operacion": "resta",
        "resultado": a - b
    }
