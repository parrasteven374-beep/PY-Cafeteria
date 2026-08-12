menu = [
    {"nombre": "cafe", "categoria": "bebida", "precio": 3000, "stock": 10, "vendidos": 0},
    {"nombre": "jugo", "categoria": "bebida", "precio": 4000, "stock": 8, "vendidos": 0},
    {"nombre": "hamburguesa", "categoria": "plato fuerte", "precio": 12000, "stock": 5, "vendidos": 0},
    {"nombre": "pizza", "categoria": "plato fuerte", "precio": 15000, "stock": 6, "vendidos": 0},
    {"nombre": "torta", "categoria": "postre", "precio": 5000, "stock": 4, "vendidos": 0},
    {"nombre": "galleta", "categoria": "postre", "precio": 2000, "stock": 7, "vendidos": 0},
]

def mostrar_menu():
    print("\n--- MENÚ DISPONIBLE ---")
    for p in menu:
        print(p["nombre"], "|", p["categoria"], "| $", p["precio"], "| Stock:", p["stock"])

def buscar_producto(nombre):
    nombre = nombre.lower().strip()
    for p in menu:
        if p["nombre"] == nombre:
            return p
    return None

def hacer_pedido():
    pedido = []
    total = 0
    contador = 0

    while contador < 5:
        print("\nProducto #", contador + 1)
        nombre = input("¿Qué producto deseas? (escribe 'salir' para volver): ").lower()

        if nombre == "salir":
            break

        producto = buscar_producto(nombre)

        if producto is None: 
            print("Producto no existe")
            continue

        try:
            cantidad = int(input("¿Cantidad?: "))
            if cantidad <= 0:
                print("Cantidad inválida")
                continue
        except ValueError:
            print("Ingresa un número válido")
            continue

        if cantidad > producto["stock"]:
            print("Solo hay", producto["stock"], "disponibles")
            continue

        subtotal = cantidad * producto["precio"]
        total += subtotal

        producto["stock"] -= cantidad
        producto["vendidos"] += cantidad

        pedido.append({
            "nombre": producto["nombre"],
            "precio": producto["precio"],
            "cantidad": cantidad,
            "subtotal": subtotal
        })

        contador += 1

        if contador < 5:
            continuar = input("¿Quieres otro producto? (si/no): ").lower()
            if continuar != "si":
                break

    if len(pedido) == 0:
        print("Debes pedir al menos un producto")
        return 0

    print("\n=========== FACTURA ===========")
    print("Producto | Precio | Cantidad | Subtotal")
    for item in pedido:
        print(item["nombre"], "| $", item["precio"], "|", item["cantidad"], "| $", item["subtotal"])

    print("---------------------------------")
    print("TOTAL SIN DESCUENTO:", total)

    if total > 20000:
        descuento = total * 0.10
        total_final = total - descuento
        print("DESCUENTO (10%): -$", descuento)
        print("TOTAL A PAGAR:", total_final)
        print("=================================")
        return total_final
    else:
        print("TOTAL A PAGAR:", total)
        print("=================================")
        return total

def resumen_dia(dinero_total_caja):
    print("\n--- RESUMEN DEL DÍA ---")

    total_vendido = 0
    for p in menu:
        total_vendido += p["vendidos"]

    if total_vendido == 0:
        print("No se realizaron ventas hoy.")
    else:
        mas_vendido = menu[0]
        for p in menu:
            if p["vendidos"] > mas_vendido["vendidos"]:
                mas_vendido = p

        print("Producto más vendido:", mas_vendido["nombre"])
        print("Total recaudado:", dinero_total_caja)

    print("Inventario crítico (<3):")
    for p in menu:
        if p["stock"] < 3:
            print("-", p["nombre"], "Stock:", p["stock"])

total_dia = 0

while True:
    print("\n=== SISTEMA CENTRAL DE LA CAFETERÍA ===")
    usuario = input("¿Eres 'estudiante' o 'admin'? (o escribe 'apagar' para cerrar la caja): ").lower().strip()

    if usuario == "apagar":
        print("Apagando el sistema. ¡Buen trabajo hoy!")
        break

    elif usuario == "estudiante":
        while True:
            print("\n===== MENÚ ESTUDIANTE =====")
            print("1. Ver menú y comprar")
            print("2. Cambiar de usuario")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                mostrar_menu()
                dinero_de_esta_venta = hacer_pedido()
                total_dia += dinero_de_esta_venta 
            elif opcion == "2":
                print("Cerrando sesión de estudiante...")
                break
            else:
                print("Opción inválida")

    elif usuario == "admin":
        while True:
            print("\n===== ADMIN =====")
            print("1. Resumen diario")
            print("2. Cambiar de usuario")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                resumen_dia(total_dia)
            elif opcion == "2":
                print("Cerrando sesión de admin...")
                break
            else:
                print("Opción inválida")

    else:
        print("Usuario no reconocido. Por favor escribe 'estudiante' o 'admin'.")