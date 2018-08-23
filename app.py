from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.before_request
def before_request():
    print 'before_request'


@app.route('/')
def index():
    print 'request index'
    return render_template('hello.html')


@app.route('/home/<name>')
def home(name):
    name = '<h1>test</h1>'
    return render_template('hello.html', name=name)


@app.after_request
def after_request(response):
    print 'after_request'
    return response


if __name__ == '__main__':
    app.run(debug=True)
