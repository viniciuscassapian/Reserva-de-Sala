from flask import Flask
from database import db
from reserva_route import routes
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(routes)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(port=5001, debug=True)
