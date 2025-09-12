from flask import Flask, render_template, session, redirect
from models.user import db
from routes.user_routes import user_bp, create_initial_user
from routes.parking_routes import parking_bp
from routes.log_routes import log_bp
from flask_cors import CORS
import os
import logging

app = Flask(__name__, 
           instance_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance'),
           instance_relative_config=True)

# Ensure the instance folder exists
os.makedirs(app.instance_path, exist_ok=True)

# Configure logging
print(app.instance_path)
log_file = os.path.join(app.instance_path, 'app.log')
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s %(levelname)s: %(message)s')
file_handler = logging.FileHandler(log_file, encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
logging.getLogger().addHandler(file_handler)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'parking.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # Adicionar chave secreta para sessão

db.init_app(app)

# Adicionar suporte a CORS
CORS(app)

app.register_blueprint(user_bp)
app.register_blueprint(parking_bp)
app.register_blueprint(log_bp)

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template('index.html')

if __name__ == '__main__': 
    with app.app_context():
        db.drop_all()
        db.create_all()
        create_initial_user()  # Adicionar esta linha
        logging.info("Database tables created successfully!")
    app.run(debug=True)
