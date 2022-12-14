import os
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for
)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

import env


app = Flask(__name__)

app.config["MONGO_DBNANE"] = os.environ.get("MONGO_DBNANE")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_movies')
def get_movies():
    movies = mongo.db.movies.find()
    return render_template("movies.html", movies=movies)


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
