from os import access
import facebook
from decouple import config
from database.database import retrieve_config


async def getCurrentUserEmail(token: str) -> str:
    appSecret = await retrieve_config('facebook_appSecret')
    FB = facebook.GraphAPI(
        access_token=token, app_secret=appSecret, version="11.0")
    user = FB.get_object("me", fields='email')
    return user['email'] if user else False


async def fbPublish(msg: str, link: str) -> dict:
    appSecret = await retrieve_config('facebook_appSecret')
    pageUsername = await retrieve_config('facebook_pageUsername')
    accessToken = await retrieve_config('facebook_accessToken')
    FB = facebook.GraphAPI(access_token=accessToken,
                           app_secret=appSecret, version="11.0")
    post = FB.put_object(pageUsername, "feed", message=msg, link=link)
    return post


async def fbPublishImg(msg: str, imgLink: str) -> dict:
    appSecret = await retrieve_config('facebook_appSecret')
    pageUsername = await retrieve_config('facebook_pageUsername')
    accessToken = await retrieve_config('facebook_accessToken')
    FB = facebook.GraphAPI(access_token=accessToken,
                           app_secret=appSecret, version="11.0")
    post = FB.put_object(pageUsername, "photos", message=msg, url=imgLink)
    return post
