from fastapi import FastAPI

app = FastAPI(version='1.0.0')


@app.get('/')
async def root():
    return 'FastAPI Auth App'

