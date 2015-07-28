import socket
print ("Escaner de puertos by braulio23\n")

host = input("Indica el host : ")
numerouno = input("Primer numero del rango : ")
numerodos = input("Segundo numero del rango : ")
socket = socket.socket()
for puerto in range(int(numerouno),int(numerodos)):
    try:
        socket.connect((host,puerto))
        print ("Puerto "+str(puerto)+" abierto")
        socket.close()
 
    except :
        print ("Puerto "+str(puerto)+" cerrado.")

 
