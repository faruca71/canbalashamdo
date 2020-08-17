# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:04:28 2020
@author: fabio
autenticacion de cuentas y traer informacion de la base de cuentas
"""

# from flask_login import UserMixin,login_user,logout_user,login_required,current_user
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class auth(UserMixin):
	def __init__(self, usuario):
		if(usuario != None):
			if(usuario[0]['nombre'] == "Anonimo"):
				self.id = datetime.now().microsecond
				self.active = True
			else:
				self.name = usuario[0]['nombre']
				self.id = usuario[0]['id']
				self.log = usuario[0]['clave']
				self.active = True
		else:
			print("Exito")

	def is_active(self):
		return self.active

	def codificar(self,clave):
		codigo = generate_password_hash(clave,method='pbkdf2:sha1', salt_length=64)
		return codigo

	def comparaClaves(self,clave):
		if check_password_hash(self.log,clave):
			return [True, self.id, self.name]
		return False

