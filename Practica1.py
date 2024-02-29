class Producto:
    def __init__(self, codigo, nombre, descripcion, precio_unitario):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario

class Cliente:
    def __init__(self, nombre, correo, nit):
        self.nombre = nombre
        self.correo = correo
        self.nit = nit

class Compra:
    def __init__(self, cliente, productos_comprados):
        self.cliente = cliente
        self.productos_comprados = productos_comprados
        self.id = None
        self.costo_total = 0
        self.impuesto = 0

nombre_estudiante = "Rogelio Esteban Velasquez Castillo"
carnet_estudiante = "202200387"

productos = []
clientes = []
compras = []

def registrar_producto():
    while True:
        print("Registro de Producto")
        codigo = input("Ingrese el código del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripción del producto: ")
        precio_unitario = float(input("Ingrese el precio unitario del producto: "))

        nuevo_producto = Producto(codigo, nombre, descripcion, precio_unitario)
        productos.append(nuevo_producto)

        print(f"Producto '{nombre}' registrado con éxito.")

        respuesta = input("¿Desea agregar otro producto? (s/n): ")
        if respuesta.lower() != 's':
            break

def registrar_cliente():
    while True:
        print("Registro de Cliente")
        nombre = input("Ingrese el nombre del cliente: ")
        correo = input("Ingrese el correo electrónico del cliente: ")
        nit = input("Ingrese el NIT del cliente: ")

        nuevo_cliente = Cliente(nombre, correo, nit)
        clientes.append(nuevo_cliente)

        print(f"Cliente '{nombre}' registrado con éxito.")

        respuesta = input("¿Desea registrar otro cliente? (s/n): ")
        if respuesta.lower() != 's':
            break

def realizar_compra():
    nit_cliente = input("Ingrese el NIT del cliente que está realizando la compra: ")

    cliente_actual = None
    for cliente in clientes:
        if cliente.nit == nit_cliente:
            cliente_actual = cliente
            break

    if cliente_actual is None:
        print("Cliente no encontrado. Volviendo al menú principal.")
        return

    productos_comprados = []

    while True:
        print("\nSubmenú de Compra:")
        print("1. Agregar Producto")
        print("2. Terminar Compra y Generar Factura")

        opcion_compra = input("Seleccione una opción (1-2): ")

        if opcion_compra == '1':
            codigo_producto = input("Ingrese el código del producto que se va a comprar: ")

            producto_encontrado = None
            for producto in productos:
                if producto.codigo == codigo_producto:
                    producto_encontrado = producto
                    break

            if producto_encontrado is not None:
                productos_comprados.append(producto_encontrado)
                print(f"Producto '{producto_encontrado.nombre}' agregado al carrito.")
            else:
                print("Producto no encontrado. Por favor, ingrese un código válido.")

        elif opcion_compra == '2':
            if not productos_comprados:
                print("No hay productos en el carrito. Volviendo al menú principal.")
                break

            costo_total = sum(producto.precio_unitario for producto in productos_comprados)
            impuesto = costo_total * 0.12

            nueva_compra = Compra(cliente_actual, productos_comprados)
            nueva_compra.id = len(compras) + 1
            nueva_compra.costo_total = costo_total
            nueva_compra.impuesto = impuesto

            compras.append(nueva_compra)

            print("Compra realizada y factura generada con éxito.")
            print(f"Costo total: Q{costo_total:.2f}")
            print(f"Impuesto: Q{impuesto:.2f}")

            break

def reporte_compra():
    id_compra = int(input("Ingrese el ID de la compra que desea visualizar: "))

    compra_encontrada = None
    for compra in compras:
        if compra.id == id_compra:
            compra_encontrada = compra
            break

    if compra_encontrada is not None:
        print("\nDetalles de la Compra:")
        print(f"ID de Compra: {compra_encontrada.id}")
        print(f"Cliente: {compra_encontrada.cliente.nombre}")
        print("Productos Comprados:")
        for producto in compra_encontrada.productos_comprados:
            print(f"  - {producto.nombre}: Q{producto.precio_unitario:.2f}")
        print(f"Costo Total: Q{compra_encontrada.costo_total:.2f}")
        print(f"Impuesto: Q{compra_encontrada.impuesto:.2f}")
    else:
        print("Compra no encontrada. Verifique el ID e intente nuevamente.")

while True:
    print("\nMenú Principal:")
    print("1. Registrar Producto")
    print("2. Registrar Cliente")
    print("3. Realizar Compra")
    print("4. Reporte de Compra")
    print("5. Datos del Estudiante")
    print("6. Salir")

    opcion = input("Seleccione una opción (1-6): ")

    if opcion == '1':
        registrar_producto()
    elif opcion == '2':
        registrar_cliente()
    elif opcion == '3':
        realizar_compra()
    elif opcion == '4':
        reporte_compra()
    elif opcion == '5':
        print("\nDatos del Estudiante:")
        print(f"Nombre: {nombre_estudiante}")
        print(f"Carnet: {carnet_estudiante}")
    elif opcion == '6':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 6.")