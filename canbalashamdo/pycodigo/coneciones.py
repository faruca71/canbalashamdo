# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 23:04:28 2020
@author: fabio
Aqui defino una clase con todos los metos requeridos por la pagina
"""
from __future__ import print_function
import mysql.connector
from autenticar import auth

class metodos:
	def __init__(self):
		self.DB_NAME = "canbalashamdo"
		self.USERS = ['paraescribir','paraleer']
		self.CLAVES = ['rr&Hijos*123','Niko&Isaac&Lori']

	def dataEnter(self,sqlCode):
		configRoot = {
			'user': self.USERS[0],
			'password': self.CLAVES[0],
			'host': 'localhost',
			'database': self.DB_NAME
			}
		conn = mysql.connector.connect(**configRoot)
		mycur = conn.cursor()
		try:
			mycur.execute(sqlCode)
			conn.commit()
		except mysql.connector.Error as err:
			conn.rollback()
			return "Se ha presentado el Error = {}".format(err.msg)
		mycur.close()
		conn.close()
		return True

	def dataConsult(self,sqlCode):
		configRoot = {
			'user': self.USERS[0],
			'password': self.CLAVES[0],
			'host': '',
			'database': self.DB_NAME
			}
		conn = mysql.connector.connect(**configRoot)
		mycur = conn.cursor(dictionary=True)
		try:
			mycur.execute(sqlCode)
		except mysql.connector.Error as err:
			return "Se ha presentado el Error = {}".format(err.msg)
		result = []
		for row in mycur.fetchall():
			result.append(row)
		mycur.close()
		conn.close()
		return result

	def consultaUser(self,datLogar):
		sqlCode = ("SELECT id, nombre, email, telefono, clave FROM clientes WHERE "
							"email= '%(correo)s' OR telefono= '%(correo)s'")
		result = self.dataConsult(sqlCode % datLogar)
		valor = "Fallo coneccion a DB"
		if(result):
			usuario = auth(result)
			result = usuario.comparaClaves(datLogar['clave'])
			if(result):
				return result
			else:
				return ["El usuario o la clave NO concuerda"]
		else:
			return ["El usuario o la clave NO concuerda"]

	def consultarApodo(self,dato):
		sqlCode = ("SELECT apodo FROM clientes WHERE apodo = '%s'" % dato)
		result = self.dataConsult(sqlCode)
		if(result):
			Rta = False
		else:
			Rta = True
		return Rta

	def registrarDatos(self, userData):
		slqExp = ("INSERT INTO expertcies "
			"(profesion,exp_en,exp_tmp,fecha_hora) VALUES ('%(profesion)s','%(exp_en)s','%(exp_tmp)s',NOW())")

		sqlCode = ("INSERT INTO canbalashamdo.clientes "
			" (nombre,email,telefono,apodo,clave,id_num,genero,direccion,taxador,abeas_data,fecha_hora) VALUES "
			" ('%(nombre)s','%(email)s','%(telefono)s','%(apodo)s','%(clave)s','%(id_num)s','%(genero)s',"
			"'%(direccion)s','%(taxador)s','%(abeas_data)s',NOW())")

		Rta = self.consultarApodo(userData['apodo'])
		if(Rta):
			reg = auth(None)
			userData['clave'] = reg.codificar(userData['clave'])
			result = self.dataEnter(sqlCode % userData)
			if(userData['taxador'] == 'S'):
				result = self.dataEnter(slqExp % userData)
		else:
			return False
		return True

	def registrarProd(self):
		sqlCode = ("INSERT INTO productos "
			"(objeto,descripcion,cambio_por,localizacion,valor_est_prop,valor_est_tax,tax_responde,activo,fecha_hora,img_locate) VALUES "
			"('%(objeto)s','%(descripcion)s','%(cambio_por)s','%(localizacion)s','%(valor_est_prop)s','%(valor_est_tax)s',"
			"'%(tax_responde)s','%(activo)s',NOW(),'%(img_locate)s')")
