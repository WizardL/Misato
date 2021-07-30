from fastapi import Body, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBasicCredentials
from fastapi.responses import RedirectResponse
from passlib.context import CryptContext

from database.database import admin_collection, post_collection
from auth.jwt_handler import signJWT
from database.database import add_admin, retrieve_config
from models.admin import *
from services.SocialConnection.FacebookService import getCurrentUserEmail

router = APIRouter()

hash_helper = CryptContext(schemes=["bcrypt"])


@router.get("/login/fb/")
async def admin_loginFB(code: str = '', state: str = ''):
    redirectUrl = await retrieve_config('siteUrl') + '/login/fb'
    fbAppId = await retrieve_config('facebook_appId')

    if not fbAppId:
        return ErrorResponseModel("An error occrred", 500, "Login with Facebook is not enabled.")

    oAuthLink = "https://www.facebook.com/v11.0/dialog/oauth?client_id={}&redirect_uri={}&state={}" \
        .format(fbAppId, redirectUrl, '') \
        + '&scope=email,pages_manage_posts,pages_read_user_content,pages_show_list'

    if code == '':
        return RedirectResponse(oAuthLink)
    else:
        userEmail = await getCurrentUserEmail(code)
        admin_user = await admin_collection.find_one({"email": userEmail}, {"_id": 0})
        if admin_user:
            return signJWT(userEmail)
        else:
            return ErrorResponseModel("An error occrred", 403, "Incorrect email or password")



@router.post("/login")
async def admin_login(admin_credentials: HTTPBasicCredentials = Body(...)):
    # NEW CODE
    admin_user = await admin_collection.find_one({"email": admin_credentials.username}, {"_id": 0})
    if (admin_user):
        password = hash_helper.verify(
            admin_credentials.password, admin_user["password"])
        if (password):
            return signJWT(admin_credentials.username)

        return ErrorResponseModel("An error occrred", 403, "Incorrect email or password")

    return ErrorResponseModel("An error occrred", 403, "Incorrect email or password")


@router.post("/")
async def admin_signup(admin: AdminModel = Body(...)):
    admin_exists = await admin_collection.find_one({"email":  admin.email}, {"_id": 0})
    if(admin_exists):
        return ErrorResponseModel("An error occrred", 500, "Email already exists")

    admin.password = hash_helper.encrypt(admin.password)
    new_admin = await add_admin(jsonable_encoder(admin))
    return new_admin
