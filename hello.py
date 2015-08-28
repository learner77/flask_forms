from flask import Flask, render_template, session, redirect, url_for
from flask import request
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import PasswordField, RadioField, SelectField, StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'KnIp3#pPx%2'
dnsnames=[('hotel_primary','hotel_primary'),('air_primary','air_primary')]
valid_aliases=[('ny-db-001','ny-db-001'),('ny-db-002','ny-db-002'),('ash1-db-401','ash1-db-401')]

class LoginForm(Form):
    name = StringField('User Name', validators=[Required()])
    passwd = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Login')

class DnsHostForm(Form):
    dnsname = SelectField('Host Name',choices=dnsnames)
    change = SubmitField('Change')

class DnsAliasForm(Form):
    alias = RadioField('Alias Name',choices=valid_aliases)
    change = SubmitField('Change')

def validate_password(name, passwd):
    if (name == "test") and (passwd == "winner"):
        return True
    else:
        return False
    

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    passwd = None
    form = LoginForm()
    if form.validate_on_submit():
        if validate_password(form.name.data, form.passwd.data):
            session['name'] = form.name.data
            return redirect(url_for('dnshosts'))
    return render_template('index.html', form=form, name=session.get('name'), passwd=passwd)

@app.route('/dnshosts')
def dnshosts():
    dnsname = None
    form = DnsHostForm()
    return render_template('dnshost.html', form=form, dnsname=dnsname)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
