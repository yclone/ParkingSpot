import sys
from pathlib import Path

# Add the parent directory to Python path
app_dir = str(Path(__file__).parent.parent)
sys.path.insert(0, app_dir)

from flask import Flask, render_template, session, redirect
from src.models.user import db
from src.routes.user_routes import user_bp, create_initial_user
from src.routes.parking_routes import parking_bp
import os

app = Flask(__name__, 
           instance_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance'),
           instance_relative_config=True)

# Ensure the instance folder exists
os.makedirs(app.instance_path, exist_ok=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'parking.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key'  # Adicionar chave secreta para sessão

db.init_app(app)

app.register_blueprint(user_bp)
app.register_blueprint(parking_bp)

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
        print("Database tables created successfully!")
    app.run(debug=True)
