# Author: Igor Pantaleão
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
db.init_app(app)

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thumbnail = db.Column(db.String)
    link = db.Column(db.String)
    publication_date = db.Column(db.String)

    def serialize(self):
        title = self.link.split('/')[-2]
        return {
            'id': self.id,
            'thumbnail': self.thumbnail,
            'link': self.link,
            'publication_date': self.publication_date,
            'title': title
        }

with app.app_context():
    db.create_all()


@app.route('/api/news', methods=['GET'])
def home():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    news = News.query.paginate(page=page, per_page=per_page)

    return jsonify(
            {
                'news': [new.serialize() for new in news.items],
                'total_pages': news.pages,
                'total_items': news.total
            }
        ), 200



if __name__ == "__main__":
    app.run(debug=True)
