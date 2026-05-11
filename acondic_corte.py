# Datos ordenados por categoría
ventas = [
    {"producto": "Manzana", "categoria": "Fruta", "monto": 10},
    {"producto": "Pera", "categoria": "Fruta", "monto": 15},
    {"producto": "Lechuga", "categoria": "Verdura", "monto": 5},
    {"producto": "Tomate", "categoria": "Verdura", "monto": 8},
    {"producto": "Zanahoria", "categoria": "Verdura", "monto": 12},
]

def procesar_corte(datos):
    i = 0
    total_general = 0
    
    while i < len(datos):
        categoria_actual = datos[i]["categoria"]
        subtotal_categoria = 0
        print(f"--- Categoría: {categoria_actual} ---")
        
        # Bucle interno: proceso de corte
        while i < len(datos) and datos[i]["categoria"] == categoria_actual:
            print(f"  {datos[i]['producto']}: ${datos[i]['monto']}")
            subtotal_categoria += datos[i]["monto"]
            i += 1
            
        print(f"Subtotal {categoria_actual}: ${subtotal_categoria}")
        print("-" * 20)
        total_general += subtotal_categoria
        
    print(f"Total General: ${total_general}")

# Ejecutar el algoritmo
procesar_corte(ventas)
