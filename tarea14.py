def calcular_descuento(precio,descuento):
    precio_descuento = precio - (precio * descuento/100)
# valor que se regresa es el precio de descuento
    return precio_descuento
#Crear una variable donde se guardo el valor
total = 0
#Creamos la variable donde se ingresa el valor del producto
producto_precio= input("Ingrese el precio del producto")
# valor del producto esta vacio
if producto_precio == "":
# muestra el mensaje que debe ingresar un valor numèrico
    print("Ingresar valores numericos")
# Se ingresa un porcentaje de descuento
else:
    producto_precio1 =input("Ingresar el porcentaje del descuento")
    if producto_precio1 == "":
        print("ingresar valores numericos")
# calculamos el precio final y lo mostramos
    else:
        total = calcular_descuento(float(producto_precio), float(producto_precio1))
#Imprimir el valor total
print(total)
