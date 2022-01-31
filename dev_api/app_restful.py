from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api =  Api(app)

class desenvolvedor (Resource):
    def get(self):
        return  'Ola Dev !'
api.add_resource(desenvolvedor, '/dev')

if __name__ == '__main__':
    app.run()
