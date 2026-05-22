# Matriz del menú
menu = [
    ["Hamburguesa", "Comida", 25000],
    ["Pizza", "Comida", 30000],
    ["Gaseosa", "Bebida", 5000],
    ["Jugo Natural", "Bebida", 8000],
    ["Helado", "Postre", 12000],
    ["Pasta", "Comida", 28000]
]

# Función para calcular el precio final
def calcular_precio_final(categoria, precio):

    if categoria == "Comida" and precio > 20000:
        descuento = precio * 0.15
        precio_final = precio - descuento

    else:
        precio_final = precio

    return precio_final


print("==========================================")
print("    MENÚ DEL RESTAURANTE - PROMOCIONES")
print("==========================================")

# Recorrer la matriz
for producto in menu:

    nombre = producto[0]
    categoria = producto[1]
    precio = producto[2]

    precio_final = calcular_precio_final(categoria, precio)

    print("Producto:", nombre)
    print("Categoría:", categoria)
    print("Precio Base:", precio)
    print("Precio Final:", precio_final)
    print("--------------------------------------")