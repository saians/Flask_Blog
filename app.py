from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ce7d24eb25b21ffe42be00c24ed6d034'

posts = [
    {
        'author': 'Saifullah',
        'title': 'Blog post 1',
        'content': 'This is a test content 1',
        'date_posted': 'November 28,2018'
    },
    {
        'author': 'Ansari',
        'title': 'Blog post 2',
        'content': 'This is a test content 1',
        'date_posted': 'November 28,2018'
    },
    {
        'author': 'Saians',
        'title': 'Blog post 3',
        'content': 'This is a test content 1',
        'date_posted': 'November 28,2018'
    }

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
        flash(f'Account created for  {form.username.data}!', 'success')
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
            flash('Login Unsuccessful. please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
