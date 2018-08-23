# encoding=utf-8

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


# @app.before_request
# def before_request():
#     print 'before_request'


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/home/<name>')
def home(name):
    return render_template('hello.html', name=name)


@app.route('/home/test')
def test():
    return render_template('index.html')

# @app.after_request
# def after_request(response):
#     print 'after_request'
#     return response


if __name__ == '__main__':
    app.run(debug=True, port=5001)
