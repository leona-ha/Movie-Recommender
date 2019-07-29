import numpy as np
import pandas as pd
import pickle as picklerick
from sklearn.decomposition import NMF
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table


engine = create_engine(f'postgres://postgres:postgres@localhost/movielens')
base = declarative_base(engine)
Session = sessionmaker(engine)
session = Session()
metadata = base.metadata
ratings = Table('ratings', metadata, autoload=True)
movies = Table('movies', metadata, autoload=True)
tags = Table('tags', metadata, autoload=True)
umr = Table('user_movie_ratings', metadata, autoload=True)


def retrain_nmf():
    #this is a function which retrains periodically my nmf model
    #it should be trained on the latest user-ratings matrix available
    R = np.array(session.query(umr).all()).T
    #create a model and set the hyperparameters
    # model assumes R ~ PQ'
    model = NMF(n_components=2, init='random', random_state=10)
    model.fit(R)
    Q = model.components_  # movie-genre matrix
    P = model.transform(R)  # user-genre matrix
    error = model.reconstruction_err_ #reconstruction error
    nR = np.dot(P, Q) #the reconstructed matrix
    #pickle my model
    list_pickle_path = 'nmf.pkl'
    nmf_pickle = open(list_pickle_path, 'wb')
    picklerick.dump(model, nmf_pickle)
    nmf_pickle.close()
    return


def get_ml_recommendations(user_input):
    #load an nmf model
    list_pickle_path = 'nmf.pkl'
    nmf_unpickle = open(list_pickle_path, 'rb')
    model = picklerick.load(nmf_unpickle)
    query = user_input

    #find out the movie_id for each movie title
    movie_titles = [x[0] for x in query]
    movie_ratings = [x[1] for x in query]

    movie_ids = []
    for title in movie_titles:
        db_result = session.query(movies).filter(movies.columns.title.ilike(f'%{title}%')).limit(1).all()
        movie_ids.append(db_result[0][0])

    #THIS STEP RUNS SLOWLY, OPTIMIZE LATER
    #create an array of len == no. of columns in umr
    data_len = 9724#len(list(session.query(umr).all()))
    query = np.ones(data_len)

    for i in range(len(movie_ids)):
        query[movie_ids[i]] = movie_ratings[i]


    Q = model.components_
    #in this case, a new user providing ratings for the 5 movies.
    R_pred = model.transform(np.array(query).reshape(-1,data_len))
    R_pred = np.dot(R_pred,Q)
    result = ""
    element = R_pred.argmax()

    for each in session.query(movies).all():
        if each[0] == element:
            result = each

    #use trained model to predict movies
    return result
