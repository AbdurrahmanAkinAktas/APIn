from fastapi import APIRouter
from starlette.responses import Response

router = APIRouter(
    prefix="/http",
    tags=["http", "status", "dummy"],
)


@router.get("/{code}",
            description="Returns an empty response with the specified HTTP status code. Returns 404 in case no corresponding status can be found.")
async def get_http_code(code: int, response: Response):
    response.status_code = code
    return response
