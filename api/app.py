from flask import Flask, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from dotenv import load_dotenv
import os

# ====================
# LOAD ENV VARIABLES
# ====================
load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

app = Flask(__name__)

# ====================
# CONFIG DATABASE
# ====================
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ====================
# MODELS
# ====================

class Artist(db.Model):
    __tablename__ = 'Artist'
    ArtistId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(120), nullable=False)
    albums = db.relationship('Album', backref='artist', cascade='all, delete-orphan')

class Album(db.Model):
    __tablename__ = 'Album'
    AlbumId = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(160), nullable=False)
    ArtistId = db.Column(db.Integer, db.ForeignKey('Artist.ArtistId'), nullable=False)
    tracks = db.relationship('Track', backref='album', cascade='all, delete-orphan')

class MediaType(db.Model):
    __tablename__ = 'MediaType'
    MediaTypeId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(120))
    tracks = db.relationship('Track', backref='mediatype', cascade='all, delete-orphan')

class Track(db.Model):
    __tablename__ = 'Track'
    TrackId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(200), nullable=False)
    AlbumId = db.Column(db.Integer, db.ForeignKey('Album.AlbumId'), nullable=False)
    MediaTypeId = db.Column(db.Integer, db.ForeignKey('MediaType.MediaTypeId'), nullable=False)
    Milliseconds = db.Column(db.Integer, nullable=True)
    UnitPrice = db.Column(db.Float, nullable=True)

# ====================
# ROUTES
# ====================

@app.route('/')
def home():
    return jsonify({"message": "API InfraMusicStore is running"}), 200

# ---- CRUD ARTIST ----
@app.route('/artists', methods=['GET'])
def get_artists():
    artists = Artist.query.all()
    return jsonify([{'ArtistId': a.ArtistId, 'Name': a.Name} for a in artists])

@app.route('/artists/<int:id>', methods=['GET'])
def get_artist(id):
    a = Artist.query.get_or_404(id)
    return jsonify({'ArtistId': a.ArtistId, 'Name': a.Name})

@app.route('/artists', methods=['POST'])
def create_artist():
    data = request.get_json()
    new_artist = Artist(Name=data['Name'])
    db.session.add(new_artist)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Artist already exists"}), 400
    return jsonify({'ArtistId': new_artist.ArtistId, 'Name': new_artist.Name}), 201

@app.route('/artists/<int:id>', methods=['PUT'])
def update_artist(id):
    a = Artist.query.get_or_404(id)
    data = request.get_json()
    a.Name = data.get('Name', a.Name)
    db.session.commit()
    return jsonify({'ArtistId': a.ArtistId, 'Name': a.Name})

@app.route('/artists/<int:id>', methods=['DELETE'])
def delete_artist(id):
    a = Artist.query.get_or_404(id)
    db.session.delete(a)
    db.session.commit()
    return jsonify({'message': 'Deleted'}), 200

# ---- CRUD ALBUM ----
@app.route('/albums', methods=['GET'])
def get_albums():
    albums = Album.query.all()
    return jsonify([{'AlbumId': a.AlbumId, 'Title': a.Title, 'ArtistId': a.ArtistId} for a in albums])

@app.route('/albums/<int:id>', methods=['GET'])
def get_album(id):
    a = Album.query.get_or_404(id)
    return jsonify({'AlbumId': a.AlbumId, 'Title': a.Title, 'ArtistId': a.ArtistId})

@app.route('/albums', methods=['POST'])
def create_album():
    data = request.get_json()
    new_album = Album(Title=data['Title'], ArtistId=data['ArtistId'])
    db.session.add(new_album)
    db.session.commit()
    return jsonify({'AlbumId': new_album.AlbumId, 'Title': new_album.Title, 'ArtistId': new_album.ArtistId}), 201

@app.route('/albums/<int:id>', methods=['PUT'])
def update_album(id):
    a = Album.query.get_or_404(id)
    data = request.get_json()
    a.Title = data.get('Title', a.Title)
    a.ArtistId = data.get('ArtistId', a.ArtistId)
    db.session.commit()
    return jsonify({'AlbumId': a.AlbumId, 'Title': a.Title, 'ArtistId': a.ArtistId})

@app.route('/albums/<int:id>', methods=['DELETE'])
def delete_album(id):
    a = Album.query.get_or_404(id)
    db.session.delete(a)
    db.session.commit()
    return jsonify({'message': 'Deleted'}), 200

# ---- CRUD MEDIATYPE ----
@app.route('/mediatypes', methods=['GET'])
def get_mediatypes():
    mt = MediaType.query.all()
    return jsonify([{'MediaTypeId': m.MediaTypeId, 'Name': m.Name} for m in mt])

@app.route('/mediatypes/<int:id>', methods=['GET'])
def get_mediatype(id):
    m = MediaType.query.get_or_404(id)
    return jsonify({'MediaTypeId': m.MediaTypeId, 'Name': m.Name})

@app.route('/mediatypes', methods=['POST'])
def create_mediatype():
    data = request.get_json()
    new_mt = MediaType(Name=data['Name'])
    db.session.add(new_mt)
    db.session.commit()
    return jsonify({'MediaTypeId': new_mt.MediaTypeId, 'Name': new_mt.Name}), 201

@app.route('/mediatypes/<int:id>', methods=['PUT'])
def update_mediatype(id):
    m = MediaType.query.get_or_404(id)
    data = request.get_json()
    m.Name = data.get('Name', m.Name)
    db.session.commit()
    return jsonify({'MediaTypeId': m.MediaTypeId, 'Name': m.Name})

@app.route('/mediatypes/<int:id>', methods=['DELETE'])
def delete_mediatype(id):
    m = MediaType.query.get_or_404(id)
    db.session.delete(m)
    db.session.commit()
    return jsonify({'message': 'Deleted'}), 200

# ---- CRUD TRACK ----
@app.route('/tracks', methods=['GET'])
def get_tracks():
    tracks = Track.query.all()
    return jsonify([
        {
            'TrackId': t.TrackId,
            'Name': t.Name,
            'AlbumId': t.AlbumId,
            'MediaTypeId': t.MediaTypeId,
            'Milliseconds': t.Milliseconds,
            'UnitPrice': t.UnitPrice
        } for t in tracks
    ])

@app.route('/tracks/<int:id>', methods=['GET'])
def get_track(id):
    t = Track.query.get_or_404(id)
    return jsonify({
        'TrackId': t.TrackId,
        'Name': t.Name,
        'AlbumId': t.AlbumId,
        'MediaTypeId': t.MediaTypeId,
        'Milliseconds': t.Milliseconds,
        'UnitPrice': t.UnitPrice
    })

@app.route('/tracks', methods=['POST'])
def create_track():
    data = request.get_json()
    new_track = Track(
        Name=data['Name'],
        AlbumId=data['AlbumId'],
        MediaTypeId=data['MediaTypeId'],
        Milliseconds=data.get('Milliseconds'),
        UnitPrice=data.get('UnitPrice')
    )
    db.session.add(new_track)
    db.session.commit()
    return jsonify({
        'TrackId': new_track.TrackId,
        'Name': new_track.Name,
        'AlbumId': new_track.AlbumId,
        'MediaTypeId': new_track.MediaTypeId,
        'Milliseconds': new_track.Milliseconds,
        'UnitPrice': new_track.UnitPrice
    }), 201

@app.route('/tracks/<int:id>', methods=['PUT'])
def update_track(id):
    t = Track.query.get_or_404(id)
    data = request.get_json()
    t.Name = data.get('Name', t.Name)
    t.AlbumId = data.get('AlbumId', t.AlbumId)
    t.MediaTypeId = data.get('MediaTypeId', t.MediaTypeId)
    t.Milliseconds = data.get('Milliseconds', t.Milliseconds)
    t.UnitPrice = data.get('UnitPrice', t.UnitPrice)
    db.session.commit()
    return jsonify({
        'TrackId': t.TrackId,
        'Name': t.Name,
        'AlbumId': t.AlbumId,
        'MediaTypeId': t.MediaTypeId,
        'Milliseconds': t.Milliseconds,
        'UnitPrice': t.UnitPrice
    })

@app.route('/tracks/<int:id>', methods=['DELETE'])
def delete_track(id):
    t = Track.query.get_or_404(id)
    db.session.delete(t)
    db.session.commit()
    return jsonify({'message': 'Deleted'}), 200

@app.route("/docs")
def docs():
    return redirect("http://localhost:8081", code=302)

# ====================
# RUN SERVER
# ====================
if __name__ == "__main__":
    with app.app_context():
        app.run(host="0.0.0.0", port=5000)
