from fastapi import FastAPI
from app.db.database import connect_db, close_db
from app.db.database import create_table
from app.apis.users import router

app = FastAPI()

@app.on_event("startup")
async def startup():
    app.state.pool = await connect_db()
    await create_table(app.state.pool)
    
@app.on_event("shutdown")
async def shutdown():
    await close_db(app.state.pool)
    
app.include_router(router)
    