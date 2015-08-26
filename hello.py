from flask import Flask, render_template
from flask import request
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import Required


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'KnIp3#pPx%2'

class LoginForm(Form):
    name = StringField('User Name', validators=[Required()])
    passwd = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Login')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    passwd = None
    form = LoginForm()
    return render_template('index.html', form=form, name=name, passwd=passwd)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
