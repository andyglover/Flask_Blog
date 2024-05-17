from datetime import datetime, timezone
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
import pytz

app = Flask(__name__)
app.config['SECRET_KEY'] = '46e8e5a05609c89707c1299f8aaace4f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['TIMEZONE'] = 'America/Los_Angeles'
db = SQLAlchemy(app)

# Helper Functions for Timezone Conversion
def utc_to_local(utc_dt):
    local_tz = pytz.timezone(app.config['TIMEZONE'])
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt)  # .normalize might be unnecessary for some cases

def local_to_utc(local_dt):
    local_tz = pytz.timezone(app.config['TIMEZONE'])
    utc_dt = local_tz.localize(local_dt).astimezone(pytz.utc)
    return utc_dt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}', '{utc_to_local(self.date_posted)}')"
 
    # The tutorial suggests using datetime.utcnow() at date_posted column insertion, which is now deprecated.
    # datetime.now(timezone.utc) returns a "timezone-aware" datetime object. 
    # You can't remove the perens from this because you need to pass a timezone argument.
    # so including "lambda:" ensures deferred execution, generating the time at column insertion.
    #
    # sqlite doesn't natively support timezone aware, so pytz and helper functions are utilized.
    # Store the datetime as naive UTC in the database and convert on retrieval and setting
    # (Removed timezone=True from db.Column(db.DateTime(timezone=True)...)


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    },
]

@app.route("/")
@app.route("/home")
def home():
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