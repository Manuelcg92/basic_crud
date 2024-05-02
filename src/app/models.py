from . import db
from sqlalchemy.ext.hybrid import hybrid_property

import re



class users(db.Model):
    iduser = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(20), unique=True, nullable=False)
    _contraseña = db.Column('password', db.String(255), nullable=False)
    
    @hybrid_property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, plaintext):
        if not re.match(r'^[a-zA-Z0-9]+$', plaintext):
            raise ValueError('La contraseña debe ser alfanumerica')
        self._password = plaintext
        
    def __repr__(self):
        return f'<users {self.usuario}>'
    
class register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperatura = db.Column(db.Float, unique=False, nullable=False)
    estacion = db.Column(db.String(20), unique=False, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
        return f"<register(id={self.id}, temperatura={self.temperatura}, estacion='{self.estacion}', fecha='{self.fecha}')>"