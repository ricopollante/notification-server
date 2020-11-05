from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from auth.token_auth import token_encode, token_verify
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:iam100%pureROOT@localhost:3306/cnmdb'
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

###MODELS
class SuperAdmin(db.Model):
    """Model for SuperAdmin accounts."""
    __tablename__ = 'superadmin'

    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(200),
                         nullable=False,
                         unique=False)
    password = db.Column(db.String(200),
                         primary_key=False,
                         unique=False,
                         nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

class User(db.Model):
    """Model for users."""
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(250),
                         nullable=False,
                         unique=False)
    notifications = db.relationship('Notifications', backref='users', lazy=True)
    def __init__(self, username):
        self.username = username

class App(db.Model):
    """Model for user apps."""
    __tablename__ = 'apps'

    id = db.Column(db.Integer,
                   primary_key=True)
    title = db.Column(db.String(100),
                         nullable=False,
                         unique=False)
    notifications = db.relationship('Notifications', backref='apps', lazy=True)

    def __init__(self, title):
        self.title = title

class Notifications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(80), unique=False, nullable=True)
    time = db.Column(db.String(80), unique=False, nullable=True)
    description = db.Column(db.String(80), unique=False, nullable=False)
    app_id = db.Column(db.Integer, db.ForeignKey('apps.id'), unique=False, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=False, nullable=True)

    def __init__(self, description, date, time,  app_id, user_id):
        self.description = description
        self.date = date
        self.time = time
        self.app_id = app_id
        self.user_id = user_id


###SCHEMA
class SuperAdminSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password')
superadmin_schema = SuperAdminSchema()
superadmin_all_schema = SuperAdminSchema(many=True)


class NotificationsSchema(ma.Schema):
    class Meta:
        fields = ('id','description','time', 'date', 'app_id', 'user_id')
notif_schema = NotificationsSchema()
notifs_all_schema = NotificationsSchema(many=True)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username')
user_schema = UserSchema()
users_all_schema = UserSchema(many=True)

class AppSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title')
app_schema = AppSchema()
apps_all_schema = AppSchema(many=True)

# ### VIEWS
@app.route('/notifications', methods=['POST'])
def dump_notifs():
        token = request.form['token']
        if token_verify(token) == "True":
            print("TRUE", file=sys.stdout)
            query_notif =  Notifications.query.all()
            dump_notif = notifs_all_schema.dump(query_notif)

        else:
            #print(error, file=sys.stdout)
            return("INVALID TOKEN")

        return jsonify(dump_notif)

# if __name__ == "__main__":
#     app.run(port=5005)