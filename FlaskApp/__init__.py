from flask import Flask, render_template, Markup
import os
app = Flask(__name__)
@app.route("/")
def hello():
    files = '<h1> fjc</h1>'
    return render_template("me.html", content=files)
	
if __name__ == "__main__":
    app.run()
