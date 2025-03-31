# Import required libraries
import os
import asyncio
import asyncpg
from dotenv import load_dotenv

async def main():
    # Load .env file
    load_dotenv()
    
    # Get the connection string from the environment variable
    connection_string = os.getenv('DATABASE_URL')
    
    # Create a connection pool
    pool = await asyncpg.create_pool(connection_string)
    
    # Acquire a connection from the pool
    async with pool.acquire() as conn:
        pass
        
    # Close the pool
    await pool.close()
    
# Run the asynchronous main function
asyncio.run(main())