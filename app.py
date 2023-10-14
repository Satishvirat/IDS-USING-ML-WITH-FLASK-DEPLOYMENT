import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)

    if prediction == 'normal':
        prediction_text = "The connection is Normal, No intrusion detected."
        out = "green"
    elif prediction == 'dos':
        prediction_text = "Intrusion detected: We suspect a Denial of Service (DOS) attack."
    elif prediction == 'probe':
        prediction_text = "Intrusion detected: We suspect a Probe attack."
    elif prediction == 'r2l':
        prediction_text = "Intrusion detected: We suspect an unauthorized access (R2L) attack."
    elif prediction == 'u2r':
        prediction_text = "Intrusion detected: We suspect a user-to-root (U2R) attack."
    else:
        prediction_text = "Unknown intrusion type."

    return render_template("index.html", prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
