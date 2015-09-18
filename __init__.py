from flask import(
        Flask,
        render_template,
		request
)
app = Flask(__name__)

@app.route("/")
@app.route("/transcode")
def hello():
    return render_template("index.html")
 
@app.route("/Credits")
def credits():
    return render_template("credits.html")
 