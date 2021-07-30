import motor.motor_asyncio
from bson import ObjectId
from decouple import config

from .database_helper import student_helper, admin_helper, config_helper, post_helper

MONGO_DETAILS = config('MONGO_DETAILS')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students

student_collection = database.get_collection('students_collection')
admin_collection = database.get_collection('admins')
config_collection = database.get_collection('configs')
post_collection = database.get_collection('posts')

# Post start


async def add_post(post_data: dict) -> dict:
    post_data['approved'] = False
    post = await post_collection.insert_one(post_data)
    new_post = await post_collection.findOne({"_id": post.inserted_id})
    return post_helper(new_post)


async def update_post_data(id: str, data: dict):
    post = await post_collection.find_one({"_id": ObjectId(id)})
    if post:
        post_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True


async def delete_post(id: str):
    post = await post_collection.find_one({"_id": ObjectId(id)})
    if post:
        await post_collection.delete_one({"_id": ObjectId(id)})
        return
# Post end


async def add_config(config_data: dict) -> dict:
    config = await config_collection.find_one({"field_name": config_data['field_name']})
    if not config:
        new_config = await config_collection.insert_one(config_data)
        return config_helper(new_config)
    return False


async def retrieve_config(field_name: str) -> str:
    config = await config_collection.find_one({"field_name": field_name})
    if config:
        return config['field_value']
    return False


async def retrieve_configs():
    configs = []
    async for config in config_collection.find():
        configs.append(student_helper(config))
    return configs


async def update_config(field_name: str, field_value: str):
    config = await config_collection.find_one({"field_name": field_name})
    if config:
        config_collection.update_one({"_id": config['_id']}, {
                                     "field_value": field_value})
        return True


async def add_admin(admin_data: dict) -> dict:
    admin = await admin_collection.insert_one(admin_data)
    new_admin = await admin_collection.find_one({"_id": admin.inserted_id})
    return admin_helper(new_admin)
