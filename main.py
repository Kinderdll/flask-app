from flask import Flask, render_template, request, redirect, url_for
from models import db, User

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable unnecessary tracking
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    username = request.form['username']
    email = request.form['email']
    
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=9000)
