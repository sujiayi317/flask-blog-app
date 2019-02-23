
from flask import Flask
app = Flask(__name__)     # app is an instance of class Flask


@app.route("/")           # decorator route is what we type into our browser to go to different pages
def hello():
    return "<h1>Home Page!</h1>"  # html heading 1


if __name__ == '__main__':
    app.run(debug=True)
