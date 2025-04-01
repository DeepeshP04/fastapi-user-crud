from fastapi import APIRouter, Depends
from app.db.database import connect_db
from app.services.user_service import get_users, get_user_by_id, create_user, update_user, delete_user

router = APIRouter()

@router.get("/users")
async def get_all_users(pool=Depends(connect_db)):
    return await get_users(pool)

@router.get("/users/{user_id}")
async def get_user(user_id: int, pool=Depends(connect_db)):
    return await get_user_by_id(pool, user_id)

@router.post("/users")
async def create_new_user(name: str, email: str, password: str, pool=Depends(connect_db)):
    return await create_user(pool, name, email, password)

@router.put("/users/{user_id}")
async def update_existing_user(user_id: int, name: str, email: str, password: str, pool=Depends(connect_db)):
    return await update_user(pool, user_id, name, email, password)

@router.delete("/users/{user_id}")
async def delete_user(user_id: int, pool=Depends(connect_db)):
    return await delete_user(pool, user_id)