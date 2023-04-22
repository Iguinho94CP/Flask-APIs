# Author: Igor Pantaleão
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/igorp/Documents/flask_projects/imdb.db"
# initialize the app with the extension
db.init_app(app)
migrate = Migrate(app, db)


class Movie(db.Model):
   __tablename__ = 'movies'
   id = db.Column(db.Integer, primary_key=True)
   Movie_title = db.Column(db.String)
   Year = db.Column(db.String)
   Genre = db.Column(db.String)
   Rating = db.Column(db.String)
   Description = db.Column(db.String)
   Duration = db.Column(db.String)
   Gross = db.Column(db.String)
   Images = db.Column(db.String)
   Actors = db.Column(db.String)
   Actress = db.Column(db.String)
   director_id = db.Column(db.Integer, db.ForeignKey('directors.id', name='fk_movie_director'))
   director = db.relationship('Director', backref='movies')


class Director(db.Model):
   __tablename__ = 'directors'
   id = db.Column(db.Integer, primary_key=True)
   Director = db.Column(db.String)
   Gross = db.Column(db.String)
   Rating = db.Column(db.String)



with app.app_context():
	db.create_all()


@app.route('/', methods=['GET'])
def home():
	movies = Movie.query.all()
	movie_list = []
	for movie in movies:
		movid_dct = {
			'title': movie.Movie_title,
			'year': movie.Year,
			'genre': movie.Genre,
			'rating': movie.Rating,
			'description': movie.Description,
			'duration': movie.Duration,
			'gross': movie.Gross,
			'images': movie.Images,
			'actors': movie.Actors,
			'actress': movie.Actress
		}


if __name__== "__main__":
	app.run(debug=True)
