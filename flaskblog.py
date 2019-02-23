
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)     # app is an instance of class Flask

app.config['SECRET_KEY'] = '7f12a1f7152a6858c852428551e29dab'

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


@app.route("/")  # decorator route is what we type into our browser to go to different pages
@app.route("/home")
def home():
    # return "<h1>Home Page</h1>"  # html heading 1
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
