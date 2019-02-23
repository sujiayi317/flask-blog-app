
from flask import Flask, render_template, url_for
app = Flask(__name__)     # app is an instance of class Flask

posts = [
    {
        'author': 'Jiayi Su',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 20, 2019'
    },
    {
        'author': 'Bernard Dong',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'February 21, 2019'
    }
]


@app.route("/")           # decorator route is what we type into our browser to go to different pages
@app.route("/home")
def home():
    # return "<h1>Home Page</h1>"  # html heading 1
    return render_template('home.html', posts=posts)


@app.route("/about")           # decorator route is what we type into our browser to go to different pages
def about():
    # return "<h1>About Page</h1>"  # html heading 1
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
