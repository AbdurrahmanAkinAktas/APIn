import logging

from fastapi import APIRouter
from starlette.requests import Request

router = APIRouter(
    prefix="/log",
    tags=["log", "dummy"],
)

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


@router.get("/{param}",
            description="Simply writes the given parameter value to the log. Always return true.")
async def log_this(param: str):
    logging.info("This just came in: {}".format(param))
    return True


@router.post("/",
             description="Simply writes the request body to the log. Always return true.")
async def log_this(request: Request):
    body = await request.body()
    body = body.decode("utf-8")
    logging.info("This just came in:"
                 "\n___Start Log___\n"
                 "{}"
                 "\n___End Log___\n".format(body))
    return True
