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

@app.after_request
def gnu_terry_pratchett(resp):
 resp.headers.add("X-Clacks-Overhead", "GNU Terry Pratchett")
 return resp

if __name__ == "__main__":
 app.debug = True
 app.run(debug=True)