from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/about/')
def about():
    return "<h3>This is a Flask web application.</h3>"    

    
if __name__ == "__main__":
	hello()