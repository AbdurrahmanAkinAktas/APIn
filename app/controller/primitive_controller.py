import random

from fastapi import APIRouter

router = APIRouter(
    prefix="/primitive",
    tags=["primitive", "dummy"],
)


# Booleans

@router.get("/bool/random", description="Returns a random boolean.")
async def get_primitive():
    return bool(random.getrandbits(1))


@router.get("/bool/true", description="Always returns true.")
async def get_primitive():
    return True


@router.get("/bool/false", description="Always returns false.")
async def get_primitive():
    return False


# Integers

@router.get("/int/random", description="Returns a random integer between 0 and 100.")
async def get_primitive():
    return random.randint(0, 100)


@router.get("/int/random/{start}/{end}", description="Returns a random integer between the first and second parameter.")
async def get_primitive(start: int, end: int):
    return random.randint(start, end)
