from flask import Flask
from fastapi import FastAPI
print("flask server")


app = Flask(__name__)
print(__name__)

@app.route('/')
def test():
    return 'HOME PAGErrrsdasdadasr1'

@app.route('/hello')
def hello():
    return 'Hello, World!'
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=False)