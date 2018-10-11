from flask import  Flask, render_template,redirect,request,session,abort

app = Flask(__name__)


@app.route('/')
def root():
    return 'Hello, World'


@app.route('/boardgamesCounter')
def test(name):
    return render_template('root.html', name=name)


@app.route('/ajax/boardgamesCounter')
def boardgamesCounter():
    return "Submitted"


if __name__ == "__main__":
    app.run(debug=True, ssl_context='adhoc')
