from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/bookings/')
def bookings():
    return render_template("bookings.html")  


@app.route('/about/')
def about():
    return render_template("about.html")   


@app.route('/settings/')
def settings():
    return render_template("settings.html")

if __name__ == "__main__":
	hello()
    