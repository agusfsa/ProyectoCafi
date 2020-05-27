from datetime import date
import pymysql

def conectarDB():
        conexion=pymysql.Connection(host="bp65hmalfd442ftirlu9-mysql.services.clever-cloud.com",user="uhzdmgqgoa7jdrjb",password="07wtqmCWlNJAmfG9U9nz",db="bp65hmalfd442ftirlu9")
        return conexion

def fechaActual():
        today = date.today()
        dia = str(today.day)
        mes = str(today.month)
        año = str(today.year)
        fecha = año+"-"+mes+"-"+dia
        return fecha

def insertarCliente(nombre,apellido,dni,domicilio,telefono,nacimiento,email,contrasena):
        conexion=conectarDB()
        cursor=conexion.cursor()
        sqlInsertar = "insert into usuarios(nombre,apellido,dni,domicilio,telefono,nacimiento,email,contrasena)values(%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sqlInsertar,(nombre,apellido,dni,domicilio,telefono,nacimiento,email,contrasena))
        conexion.commit()
        cursor.close()
        conexion.close()
