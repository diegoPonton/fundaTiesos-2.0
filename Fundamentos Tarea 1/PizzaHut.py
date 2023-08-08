precios_ingredientes = {
    "pepperoni": 2.50,
    "jamón": 2.00,
    "pimientos": 1.50,
    "cebolla": 1.00,
    "aceitunas": 1.00,
    "tomate": 1.00,
    "extra_queso": 2.00
}

# Función para calcular el precio total del pedido


def calcular_precio_pedido(ingredientes):
    total = 0
    for ingrediente in ingredientes:
        if ingrediente in precios_ingredientes:
            total += precios_ingredientes[ingrediente]
    return total


# Solicitar al usuario los ingredientes del pedido
print("¡Bienvenido a Pizza Hut!")
print("Por favor, elige los ingredientes para tu pizza.")
print("Ingresa los ingredientes uno por uno y presiona Enter para agregarlos.")
print("Cuando hayas terminado, escribe 'listo'.")

ingredientes_pedido = []
while True:
    ingrediente = input("Ingrediente: ")
    if ingrediente.lower() == "listo":
        break
    ingredientes_pedido.append(ingrediente)

# Calcular el precio del pedido
precio_total = calcular_precio_pedido(ingredientes_pedido)

# Mostrar el resumen del pedido
print("Resumen de tu pedido:")
print("Ingredientes:")
for ingrediente in ingredientes_pedido:
    print("- " + ingrediente)
print("Precio total: $", precio_total)
