# get all users
async def get_users(pool):
    async with pool.acquire() as conn:
        return await conn.fetch("SELECT * FROM users")
    
# get user by id
async def get_user_by_id(pool, user_id):
    async with pool.acquire() as conn:
        return await conn.fetchrow("SELECT * FROM users WHERE id = $1", user_id)

# create user
async def create_user(pool, name, email, password):
    async with pool.acquire() as conn:
        return await conn.fetchrow(
            "INSERT INTO users (name, email, password) VALUES ($1, $2, $3) RETURNING *",
            name, email, password
        )
     
# update user   
async def update_user(pool, user_id, name, email, password):
    async with pool.acquires() as conn:
        return await conn.fetchrow(
            "UPDATE users SET name = $1, email = $2, password = $3 WHERE id = $4 RETURNING *",
            name, email, password, user_id
        )
      
# delete user  
async def delete_user(pool, user_id):
    async with pool.acquire() as conn:
        return await conn.execute("DELETE FROM users WHERE id = $1", user_id)        