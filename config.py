from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://dbhotel3_taperideon:86f157c9c3807268c5a909dcd01d66a99ca6ebc2@5g9x2.h.filess.io:3305/dbhotel3_taperideon'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()