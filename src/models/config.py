from pydantic import BaseModel, Field

'''
List of field_name:
    - siteUrl: Url of site without '/' at the end (str)
    - postPrefix: Post prefix, e.g.: #靠北工程師
    - postCounter: Post counter.
    - facebook_appId: Id of your facebook app (str)
    - facebook_appSecret: Secret of your facebook app (str)
    - facebook_pageUsername: Username of your facebook page (str)
    - facebook_socialEnabled: Enable facebook service or not (True or False)
    - recaptchaId: ID given by recaptcha (str)
    - recaptchaKey: Key given by recaptcha (str)
'''

class ConfigModel(BaseModel):
    field_name: str = Field(...)
    field_value: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "field_name": "recaptchaKey",
                "field_value": "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
            }
        }
