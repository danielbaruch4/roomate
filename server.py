from typing import Union

from fastapi import FastAPI

import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}



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