# flask-blog-app

Learning flask using python to build a blog app.


## KEY POINTS

1. Create Virtual Environments
    - use virtualenv. 
2. Use the Flask framework to use Python as a Server Side Language. 
    - pip install flask
    - localhost (the port number): the IP address of the local machine, 127.0.0.1
    - set (or export) FLASK_DEBUG = 1: activate the debugger
3. Mkdir templates
    - in the project folder, contains .html files.
4. Learned template inheritance
    - layout.html is the skeleton to be inherited, .html file extends layout.html
5. Add navigation bar and global styles.
6. Mkdir statics
    - store stylesheets, Javascripts, images...
    - here is main.css file, which is linked by layout.html <head>
7. The function url_for()
    - accepts the name of the function as an argument, which is useful
    - finds the exact location of routes so that we don't need to worry about it in the background
8. Forms
    - pip install flask-wtf, which is wtforms. 
    - in forms.py, the class RegistrationForm and LoginForm all inherit from FlaskForm, which is a class of flask_wtf
9. Secret Key
    - in flaskblog.py module (later the __init__.py in the flaskblog package)
    - add.config['SECRET_KEY']=...
    - import secrets, secrets.token_hex(16) to generate the secret key
10. The routes register and login use forms mentioned above, in register.html and login.html, the block content part should 
contain the form information.
11. Use database
    - pip install flask_sqlalchemy
    - from flask_sqlalchemy import SQLAlchemy
    - app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # /// means the relative path from the current file
    - db = SQLAchemy(app) # create db variable, representing database structure as classes (models), each class is a table in the db.
12. In models.py, User and Post class inherit from db.Model.
13. Usage:
```
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
```
14. Use package instead of module to avoid circular import
```
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
```
15. Create database in cmd
```
>>> from flaskblog import db
>>> from flaskblog.models import User, Post
>>> db.create_all()
>>> User.query.all()
[]
```
16. User Authentification. Hash and verify passwords
     - pip install flask-bcrypt

```
>>> from flask_bcrypt import Bcrypt
>>> bcrypt = Bcrypt()
>>> bcrypt.generate_password_hash('testing')
b'$2b$12$5vFSM9rpR3XULgIbkpRYVuCj27ssQJyXUrWLbyaJNmz.6cF10AO96'
>>> bcrypt.generate_password_hash('testing').decode('utf-8')
'$2b$12$iiicRu9QQ/WSf8NiY149Y.jH.7GfvDDbbvzjpUHDq3Sp7craz.Qte'
>>> hashed_pw = bcrypt.generate_password_hash('testing').decode('utf-8')
>>> bcrypt.check_password_hash(hashed_pw, 'password')
False
>>> bcrypt.check_password_hash(hashed_pw, 'testing')
True
```
17. Users can login and logout
     - pip install flask-login
     - LoginManager, UserMixin, login_user, current_user
     - navigation bar
     - correct create account page
     - must login to see the account page
     - if not logged in, account route redirect user to login page
     - redirect to *next page* using flask.request.args.get('next'), or *None* to 'home'
18. Account form and profile picture
     - users can update, field already filled for users
     - don't forget enctype="multipart/form-data" in account.html
     - auto-resize image when uploading: pip install Pillow
19. Create, update and delete posts
     - save newly created post to database and desplay it on home page
     - delete botton, extra confirmation, using [bootstrap code](https://getbootstrap.com/docs/4.0/components/modal/#live-demo)
20. Pagination
     - posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)

```
>>> from flaskblog.models import Post
C:\Users\JIAYIS~1\Desktop\ENVIRO~1\PROJEC~1\lib\site-packages\flask_sqlalchemy\__init__.py:794: FSADe
precationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by de
fault in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
>>> post = Post.query.all()
>>> posts = Post.query.all()
>>> for post in posts:
...     print(post)
...
Post('My first Updated Post', '2019-02-25 15:41:55.448295')
Post('A Second Post', '2019-02-25 16:20:39.511205')
Post('Programming languages for a qualified full stack developer', '2019-02-25 21:56:23.555072')
Post('Front-end technology', '2019-02-25 21:57:22.307062')
Post('Back-End Developer - skills and tools', '2019-02-25 22:03:24.162886')
Post('Ruby learning order', '2019-02-25 22:12:42.078326')
Post('Pros and cons of Flask and Django', '2019-02-25 22:19:40.784217')
Post('Flask:', '2019-02-25 22:25:19.160750')
Post('Django framework: ', '2019-02-25 22:25:58.257603')
Post('Popular applications and services built with Python', '2019-02-25 22:26:57.504383')
Post('Open Source Projects', '2019-02-25 23:01:59.716831')
Post('The most distilled way to improve a Github profile', '2019-02-25 23:04:11.207612')
Post('Python in Artificial Intelligence (AI):', '2019-02-25 23:37:13.325630')
Post('Python in Big Data', '2019-02-25 23:37:26.905883')
Post('Python in Data Science:', '2019-02-25 23:37:48.344707')
Post('Python in Testing Frameworks:', '2019-02-25 23:38:05.390772')
Post('Python in Web Development:', '2019-02-25 23:38:41.192807')
Post('3 main popular applications for Python', '2019-02-25 23:56:10.878898')
Post('Popular machine learning algorithms', '2019-02-25 23:57:40.065928')
Post('What is Java?', '2019-02-26 00:02:22.124745')
Post('Practice Coding', '2019-02-26 00:06:30.528135')
Post('AI automates repetitive learning and discovery through data. ', '2019-02-26 00:09:09.731899')
Post('AI adds intelligence', '2019-02-26 00:09:30.662352')
Post('AI adapts through progressive learning algorithms', '2019-02-26 00:09:49.213537')
Post('AI analyzes more and deeper data', '2019-02-26 00:10:06.594489')
Post('AI achieves incredible accuracy', '2019-02-26 00:10:27.713606')
Post('AI gets the most out of data', '2019-02-26 00:10:45.401517')
>>> posts = Post.query.paginate()
>>> posts
<flask_sqlalchemy.Pagination object at 0x000002183FF70BE0>
>>> dir(posts)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__g
etattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module_
_', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__s
tr__', '__subclasshook__', '__weakref__', 'has_next', 'has_prev', 'items', 'iter_pages', 'next', 'nex
t_num', 'page', 'pages', 'per_page', 'prev', 'prev_num', 'query', 'total']
>>> posts.per_page
20
>>> posts.page
1
>>> for post in posts.items:
...     print(post)
...
Post('My first Updated Post', '2019-02-25 15:41:55.448295')
Post('A Second Post', '2019-02-25 16:20:39.511205')
Post('Programming languages for a qualified full stack developer', '2019-02-25 21:56:23.555072')
Post('Front-end technology', '2019-02-25 21:57:22.307062')
Post('Back-End Developer - skills and tools', '2019-02-25 22:03:24.162886')
Post('Ruby learning order', '2019-02-25 22:12:42.078326')
Post('Pros and cons of Flask and Django', '2019-02-25 22:19:40.784217')
Post('Flask:', '2019-02-25 22:25:19.160750')
Post('Django framework: ', '2019-02-25 22:25:58.257603')
Post('Popular applications and services built with Python', '2019-02-25 22:26:57.504383')
Post('Open Source Projects', '2019-02-25 23:01:59.716831')
Post('The most distilled way to improve a Github profile', '2019-02-25 23:04:11.207612')
Post('Python in Artificial Intelligence (AI):', '2019-02-25 23:37:13.325630')
Post('Python in Big Data', '2019-02-25 23:37:26.905883')
Post('Python in Data Science:', '2019-02-25 23:37:48.344707')
Post('Python in Testing Frameworks:', '2019-02-25 23:38:05.390772')
Post('Python in Web Development:', '2019-02-25 23:38:41.192807')
Post('3 main popular applications for Python', '2019-02-25 23:56:10.878898')
Post('Popular machine learning algorithms', '2019-02-25 23:57:40.065928')
Post('What is Java?', '2019-02-26 00:02:22.124745')
>>> posts = Post.query.paginate(page=2)
>>> for post in posts.items:
...     print(post)
...
Post('Practice Coding', '2019-02-26 00:06:30.528135')
Post('AI automates repetitive learning and discovery through data. ', '2019-02-26 00:09:09.731899')
Post('AI adds intelligence', '2019-02-26 00:09:30.662352')
Post('AI adapts through progressive learning algorithms', '2019-02-26 00:09:49.213537')
Post('AI analyzes more and deeper data', '2019-02-26 00:10:06.594489')
Post('AI achieves incredible accuracy', '2019-02-26 00:10:27.713606')
Post('AI gets the most out of data', '2019-02-26 00:10:45.401517')
>>> posts = Post.query.paginate(per_page=5)
>>> posts.page
1
>>> for post in posts.items:
...     print(post)
...
Post('My first Updated Post', '2019-02-25 15:41:55.448295')
Post('A Second Post', '2019-02-25 16:20:39.511205')
Post('Programming languages for a qualified full stack developer', '2019-02-25 21:56:23.555072')
Post('Front-end technology', '2019-02-25 21:57:22.307062')
Post('Back-End Developer - skills and tools', '2019-02-25 22:03:24.162886')
>>> posts = Post.query.paginate(per_page=5, page=2)
>>> posts.page
2
>>> for post in posts.items:
...     print(post)
...
Post('Ruby learning order', '2019-02-25 22:12:42.078326')
Post('Pros and cons of Flask and Django', '2019-02-25 22:19:40.784217')
Post('Flask:', '2019-02-25 22:25:19.160750')
Post('Django framework: ', '2019-02-25 22:25:58.257603')
Post('Popular applications and services built with Python', '2019-02-25 22:26:57.504383')
>>> posts.total
27
>>>
```

     - show the newest posts on top
```
posts = Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
```
     
     - desplay a new route with posts from a particular user

21. Use email to allow users to reset passwords
     - usage of TimedJSONWebSignatureSerializer
```
>>> from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
>>> s = Serializer('secret', 30)
>>> token = s.dumps({'user_id': 1}).decode('utf-8')
>>> token
'eyJhbGciOiJIUzUxMiIsImlhdCI6MTU1MTI4NDEzOCwiZXhwIjoxNTUxMjg0MTY4fQ.eyJ1c2VyX2lkIjoxfQ.BmgsjI4UBr9-sieP_42Q8anQyWINaiyngaUEuahUEWi5_Lms8dU2V7HjYtPHxnhKY4HBYCQl7vmsmSeH_P4HeQ'
>>> s.loads(token)
{'user_id': 1}
>>> s.loads(token)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "C:\Users\Jiayi Su\Desktop\Environments\project1_env\lib\site-packages\itsdangerous\jws.py", line 205, in loads
    date_signed=self.get_issue_date(header),
itsdangerous.exc.SignatureExpired: Signature expired
```
     - pip install flask_mail
```
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='sujiayi317@gmail.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
```

22. Restructure the application & Blueprints
     - move configuration variables into their own file
     - move the creation of the application into its own function, to allow different instance with configuration
     - app factory (testing + production)
     - import Blueprint objects from each of those packages and register them with the route

```
|-- flaskblog
|    |-- __init__.py
|    |-- config.py
|    |-- main
|         |-- __init__.py
|         |-- routes.py
|    |-- models.py
|    |-- posts
|    |    |-- __init__.py 
|    |    |-- forms.py 
|    |    |-- routes.py 
|    |-- site.db
|    |-- statics
|    |    |-- main.css 
|    |    |-- profile_pics 
|    |         |-- default.jpg...
|    |-- templates
|    |    |-- about.html
|    |    |-- account.html
|    |    |-- create_post.html
|    |    |-- home.html
|    |    |-- layout.html
|    |    |-- login.html
|    |    |-- post.html
|    |    |-- register.html
|    |    |-- reset_request.html
|    |    |-- reset_token.html
|    |    |-- user_posts.html
|    |-- users
|         |-- __init__.py 
|         |-- forms.py 
|         |-- routes.py
|         |-- utils.py
|-- run.py
```

23. Add custom error pages to the application
     - easy to add new blueprints to the app
     - in flask a second value, which is the status code (default: 200), could be returned with render_template
        - 403 Error: forbidden response
        - 500 Error: general server error
     - register blueprints with the application in __init__.py