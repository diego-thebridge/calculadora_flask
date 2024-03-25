# app.py
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages

import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///servicios.db'
db = SQLAlchemy(app)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', '1234')


# Modelo de la base de datos para almacenar la configuración de los servicios
class Servicio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    options = db.Column(db.String(120), nullable=False)
    total = db.Column(db.Float, nullable=False)

'''@app.before_first_request
def create_tables():
    db.create_all() ''' 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        services = ','.join(request.form.getlist('service'))
        total = request.form['total']
        
        # Crear una nueva entrada en la base de datos
        new_service = Servicio(username=username, options=services, total=float(total))
        db.session.add(new_service)
        db.session.commit()

        flash('Datos guardados con éxito!')
        return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/confirmation')
def confirmation():
    return 'Datos guardados con éxito!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)