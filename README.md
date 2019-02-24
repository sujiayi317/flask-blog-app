# flask-blog-app

Learning flask using python to build a blog app.


KEY POINTS

1. Create Virtual Environments using virtualenv. 
2. Use the Flask framework to use Python as a Server Side Language. 
	pip install flask
	localhost (the port number): the IP address of the local machine, 127.0.0.1
	set (or export) FLASK_DEBUG = 1: activate the debugger
3. Create template directory in the project folder, which contains .html files.
4. Learned template inheritance, layout.html is the skeleton to be inherited, .html file extends layout.html.
5. Add navigation bar and global styles.
6. Mkdir statics to store stylesheets, Javascripts, images, here is main.css file, which is linked by layout.html <head>.
7. The function url_for() accepts the name of the function as an argument, which is useful 
because it will find the exact location of routes for us so that we don't need to worry about it in the background.
8. Forms - pip install flask-wtf, which is wtforms. In forms.py, the class RegistrationForm and LoginForm all inherit from FlaskForm, 
which is a class of flask_wtf.
9. In flaskblog.py module (later the __init__.py in the flaskblog package), add.config['SECRET_KEY']=..., in python we can
import secrets, secrets.token_hex(16) to generate the secret key.
10. The routes register and login use forms mentioned above, in register.html and login.html, the block content part should 
contain the form information.
11. Use database, pip install flask_sqlalchemy, from flask_sqlalchemy import SQLAlchemy, 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # /// means the relative path from the current file
db = SQLAchemy(app) # create db variable, which represent database structure as classes (models), each class is a table in the db.
12. In models.py, User and Post class inherit from db.Model.
13. Usage:
>>> from flaskblog import db
>>> db.create_all()   # then site.db is created in the current folder
>>> from flaskblog import User, Post
>>> user_1 = User(username='Jenny', email='Jenny@gmail.com, password='123456')
>>> db.session.add(user_1)
>>> user_2 = User(username='Tom', email='Tom@gmail.com, password='123456')
>>> db.session.commit()
>>> User.query.all()
[User('Jenny', 'Jenny@gmail.com', 'default.jpg'), User(...
>>> User.query.first()
User('Jenny', 'Jenny@gmail.com', 'default.jpg')
>>> User.query.filter_by(username='Jenny').all()
[User('Jenny', 'Jenny@gmail.com', 'default.jpg'), User(...
>>> User.query.filter_by(username='Jenny').first()
User('Jenny', 'Jenny@gmail.com', 'default.jpg')
>>> user = User.query.filter_by(username='Jenny').first()
>>> user
User('Jenny', 'Jenny@gmail.com', 'default.jpg')
>>> user.id
1
>>> user = User.query.get(1)
>>> user
User('Jenny', 'Jenny@gmail.com', 'default.jpg')
>>> user.posts
[]
>>> post_1 = Post(title='Blog 1', content='First Post Content!', user_id=user.id)
>>> post_2 = Post(title='Blog 2', content='Second Post Content!', user_id=user.id)
>>> db.session.add(post_1)
>>> db.session.add(post_2)
>>> db.session.commit()
>>> user.posts
[Post('Blog 1', (2019-02-23 22:32:43:462988'), Post(...)]
>>> for post in user.posts:
...     print(post.title)
...
Blog 1
Blog 2
>>> post = Post.query.first()
>>> post
Post('Blob 1'...
>>> post.user_id
1
>>> post.author
User('Jenny','Jenny@gmail.com','default.jpg')

>>> db.drop_all()
>>> db.create_all()
>>> User.query.all()
[]
14. Use package instead of module to avoid circular import
|-- flaskblog
|    |-- __init__.py
|    |-- forms.py
|    |-- models.py
|    |-- routes.py
|    |-- static
|    |    |-- main.css
|    |-- templates
|         |-- about.html
|         |-- home.html
|         |-- layout.html
|         |-- register.html
|-- run.py
15. Create database in cmd
>>> from flaskblog import db
>>> from flaskblog.models import User, Post
>>> db.create_all()
>>> User.query.all()
[]
