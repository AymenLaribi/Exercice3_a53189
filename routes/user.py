from fastapi import APIRouter
from models.user import User
from config.db import conn 
from schemas.user import userEntity, usersEntity
from bson import ObjectId

user = APIRouter()

@user.get('/')
async def find_user():
    return usersEntity(conn.local.user.find())
    
@user.post('/')
async def create_user(user : User):
    conn.local.user.insert_one(dict(user))
    return userEntity(conn.local.user.find())

@user.put('/')
async def update_user(id,user : User):
    conn.local.user.find_one_and_update({"_id" : ObjectId(id)},{"set": dict(user)})
    return userEntity(conn.local.user.find({"_id" : ObjectId(id)}))

@user.delete('/')
async def delete_user(id,user : User):
    return userEntity(conn.local.user.find_one_and_delete({"_id" : ObjectId(id)}))