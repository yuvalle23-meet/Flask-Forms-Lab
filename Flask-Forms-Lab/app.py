from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "Yuvasl"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]




@app.route('/', methods = ['GET', 'POST'])  # '/' for the default page
def login():

	return render_template("login.html")

@app.route('/create', methods = ['GET', 'POST'])  # '/' for the default page
def login1():

	if request.method == "GET":
		return render_template("login.html")
	else:
		if request.form['username'] == username and request.form['password']==password:
			return render_template('home.html', friends = facebook_friends)
		else:
			return render_template("login.html")



@app.route('/friend_exists/<string:name>', methods = ['GET', 'POST'])  # '/' for the default page
def exist(name):
	return render_template("friend_exists.html", n = name)




if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)