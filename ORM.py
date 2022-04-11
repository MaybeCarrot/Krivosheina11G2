from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # объект приложения Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db' # привязываем базу данных
db = SQLAlchemy(app) # создаем объект SQLAlchemy

from datetime import datetime

class Client(db.Model):
    id = db.Colummn(db.Integer, primary_key = True, unique = True, nallable = False)
    name = db.Column(db.String(100), nullable = False)
    sername = db.Column(db.String(100), nullable = False)
    date = db.Column(db.DateTime, nullable=False)
    born = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
        return f'{self.id} {self.name}'

class Types(db.Model):
    id = db.Colummn(db.Integer, primary_key = True, unique = True, nallable = False)
    name = db.Column(db.String(100), nullable = False)
    
    def __repr__(self):
        return f'{self.id} {self.name}'
    
class Goods(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True, nallable = False)
    type_id = db.Column(db.Integer, db.ForeignKey('Types.id'))
    name =db.Column(db.String(100), nullable = False)
    kol = db.Column(db.Integer, nullable = True)
    type = db.relationship('Types', backref=db.backref('streams', lazy=False))    
    
    def __repr__(self):
        return f'good kol {self.kol}' 
    
class Operation(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True, nallable = False)
    id_good = db.Column(db.Integer, db.ForeignKey('Goods.id'))
    id_client = db.Column(db.Integer, db.ForeignKey('Client.id'))
    kol = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    delivery_date = db.Column(db.DateTime, nullable=True)
    good = db.relationship('Goods', backref=db.backref('streams', lazy=False))    
    client = db.relationship('Client', backref=db.backref('streams', lazy=False))    
            
    def __repr__(self):
        return f'order operarion {self.order_date}'   
    
class Price(db.Model):
    good_id = db.Column(db.Integer, db.ForeignKey('Goods.id'))
    price = db.Column(db.Integer, nellable = False)
    date = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
        return f'price {self.price}'       
    
db.create_all()

client = Client(name="SQLAlchemy basics", lesson_amount=4)
db.session.add(client)
db.session.commit()

Courses.query.all()