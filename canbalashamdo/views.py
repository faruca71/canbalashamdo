from canbalashamdo import app, login_manager
import pycodigo as cte
from flask import render_template, url_for, request, redirect, flash
import random
import os

@app.route('/')
def index():
	usr=''
	return render_template('inicio.html',usr=usr)

@app.route('/detallando') 
def detalleArticulo():
	ruta = "canbalashamdo/static/img/frc1394/"
	hists = ["../static/img/frc1394/"+F for F in os.listdir(ruta)]
	print(hists)
	A = 6*[0]
	return render_template('detallando.html',A=A, rutas=hists)

@login_manager.user_loader
def load_user(log):
	mtd = cte.metodos()
	usr = mtd.consultaUser(log)
	return usr

@app.route('/login', methods=['GET', 'POST'])
def hacerLogin():
	nom=''
	log = cte.logar()
	if(request.method == 'POST'):
		for col in log:
			log[col] = request.form.get(col)
		usr = load_user(log)
		if(len(usr) > 1):
			nom = usr[-1].split(' ')[0]
			render_template('inicio.html',usr=nom)
		else:
			nom = usr[0]
	return render_template('login.html',usr=nom)

@app.route('/registro', methods=['GET', 'POST'])
def hacerRegistro():
	userData = cte.clients()
	msg = ""
	usr=''
	if(request.method == 'POST'):
		for col in userData.keys():
			if(request.form.get(col)):
				userData[col] = request.form.get(col)
		registrar = cte.metodos()
		rta = registrar.registrarDatos(userData)
		if(rta):
			return redirect(url_for('index'))
		else:
			msg = " (El Apodo o Alias, {apodo} ya esta siendo usado)".format(**userData)
	return render_template('registro.html',usr=usr,msg=msg)

@app.route('/registro-productos', methods=['GET', 'POST'])
def haceRegProd():
	usr=''
	return render_template('regProd.html',usr)