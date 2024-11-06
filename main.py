from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title=Backstract Generated APIs - jittery-migre-coll-1ec8549fe54c4a0985f4340d08bdd433,debug=False,docs_url=keen-omkar-a5985d609c0d11ef8bda0242c0a8900213/docs,openapi_url=keen-omkar-a5985d609c0d11ef8bda0242c0a8900213/openapi.json)

app.include_router(router, prefix='/keen-omkar-a5985d609c0d11ef8bda0242c0a8900213/api', tags=['APIs v1'])

def run_h11():
    uvicorn.run('main:app', host='0.0.0.0', port=8008, reload=True)

if __name__ == '__main__':
    run_h11()