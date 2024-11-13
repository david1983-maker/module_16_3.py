from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = {'1': "Имя:Example,возраст:18"}


@app.get('/users')
async def get_user() -> dict:
    return users


@app.post('/user/{user_id}/{username}/{age}')
async def post_user(user_id: str, username: str, age: int) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя:{username}, возраст:{age}'
    return f"User {user_id} is registred "


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str, age: int) -> str:
    users[user_id] = f'Имя:{username}, возраст:{age}'
    return f'The user {user_id} is update'


@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f'User {user_id} has been deleted'
