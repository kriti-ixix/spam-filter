import pickle
from flask import Flask, render_template, request


app = Flask(__name__)
loadedModel = pickle.load(open('Model.pkl', 'rb'))


@app.route("/")
def home():
    return render_template('form.html')


@app.route("/predict", methods=["POST"])
def predict():
    name = request.form['name']
    message = request.form['message']

    prediction = loadedModel.predict([message])[0]

    if prediction == 'ham':
        prediction = "Genuine Message"
    else:
        prediction = "Spam Message"

    return render_template('form.html', api_message=message, api_output=prediction)


if __name__ == '__main__':
    app.run(debug=True)