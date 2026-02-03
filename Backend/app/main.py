

from fastapi import FastAPI
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()


origins = [
    "http://localhost:3000", # Für Create-React-App
    "http://localhost:5173", # Für Vite
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

