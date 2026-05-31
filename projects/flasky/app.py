from flask import Flask, make_response, render_template,redirect,url_for,session,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

class NameForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    submit = SubmitField('submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'my very secret flask app key'

Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index()-> str:
    nameForm = NameForm()

    if nameForm.validate_on_submit():
        if nameForm.name.data:
            flash('Name change successful!', 'success')
            session['name'] = nameForm.name.data
            
            return redirect(url_for('index'))

    sessionName = session.get('name')
    greetName = sessionName if sessionName else 'Stranger'

    return make_response(render_template('form.html', form=nameForm, name=greetName), 200)
