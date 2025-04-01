# Import required libraries
import os
import asyncpg
from dotenv import load_dotenv
from .models import CREATE_USERS_TABLE

async def connect_db():
    # Load .env file
    load_dotenv()
    
    # Get the connection string from the environment variable
    connection_string = os.getenv('DATABASE_URL')
    
    # Create a connection pool
    pool = await asyncpg.create_pool(connection_string)
    
    return pool
    
async def create_table(pool):
    # Create the table if it doesn't exist
    async with pool.acquire() as connection:
        await connection.execute(CREATE_USERS_TABLE)
    
async def close_db(pool):
    # Close the database connection pool
    await pool.close()
    
# # Run the asynchronous main function
# asyncio.run(main())