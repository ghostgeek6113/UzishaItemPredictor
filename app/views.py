import pickle
from werkzeug.routing import ValidationError
from app import app
from flask import request, jsonify
from app.models import item_details
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Predict Item Price"
    }
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)


# Setting all our routes regarding the prediction of prices

@app.route('/')
def home():
    try:
        return "Welcome to predict", 200
    except ValueError:
        return "API Not working", 404


@app.route('/predict', methods=['POST'])
def predict():
    try:
        json_ = request.json
        items = item_details.Items(json_).jsonify_input()
        print(items)
        clf = pickle.load(open('app/algorithm/model.pkl', 'rb'))
        prediction = list(clf.predict(items))
        return jsonify({'prediction': str(prediction)}), 200
    except ValidationError:
        return jsonify({"Error": "Invalid Request, please try again."}), 400
