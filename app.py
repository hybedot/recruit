from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import numpy as np
import pickle as p


app = Flask(__name__)
app.config['SECRET_KEY'] = 'blocking 4'

CORS(app)

api = Api(app)

modelfile = 'models/car_prediction.pickle'
model = p.load(open(modelfile, 'rb'))

class Predict(Resource):
    def post(self):
        json_data = request.get_json()
        
        try:
            condition = json_data['condition']
            mileage = json_data['mileage'] 
            year = json_data['year']

            prediction_data = [condition, mileage, year]

            prediction = np.array2string(model.predict([prediction_data]))

            prediction = prediction.strip('[]')


            return {
                    'status code':'200',
                    'message':prediction
                    }, 200
        except:
            return {
                    'status code':'500',
                    'message':'Invalid Values'
                    }, 500



#connect class with endpoint
api.add_resource(Predict, '/api/predict')

if __name__ == '__main__':
    app.run(debug=True)