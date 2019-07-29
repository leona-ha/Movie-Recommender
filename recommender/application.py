from flask import Flask
from flask import render_template, request
from recommender import get_ml_recommendations, retrain_nmf

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('bootstrap.html')

@app.route('/recommender')
def show_recommender():
    user_input = list(request.args.to_dict().items())
    recommendation = get_ml_recommendations(user_input)
    return render_template('data.html', data=recommendation)

@app.route('/train')
def train_nmf():
    retrain_nmf()
    return render_template('retrain.html')

@app.route('/data')
def show_data():
    results = find_some_data()
    return render_template('data.html', data=results)
