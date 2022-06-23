from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': 'Max'}}

@app.get('/about')
def about():
    return {'data': 'about page'}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True, debug=True)
