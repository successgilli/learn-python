from flask import Flask, make_response, render_template,redirect,url_for,session,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

class NameForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    submit = SubmitField('submit', render_kw={'class': 'btn btn-primary'})


app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'my very secret flask app key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'

Bootstrap(app)
db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), unique=True)
    users: Mapped[list['User']] = relationship(back_populates='roles')

    def __repr__(self):
        return 'Role {}'.format(self.name)

class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(64), unique=True)

    # role relationship
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey('roles.id'))
    roles: Mapped["Role"] = relationship(back_populates="users")


    def __repr__(self):
        return 'User {}'.format(self.username)

# expose imports to flask shell

@app.shell_context_processor
def shell_context():
    return dict(db=db, User=User, Role=Role)

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
