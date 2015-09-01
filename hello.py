from flask import Flask, render_template, session, redirect, url_for
from flask import request
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import PasswordField, RadioField, SelectField, StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'KnIp3#pPx%2'
dnsnames=[('stocks_primary','stocks_primary'),('bonds_primary','bonds_primary')]
valid_aliases={}
valid_aliases['stocks_primary']=[('ny-stockdb-001','ny-stockdb-001'),('ny-stockdb-002','ny-stockdb-002'),('tx-stockdb-401','tx-stockdb-401')]
valid_aliases['bonds_primary']=[('ny-bonddb-001','ny-bonddb-001'),('ny-bonddb-002','ny-bonddb-002'),('tx-bonddb-401','tx-bonddb-401')]

class LoginForm(Form):
    name = StringField('User Name', validators=[Required()])
    passwd = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Login')

class DnsHostForm(Form):
    dnsname = SelectField('Host Name',choices=dnsnames)
    change = SubmitField('Change')

class DnsAliasForm(Form):
    alias = RadioField('Alias Name')
    change = SubmitField('Change')

def validate_password(name, passwd):
    if (name == "test") and (passwd == "test"):
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

@app.route('/dnshosts', methods=['GET', 'POST'])
def dnshosts():
    dnsname = None
    form = DnsHostForm()
    if form.validate_on_submit():
        session['dnsname'] = form.dnsname.data
        return redirect(url_for('dnsalias'))
    else:
        return render_template('dnshost.html', form=form, dnsname=dnsname)

@app.route('/dnsalias')
def dnsalias():
    dnsalias = None
    dnsname=session.get('dnsname')
    print "dnsname = ", dnsname
    print valid_aliases[dnsname]
    form = DnsAliasForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    else:
        return render_template('dnsalias.html', form=form, dnsname=dnsname, alias=valid_aliases[dnsname])

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
