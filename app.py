from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from apiv1 import blueprint as api1

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.register_blueprint(api1)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
