from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import todo


origins = [
    "http://localhost:3000",
]


def create_application() -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(todo.router, prefix="/api/todo", tags=["todo"])
    return app


app = create_application()


@app.get("/")
def read_root():
    return {"ping": "pong"}
