from fastapi import FastAPI, Depends
import uvicorn

from auth.jwt_bearer import JWTBearer
from routes.admin import router as AdminRouter
from routes.post import router as PostRouter

app = FastAPI()

token_listener = JWTBearer()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Misato."}


app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
app.include_router(PostRouter, tags=["Post"], prefix="/post")

if __name__ == '__main__':
    uvicorn.run('app:app', host="0.0.0.0", port=4896, reload=True)
