import re
from database.database import *
from services.SocialConnection.FacebookService import fbPublish, fbPublishImg


async def publishToSocial(postData: dict):
    enabledSocialServices = []
    configs = retrieve_configs()
    for config in configs:
        if '_socialEnabled' in config['field_name'] and config['field_value'] == 'True':
            socialService = config['field_name'].split('_socialEnabled')[0]
            enabledSocialServices.append(socialService)

    urlRegex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(urlRegex, postData['content'])
    postData['content'] = "{}{}\n{}".format(
        configs['postPrefix'], configs['postCounter'], postData['content'])

    for socialService in enabledSocialServices:
        if socialService == 'facebook':
            if postData['imageLink'] == '':
                fbPost = await fbPublish(postData['content'], url[0][0] if len(url) == 1 else '')
            else:
                fbPost = await fbPublishImg(postData['content'], postData['imageLink'])
            if 'error' in fbPost:
                return False
        elif socialService == 'discord':
            return
