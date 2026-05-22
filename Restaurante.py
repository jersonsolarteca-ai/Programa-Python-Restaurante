"Programa: Gestor de precios de menú"

# Matriz de productos: [Nombre, Categoría, Precio base]
menu = [
    ["Hamburguesa", "Comida Rápida", 35000],
    ["Pizza Familiar", "Comida Rápida", 42000],
    ["Ensalada", "Comida Saludable", 18000],
    ["Gaseosa", "Bebida", 6000],
    ["Jugo Natural", "Bebida", 12000],
    ["Perro Caliente", "Comida Rápida", 28000]
]


def calcular_precio_final(producto, categoria_objetivo, umbral):
    """Calcula el precio final para un producto.

    Parámetros:
    - producto: lista con [nombre, categoría, precio]
    - categoria_objetivo: categoría que opta a promoción (str)
    - umbral: precio mínimo para aplicar el descuento (numérico)

    Retorna una tupla (precio_final, descuento_aplicado)
    """
    nombre, categoria, precio = producto

    # Inicializamos descuento en 0
    descuento = 0

    # Verificar descuento
    if isinstance(categoria, str) and categoria.lower() == categoria_objetivo.lower() and precio > umbral:
        descuento = precio * 0.15  # 15% de descuento

    precio_final = precio - descuento
    return precio_final, descuento




def mostrar_menu(menu, categoria_objetivo, umbral):
    """Imprime de forma ordenada la información de cada producto."""
    print("===============================================")
    print("           MENÚ DEL RESTAURANTE")
    print("===============================================")

    # Recorremos cada producto con un ciclo for
    for producto in menu:
        nombre, categoria, precio = producto

        precio_final, descuento = calcular_precio_final(producto, categoria_objetivo, umbral)

        print(f"Producto: {nombre}")
        print(f"Categoría: {categoria}")
        print(f"Precio base: ${precio}")


        # Mostramos si hubo descuento o no
        if descuento > 0:
            print(f"Descuento aplicado: 15% (-${descuento})")
        else:
            print("Sin promoción")

        print(f"Precio final: ${precio_final}")
        print("-----------------------------------------------")


if __name__ == "__main__":
    # Parámetros de la promoción según requisitos
    categoria_objetivo = "Comida Rápida"
    umbral = 30000

    # Ejecutamos la visualización del menú
    mostrar_menu(menu, categoria_objetivo, umbral)
