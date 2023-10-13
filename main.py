from fastapi import FastAPI
from api.endpoint.router import router


app = FastAPI()
app.include_router(router)
