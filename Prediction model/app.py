import numpy as np
from flask import Flask,render_template,request

import pickle

flask_app = Flask(__name__)

model = pickle.load(open("model.pkl","rb"))


@flask_app.route("/")
def home():
    return render_template("index.html")
@flask_app.route("/predict", methods=["POST"])

def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)

    return render_template("index.html", prediction_text="The predicted crop is {}".format(prediction))

if __name__ == "__main__":
    flask_app.run(debug=True)