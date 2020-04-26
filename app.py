from flask import Flask
from config import Config
from werkzeug.utils import cached_property
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from blueprint.api  import blueprint as api

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.register_blueprint(api, url_prefix='/api/1')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
