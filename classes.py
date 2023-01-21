"""Classes necessarias"""

from main import db

class Hero(object):
    def __init__(self, picture, name, description):
        self.picture = picture
        self.name = name
        self.description = description

class Selecao(db.Model):
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        picture = db.Column(db.String(400))
        name = db.Column(db.String(50), nullable=False)
        description = db.Column(db.String(500))

        def __repr__(self):
            return '<Name %r>' % self.name

class Vingadores(db.Model):
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        picture = db.Column(db.String(400))
        name = db.Column(db.String(50), nullable=False)
        description = db.Column(db.String(500))

        def __repr__(self):
            return '<Name %r>' % self.name

class Equipe(db.Model):
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        picture = db.Column(db.String(400))
        name = db.Column(db.String(50), nullable=False)
        description = db.Column(db.String(500))

        def __repr__(self):
            return '<Name %r>' % self.name