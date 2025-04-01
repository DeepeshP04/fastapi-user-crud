from fastapi import APIRouter, Depends
from db.database import connect_db
from services.user_service import get_users, get_user_by_id, create_user, update_user, delete_user

router = APIRouter()

@router.get("/users")
async def get_all_users(pool=Depends(connect_db)):
    return await get_users(pool)
