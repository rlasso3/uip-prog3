import MySQLdb

# Establecemos la conexión con la base de datos
bd = MySQLdb.connect("localhost","usuarioprueba","prueba123","prueba_db" )

# Preparamos el cursor que nos va a ayudar a realizar las operaciones con la base de datos
cursor = bd.cursor()

# Preparamos el query SQL para obtener todos los empleados de la BD
sql = "SELECT * FROM EMPLEADO"
try:
   # Ejecutamos el comando
   cursor.execute(sql)
   # Obtenemos todos los registros en una lista de listas
   resultados = cursor.fetchall()
   for registro in resultados:
      nombre = registro[0]
      apellido = registro[1]
      edad = registro[2]
      sexo = registro[3]
      salario = registro[4]
      # Imprimimos los resultados obtenidos
      print "nombre=%s, apellido=%s, edad=%d, sexo=%s, salario=%d" % (nombre, apellido, edad, sexo, salario)
except:
   print "Error: No se pudo obtener la data"

# Nos desconectamos de la base de datos
bd.close()