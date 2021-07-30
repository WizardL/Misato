from typing import Optional

from pydantic import BaseModel, Field


class PostModel(BaseModel):
    content: str = Field(...)
    imageLink: str = Field(...)
    approved: float = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "content": "Misato my waifu",
                "imageLink": "https://user-images.githubusercontent.com/3853064/127108303-6895eb8b-c249-4044-9ae5-28b3c73cbb7e.png",
                "approved": False,
            }
        }


class AddPostModel(BaseModel):
    content: str = Field(...)
    imageLink: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "content": "Misato my waifu",
                "imageLink": "https://user-images.githubusercontent.com/3853064/127108303-6895eb8b-c249-4044-9ae5-28b3c73cbb7e.png",
            }
        }


class UpdatePostModel(BaseModel):
    content: Optional[str]
    imageLink: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "content": "Misato my waifu",
                "imageLink": "https://user-images.githubusercontent.com/3853064/127108303-6895eb8b-c249-4044-9ae5-28b3c73cbb7e.png",
            }
        }

def ResponseModel(data, message):
    return {
        "data": [
            data
        ],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }
