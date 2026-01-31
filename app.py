import os
import yaml
from flask import Flask
from my_project.db import db

from my_project.route.car_class_route import class_bp
from my_project.route.review_route import review_bp
from my_project.route.car_brand_route import brand_bp
from my_project.route.client_route import client_bp
from my_project.route.car_model_route import model_bp
from my_project.route.driver_route import driver_bp
from my_project.route.car_route import car_bp
from my_project.route.order_route import order_bp
from my_project.route.status_route import status_bp
from my_project.route.payment_route import payment_bp
from my_project.route.procedure_route import procedure_bp

app = Flask(__name__)

config_path = os.path.join(os.path.dirname(__file__), 'config', 'app.yml')
with open(config_path, 'r') as f:
    config = yaml.safe_load(f)

db_cfg = config['database']
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{db_cfg['user']}:{db_cfg['password']}@"
    f"{db_cfg['host']}:{db_cfg['port']}/{db_cfg['schema']}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(brand_bp)
app.register_blueprint(client_bp)
app.register_blueprint(model_bp)
app.register_blueprint(driver_bp)
app.register_blueprint(car_bp)
app.register_blueprint(order_bp)
app.register_blueprint(class_bp)
app.register_blueprint(review_bp)
app.register_blueprint(status_bp)
app.register_blueprint(payment_bp)
app.register_blueprint(procedure_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)