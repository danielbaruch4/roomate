from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# if __name__ == "__main__":
#     uvicorn.run('server:app',port=5000,host="0.0.0.0",reload=True)



# from flask import Flask
# print("flask server")


# app = Flask(__name__)
# print(__name__)

# @app.route('/')
# def test():
#     return {'data':[1,2,3]}

# @app.route('/hello')
# def hello():
#     return 'Hello, World!'
    
# if __name__ == '__main__':
#   app.run(host='0.0.0.0', debug=False)