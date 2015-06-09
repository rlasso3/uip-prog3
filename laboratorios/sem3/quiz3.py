

nombre = (input("Ingresar nombre: "))
vent1 = float(input("Ingresar venta para el primer mes: ")) 
vent2 = float(input("Ingresar venta para el segundo mes: "))   
vent3 = float(input("Ingresar venta para el tercer mes: "))

vent = vent1 + vent2 + vent3 
comision = vent * 0.125


print ("\nINFORME DE COMISINES")
  

print ("Vendedor \t Ventas \t Comision \n" )
print (nombre, "\t\t$", vent, "\t\t", comision )
