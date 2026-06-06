from flask import Flask
from config import Config
from flask_bcrypt import Bcrypt
from models.employee import Employee
from models.user import db
from routes.auth import auth_bp
from routes.employee import employee_bp
import time

app = Flask(__name__)

app.config.from_object(Config)

bcrypt = Bcrypt(app)

db.init_app(app)
app.register_blueprint(auth_bp)
app.register_blueprint(employee_bp)

with app.app_context():
    for attempt in range(10):
        try:
            db.create_all()
            print("Database connected successfully!")
            break
        except Exception as e:
            print(f"Database not ready, retrying... ({attempt+1}/10)")
            time.sleep(5)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
