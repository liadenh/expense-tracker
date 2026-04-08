from flask import Flask, render_template, request, redirect

from models import db, Category, Transaction, Goal
#create the flask app
app = Flask(__name__)

#use sqlLite save as file called expenses.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
#connect database to flask app (joins models.py to this app.py)
db.init_app(app)

#when someone visits homepage /, run below
@app.route("/")
#defins function that runs when user goes to homepage
def home():
	#grab all transactions, categories, and goals from database
	transactions = Transaction.query.all()
	categories = Category.query.all()
	goals = Goal.query.all()
	return render_template("index.html", transactions=transactions, categories=categories, goals=goals) #render index.html and pass in transactions, categories, and goals to be used in the template
@app.route("/add", methods=["POST"])
def add():
	#request.form is everything user types in
	item = request.form.get('item')
	price = request.form.get('price')
	date = request.form.get('date')
	category_id = request.form.get('category_id')
	description = request.form.get('description')

	#convert date from string into date object db understands
	from datetime import datetime
	date = datetime.strptime(date, '%Y-%m-%d').date()

	#create new row in table with data
	new_transaction = Transaction(
		item=item,
		price=float(price),
		date=date,
		category_id=int(category_id),
		description=description
	)
	db.session.add(new_transaction) #stage it to be saved
	db.session.commit() #save change commits to database
	return redirect("/") #after adding, go back to homepage

@app.route("/delete/<int:id>", methods=["GET"])
def delete(id):
	#find transaction with given id and delete it or return error not found
	transaction = Transaction.query.get_or_404(id)
	db.session.delete(transaction) #stage it to be deleted
	db.session.commit() #save change commits to database
	return redirect("/") #after deleting, go back to homepage

if __name__ == "__main__":
	with app.app_context():
		db.create_all() #create tables in database based on models.py
	
		if Category.query.count() == 0: #if there are no categories, add some default ones
			default_categories = ['Eating Out', 'Transportation', 'Entertainment', 'Utilities', 'Groceries', 'Other']
			for name in default_categories:
				category = Category(name=name) #create new row in category table
				db.session.add(category) #stage it to be saved
			db.session.commit() #save change commits to database
	app.run(debug=True)

