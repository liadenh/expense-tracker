from flask_sqlalchemy import SQLAlchemy
#create db
db = SQLAlchemy()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True) #auto increments, each has a unique id
    name = db.Column(db.String(50), nullable=False) #name cannot be null
    #category.transactions gives all transactions in this category
    transactions = db.relationship('Transaction', backref='category')
    #category.goal gives goal, uselist=False means theres only one goal per category
    goal = db.relationship('Goal', backref='category', uselist=False)
#this class represents a table called transaction
#table with id, item, price, date, notes, category_id
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable = False)
    price = db.Column(db.Float, nullable = False)
    date = db.Column(db.Date, nullable = False)
    description = db.Column(db.String(200))
    #foreign key to category table, each transaction linked to a category
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    #foreign key to category table, each goal linked to a category
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)