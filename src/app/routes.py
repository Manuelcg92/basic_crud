from flask import render_template,url_for,redirect, request
from . import app, db
from app.models import users, register

#Rutas de la aplicación
@app.route('/')
def home():
    data = db.session.query(register).all()
    return render_template('index.html', data=data)
    
# Ruta para guardar datos en la base de datos
@app.route('/user', methods=["POST"])
def add_register():
    temperatura = request.form['temperatura']
    estacion = request.form['estacion']
    fecha = request.form['fecha']
    
    if temperatura and estacion and fecha:
        new_register = register(temperatura=temperatura, estacion=estacion, fecha=fecha)
        db.session.add(new_register)
        db.session.commit()
    
    return redirect(url_for('home'))

# Ruta para eliminar datos
@app.route('/delete/<int:id>')
def delete(id):
    register_to_delete = db.session.query(register).get(id)
    if register_to_delete is None:
        return "Registro no encontrado", 404
    else:
        db.session.delete(register_to_delete)
        db.session.commit()
        return redirect(url_for('home'))

# Ruta para editar datos
@app.route('/edit/<int:id>', methods=["POST"])
def edit(id):
    register_to_edit = db.session.query(register).get(id)
    if register_to_edit is None:
        return "Registro no encontrado", 404
      
    temperatura = request.form['temperatura']
    estacion = request.form['estacion']
    fecha = request.form['fecha']
    
    if temperatura and estacion and fecha:
        register_to_edit.temperatura = temperatura
        register_to_edit.estacion = estacion
        register_to_edit.fecha = fecha
        
        db.session.commit()
    
    return redirect(url_for('home'))

# Ruta para registro de usuarios
@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username and password:
            new_user = users(usuario=username, contraseña=password)
            db.session.add(new_user)
            db.session.commit()
            
            return redirect(url_for('login'))  # Redirigir al usuario al endpoint 'login'

        else:
            # Introducir mensaje de error
            return render_template('signup.html')
    
    return render_template('signup.html')

# Ruta para login de usuarios
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = db.session.query(users).filter_by(usuario=username, contraseña=password).first()

        if user:
            return redirect(url_for('home'))
        else:
            return render_template('login.html')
    
    return render_template('login.html') 