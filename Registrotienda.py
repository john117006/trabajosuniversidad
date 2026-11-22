productos =[]
productos.append(str(input("Ingrese el nombre del producto (FIN para terminar): ")))
producto = str(productos[len(productos)- 1])
prodictosregistrados = 0
productosConDescuentos = 0
totalCompras = 0
totalpagado = 0
valoracc = []
i = 0
while (producto != "fin"):
    cantidad = int(input("ingrese la cantidad: "))
    precio = int(input("ingrese el precio unitario: "))
    prodictosregistrados +=1
    totalProductos = cantidad * precio
    descuento = 0
    if (totalProductos >=100000):
        descuento = totalProductos *0.10
        productosConDescuentos +=1
    elif (totalProductos >=50000):
        descuento = totalProductos *0.05
        productosConDescuentos +=1
    valorfinal = totalProductos - descuento
    valoracc.append(valorfinal)
    print("producto: " +str(producto))
    print("Valor original: $" +str(totalProductos))
    print("Descuento: " +str(descuento))
    print("Valor a pagar: " +str(valorfinal))
    totalCompras += totalProductos
    totalpagado += valorfinal
    productos.append(str(input("Ingrese el nombre del producto (FIN para terminar): ")))
    producto = str(productos[len(productos)- 1])
print("RESUMEN DE LA COMPRA")
print("Productos registrados: "+ str(prodictosregistrados))
for i in range (len(productos)-1):
    print ("Producto: "+ str(productos[i]))
    print ("Valor: " + str(valoracc[i]) )
print("Productos con descuento: "+ str(productosConDescuentos))
print("Valor original de las compras: $"+ str(totalCompras))
print("Valor final a pagar: $"+ str(totalpagado))