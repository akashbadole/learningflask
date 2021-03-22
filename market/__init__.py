from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from markupsafe import escape
# app = Flask(__name__)
app = Flask(__name__, template_folder='../templates') 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

# database
db = SQLAlchemy(app)

from market import routes

# if __name__ == "__main__":
#     app.run(debug=True)