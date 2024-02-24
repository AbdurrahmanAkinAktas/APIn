from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import PlainTextResponse

router = APIRouter(
    prefix="/echo",
    tags=["echo", "dummy"],
)


# GET versions

@router.get("/string/{var}", description="Echoes back the path variable as string.")
async def get_echo(var: str):
    return str(var)


@router.get("/int/{var}", description="Echoes back the path variable as integer.")
async def get_echo(var: int):
    return int(var)


@router.get("/float/{var}", description="Echoes back the path variable as float.")
async def get_echo(var: float):
    return float(var)


# POST versions

@router.post("/body/plain", response_class=PlainTextResponse,
             description="Echoes back the request body as utf-8 plain text.")
async def get_echo(request: Request):
    body = await request.body()
    body = body.decode(encoding="utf-8")
    return body
