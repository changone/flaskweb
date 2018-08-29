# encoding=utf-8

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms.LoginForm import LoginForm

app = Flask(__name__, template_folder='templates')
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hardtoguessstring'
# @app.before_request
# def before_request():
#     print 'before_request'


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/home/<name>')
def home(name):
    return render_template('user.html', name=name)


@app.route('/home/test')
def test():
    return render_template('test.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(email=form.email.data).first()
    # if user is not None and user.verify_password(form.password.data):
    #     login_user(user, form.remember_me.data)
    #     return redirect(request.args.get('next') or url_for('main.index'))
    # flash('Invalid username or password.')
    return render_template('auth/index.html', form=form)


# @app.after_request
# def after_request(response):
#     print 'after_request'
#     return response


if __name__ == '__main__':
    app.run(debug=True, port=5001)
