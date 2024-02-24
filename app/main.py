from fastapi import FastAPI

from app.controller import primitive_controller, echo_controller, log_controller
from app.controller import http_code_controller

app = FastAPI()

app.include_router(primitive_controller.router)
app.include_router(echo_controller.router)
app.include_router(http_code_controller.router)
app.include_router(log_controller.router)

@app.get("/")
def root():
    return {"message": "Welcome to APIn"}
