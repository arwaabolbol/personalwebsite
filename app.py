from flask import Flask , render_template
from random import randint
y=["arwa","HI","oneee"]

app= Flask(__name__)
@app.route("/Hello")

def index():
	return "Hello world !"

@app.route("/goodbye")
def bye():
	return "Good bye"

@app.route("/myname")
def index3():

	return " My name is Arwa!!!!"""

@app.route("/web")
def rr():

	return render_template("homwwork.html")


@app.route('/')
def hi():
	return "hi"

if __name__=="__main__":
	app.run(port=7000, debug=True)