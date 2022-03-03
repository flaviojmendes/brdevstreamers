
from model.initializer import init_db
from dotenv import dotenv_values
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from controller.public_api import app_public
from controller.private_api import app_private
from fastapi.middleware.gzip import GZipMiddleware

config = dotenv_values(".env")

init_db()
origins = ["*"]

app = FastAPI()

app.mount("/api", app_private)
app.mount("/public", app_public)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware)

if __name__ == '__main__':
    if(config["ENV"] == 'prod'):
        uvicorn.run("main:app",
                    host="0.0.0.0",
                    port=8000,
                    reload=True,
                    ssl_keyfile=config["PRIVATE_KEY"],
                    ssl_certfile=config["CERT"]
                    )
    else:
        uvicorn.run("main:app",
                    host="0.0.0.0",
                    port=8000,
                    reload=True
                    )
