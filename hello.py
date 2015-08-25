from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>your browser is: %s</p>' % user_agent


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
