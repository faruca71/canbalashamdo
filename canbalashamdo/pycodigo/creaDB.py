"""
  creado: Lunes 03 de Agosto de 2020
  Autor: Fabio Rueda Calier
  Empresa: Rueda Rodriguez e Hijos S.A.S
  Codigo python para crear base de datos, tablas, usuaios y permisos de canbalashamdo
"""

from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode

class crear:
  def __init__(self):
    configRoot = {
      'user': 'root',
      'password': 'SanGil*91073$',
      'host': 'localhost',
      'database': 'mysql'
      }
    self.DB_NAME = "canbalashamdo"
    conn = mysql.connector.connect(**configRoot)
    self.crear_database(conn)
    self.crear_tablas(conn)
    self.crear_usuarios(conn)
    conn.close()

  def crear_tablas(self,conn):
    TABLES = {}
    TABLES['clientes'] = (
      "CREATE TABLE clientes ("
      "  ID int(8) NOT NULL AUTO_INCREMENT,"
      "  nombre VARCHAR(255) NOT NULL,"
      "  email VARCHAR(100) NOT NULL,"
      "  telefono VARCHAR(50) NOT NULL,"
      "  apodo VARCHAR(255) NOT NULL,"
      "  clave VARCHAR(255) NOT NULL,"
      "  cumpleano DATE NOT NULL," ## espacio no existe en la tabla
      "  id_num VARCHAR(50) NOT NULL,"
      "  genero enum('M','F','N') NOT NULL,"
      "  direccion VARCHAR(250) NOT NULL,"
      "  taxador enum('S','N'),"
      "  fecha_hora DATETIME NOT NULL,"
      "  abeas_data enum('S','N'),"
      "  PRIMARY KEY (ID), UNIQUE KEY apodo (apodo)"
      ") ENGINE=InnoDB")

    TABLES['productos'] = (
      "CREATE TABLE productos ("
      "  ID int(10) NOT NULL AUTO_INCREMENT,"
      "  apodo_vendedor VARCHAR(250) NOT NULL,"
      "  objeto VARCHAR(250) NOT NULL,"  ## Este espacio no existe en la tabla
      "  descripcion VARCHAR(1000) NOT NULL,"
      "  cambio_por VARCHAR(1000) NOT NULL,"
      "  localizacion VARCHAR(250) NOT NULL,"
      "  valor_est_prop DECIMAL NOT NULL,"
      "  valor_est_tax DECIMAL NOT NULL,"
      "  tax_responde VARCHAR(255) NOT NULL,"
      "  activo enum('S','N'),"
      "  fecha_hora DATETIME NOT NULL,"
      "  img_locate VARCHAR(512) NOT NULL,"
      "  PRIMARY KEY (ID),"
      "  INDEX (apodo_vendedor),"
      "  FOREIGN KEY (apodo_vendedor) "
      "  REFERENCES clientes(apodo) ON UPDATE CASCADE ON DELETE RESTRICT"
      ") ENGINE=InnoDB")

    TABLES['expertcies'] = (
      "CREATE TABLE expertcies ("
      "  ID int(10) NOT NULL AUTO_INCREMENT,"
      "  apodo_tax VARCHAR(250) NOT NULL,"
      "  profesion VARCHAR(250) NOT NULL,"
      "  exp_en VARCHAR(250) NOT NULL,"
      "  exp_tmp INT(2) NOT NULL,"
      "  fecha_hora DATETIME NOT NULL,"
      "  PRIMARY KEY (ID),"
      "  INDEX (apodo_tax),"
      "  FOREIGN KEY (apodo_tax) "
      "  REFERENCES clientes(apodo) ON UPDATE CASCADE ON DELETE RESTRICT"
      ") ENGINE=InnoDB")
    
    mycur = conn.cursor()
    mycur.execute("USE {}".format(self.DB_NAME))
    for table_name in TABLES:
      table_description = TABLES[table_name]
      try:
        print("Creating table {}: ".format(table_name), end='')
        mycur.execute(table_description)
      except mysql.connector.Error as err:
        if(err.errno == errorcode.ER_TABLE_EXISTS_ERROR):
          print("already exists.")
        else:
          print(err.msg)
      else:
        print("OK")
    mycur.close()
    return True

  def crear_database(self,conn):
    mycur = conn.cursor()
    try:
      mycur.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(self.DB_NAME))
    except mysql.connector.Error as err:
      print("Ha Fallado la creacion de : {}".format(err))
      exit(1)
    mycur.close()
    return True

  def crear_usuarios(self,conn):
    DB_NAME = self.DB_NAME
    USER = ['adminCambalache']
    CLAVE = ['Niko&Isaac&Lori']
    USUARIO = ("CREATE USER '{0}'@'localhost' IDENTIFIED BY '{1}'".format(USER,CLAVE))
    PERMISO = ("GRANT SELECT, INSERT, UPDATE, DELETE ON {0}.* TO '{1}'@'localhost' WITH GRANT OPTION".format(DB_NAME,USER))

    mycur = conn.cursor()
    try:
      print("Creando el ususario: {} ".format(USER), end='')
      mycur.execute(USUARIO)
      mycur.execute("FLUSH PRIVILEGES")
      mycur.execute(PERMISO)
      mycur.execute("FLUSH PRIVILEGES")
    except mysql.connector.Error as err:
      if(err.errno):
        print("Eror con: {0}, de tipo = {1}".format(USER, err.errno))
      else:
        print(err.msg)
    else:
      print("OK")
    mycur.close()
    return True

if(__name__ =="__main__"):
  creando = crear()