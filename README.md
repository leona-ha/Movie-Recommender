## Travis
[![Build Status](https://travis-ci.com/leona-ha/Movie-Recommender.svg?branch=master)](https://travis-ci.com/leona-ha/Movie-Recommender)

## Movie-Recommender
Build a software system that gives movie recommendations and create a web interface using Flask.

### Data
Movies and ratings are collected from the Movielens Dataset for education and development
* https://grouplens.org/datasets/movielens/

### Model: Unsupervised Learning using Non-negative Matrix Factorization (NMF)
* Using matrix factorization, find some latent, "hidden" features that determine how a user rates an item.
After discovering these hidden features we should be able to predict a rating with respect to a certain user and a certain item, because the features associated with the user should match with the features associated with the item.
* Task: Find two matrices P (user * features) and Q (movie * features) such that their product approximates R (the User * Movie matrix)

### Final product: A Web Interface running the NMF prediction on the server
