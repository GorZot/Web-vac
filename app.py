from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newflask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    salary = db.Column(db.Text, nullable=False)
    duties = db.Column(db.Text, nullable=False)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        salary = request.form['salary']
        duties = request.form['duties']

        post = Post(duties=duties, title=title, salary=salary)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except:
            return 'При добавлении вакансии произошла ошибка'
    else:
        return render_template('create.html')


@app.route('/reg', methods=['POST', 'GET'])
def reg():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        user = Users(name=name, password=password)

        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/')

        except:
            return 'При добавлении пользователя произошла ошибка'
    else:
        return render_template('reg.html')



if __name__ == '__main__':
    app.run(debug=True)