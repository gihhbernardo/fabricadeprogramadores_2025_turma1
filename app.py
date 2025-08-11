from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello world,/h1>'

@app.route('/home')
def home():
    return '<h1>bem-vindo a home,/h1>'


app.add_url_rule('/','index', index)


if __name__ == '_main_':
    app.run()