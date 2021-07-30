from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder

from database.database import *
from models.post import *
from services.PostService import *
from auth.jwt_bearer import JWTBearer

router = APIRouter()
token_listener = JWTBearer()


@router.post("/", response_description="Post data added into the database")
async def addPost(post: AddPostModel = Body(...)):
    post = jsonable_encoder(post)
    new_post = await add_post(post)
    return ResponseModel(new_post, "Your post is submitted successfully, please wait for approval.")


@router.put("/{id}", response_description="Update the post content.", dependencies=[Depends(token_listener)])
async def updatePost(id: str, post: UpdatePostModel = Body(...)):
    updated_post = await update_post_data(id, post.dict())
    return ResponseModel("Post with ID: {} content update is successful".format(id),
                         "Post content updated successfully") \
        if updated_post \
        else ErrorResponseModel("An error occurred", 404, "Post with id {0} doesn't exist".format(id))


@router.post("/approve/{id}", response_description="Approve the post and post it to social services.", dependencies=[Depends(token_listener)])
async def approvePost(id: str):
    post = await post_collection.find_one({"_id": id})
    if post:
        posted = await publishToSocial(post)
        if posted:
            await post_collection.update_one({"_id": id}, {"approved": True})
        else:
            return ErrorResponseModel("An error occrred", 500,
                               "Post with id {0} unable to publish".format(id))
        return ResponseModel("Post with ID: {} approved".format(id), "Post published successfully")
    return ErrorResponseModel("An error occured", 404, "Post with id {0} doesn't exist".format(id))


@router.delete("/{id}", response_description="Remove the post.", dependencies=[Depends(token_listener)])
async def deletePost(id: str):
    deleted_post = await delete_post(id)
    if deleted_post:
        return ResponseModel("Post with ID: {} removed".format(id), "Post deleted successfully") \
            if deleted_post \
            else ErrorResponseModel("An error occured", 404, "Post with id {0} doesn't exist".format(id))
