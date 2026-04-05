from flask import Flask, render_template
#create the flask app
app = Flask(__name__)

#when someone visits homepage /, run below
@app.route("/")
#defins function that runs when user goes to homepage
def home():
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)

