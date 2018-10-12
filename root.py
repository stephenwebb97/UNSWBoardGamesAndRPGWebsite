from flask import  Flask, render_template,redirect,request,session,abort

app = Flask(__name__)



@app.route('/')
def root():
    return 'Hello, World'


@app.route('/boardgamesCounter')
def boardgamesCounter():
    return render_template('root.html')


@app.route('/ajax/boardgamesCounter', methods=['POST'])
def ajaxBoardgamesCounter():
    return "Submitted"


if __name__ == "__main__":
    app.run(debug=True)
