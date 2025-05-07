# primitive_selector.py - Simulación del Selector con Variables Primitivas EXTREMA (con control de inicialización)

# --- Variables Primitivas que Representan los 8 Elementos Fijos ---
# Cada grupo de 4 variables representa un "nodo" simulado.
# Los *_next_id y *_prev_id son las "referencias encajadas" (simples IDs enteros).

# Elemento 1 (Patrick)
element1_id = 1
element1_name = "Patrick"
element1_next_id = 2
element1_prev_id = 8

# Elemento 2 (Spongebob)
element2_id = 2
element2_name = "Spongebob"
element2_next_id = 3
element2_prev_id = 1

# Elemento 3 (Aang)
element3_id = 3
element3_name = "Aang"
element3_next_id = 4
element3_prev_id = 2

# Elemento 4 (Korra)
element4_id = 4
element4_name = "Korra"
element4_next_id = 5
element4_prev_id = 3

# Elemento 5 (Garfield)
element5_id = 5
element5_name = "Garfield"
element5_next_id = 6
element5_prev_id = 4

# Elemento 6 (Reptar)
element6_id = 6
element6_name = "Reptar"
element6_next_id = 7
element6_prev_id = 5

# Elemento 7 (Zim)
element7_id = 7
element7_name = "Zim"
element7_next_id = 8
element7_prev_id = 6

# Elemento 8 (Jenny)
element8_id = 8
element8_name = "Jenny"
element8_next_id = 1
element8_prev_id = 7

# --- Variable para Rastrea el Elemento Actualmente Seleccionado ---
# Inicializamos con un valor que no es un ID válido (0 o -1)
# para indicar que aún no hay nada seleccionado hasta inicializar.
current_primitive_element_id = 0 # Usamos 0 o un valor fuera del rango 1-8

# --- Variable para rastrear si el selector ha sido inicializado ---
is_primitive_selector_initialized = False # Estado inicial: no inicializado

# --- Operaciones Públicas para el Selector Primitivo ---

def initialize_primitive_selector():
    """
    Inicializa el selector primitivo.
    Establece el ID del elemento actual al primero y marca como inicializado.
    """
    global current_primitive_element_id
    global is_primitive_selector_initialized

    current_primitive_element_id = element1_id # Establece al primer elemento (ID 1)
    is_primitive_selector_initialized = True # Marca como inicializado

    print("Selector primitivo inicializado con 8 elementos fijos.")
    display_primitive_simple_selection() # Mostrar el primero después de inicializar
    print("-" * 20)

def move_primitive_next():
    """
    Mueve la selección al siguiente elemento, solo si está inicializado.
    """
    global current_primitive_element_id
    global is_primitive_selector_initialized # Necesario para leer el estado

    if not is_primitive_selector_initialized:
        print("Error: El selector primitivo no ha sido inicializado. Por favor, seleccione la opción 1 primero.")
        return # Sale de la función si no está inicializado

    # Lógica para encontrar el siguiente ID
    next_id = None
    if current_primitive_element_id == 1: next_id = element1_next_id
    elif current_primitive_element_id == 2: next_id = element2_next_id
    elif current_primitive_element_id == 3: next_id = element3_next_id
    elif current_primitive_element_id == 4: next_id = element4_next_id
    elif current_primitive_element_id == 5: next_id = element5_next_id
    elif current_primitive_element_id == 6: next_id = element6_next_id
    elif current_primitive_element_id == 7: next_id = element7_next_id
    elif current_primitive_element_id == 8: next_id = element8_next_id
    
    current_primitive_element_id = next_id # next_id siempre será válido (1-8)

    print("Movido al siguiente.")
    display_primitive_simple_selection()

def move_primitive_previous():
    """
    Mueve la selección al elemento anterior, solo si está inicializado.
    """
    global current_primitive_element_id
    global is_primitive_selector_initialized # Necesario para leer el estado

    if not is_primitive_selector_initialized:
        print("Error: El selector primitivo no ha sido inicializado. Por favor, seleccione la opción 1 primero.")
        return # Sale de la función si no está inicializado

    # Lógica para encontrar el anterior ID
    prev_id = None
    if current_primitive_element_id == 1: prev_id = element1_prev_id
    elif current_primitive_element_id == 2: prev_id = element2_prev_id
    elif current_primitive_element_id == 3: prev_id = element3_prev_id
    elif current_primitive_element_id == 4: prev_id = element4_prev_id
    elif current_primitive_element_id == 5: prev_id = element5_prev_id
    elif current_primitive_element_id == 6: prev_id = element6_prev_id
    elif current_primitive_element_id == 7: prev_id = element7_prev_id
    elif current_primitive_element_id == 8: prev_id = element8_prev_id

    current_primitive_element_id = prev_id # prev_id siempre será válido (1-8)

    print("Movido al anterior.")
    display_primitive_simple_selection()


def display_primitive_simple_selection():
    """
    Muestra una versión simple del elemento actualmente seleccionado,
    accediendo a los datos directamente con lógica condicional,
    solo si está inicializado.
    """
    global is_primitive_selector_initialized # Necesario para leer el estado

    if not is_primitive_selector_initialized:
        # No imprimir mensaje aquí, ya que es una función llamada por otras.
        # La función que la llama (move_next/prev o display_detailed) ya imprime el error.
        return

    # Lógica para obtener los datos
    current_id = None
    current_name = None
    if current_primitive_element_id == 1: current_id = element1_id; current_name = element1_name
    elif current_primitive_element_id == 2: current_id = element2_id; current_name = element2_name
    elif current_primitive_element_id == 3: current_id = element3_id; current_name = element3_name
    elif current_primitive_element_id == 4: current_id = element4_id; current_name = element4_name
    elif current_primitive_element_id == 5: current_id = element5_id; current_name = element5_name
    elif current_primitive_element_id == 6: current_id = element6_id; current_name = element6_name
    elif current_primitive_element_id == 7: current_id = element7_id; current_name = element7_name
    elif current_primitive_element_id == 8: current_id = element8_id; current_name = element8_name

    print(f"Elemento actual: {current_name} (ID: {current_id})")


def display_primitive_detailed_selection():
    """
    Muestra la información detallada del elemento actualmente seleccionado,
    accediendo a los datos directamente con lógica condicional,
    solo si está inicializado.
    """
    global is_primitive_selector_initialized # Necesario para leer el estado

    if not is_primitive_selector_initialized:
        print("Error: El selector primitivo no ha sido inicializado. Por favor, seleccione la opción 1 primero.")
        return

    # Lógica para obtener los datos
    current_id = None
    current_name = None
    if current_primitive_element_id == 1: current_id = element1_id; current_name = element1_name
    elif current_primitive_element_id == 2: current_id = element2_id; current_name = element2_name
    elif current_primitive_element_id == 3: current_id = element3_id; current_name = element3_name
    elif current_primitive_element_id == 4: current_id = element4_id; current_name = element4_name
    elif current_primitive_element_id == 5: current_id = element5_id; current_name = element5_name
    elif current_primitive_element_id == 6: current_id = element6_id; current_name = element6_name
    elif current_primitive_element_id == 7: current_id = element7_id; current_name = element7_name
    elif current_primitive_element_id == 8: current_id = element8_id; current_name = element8_name

    print("\n--- Detalles del Elemento Seleccionado (Primitivo Brutal) ---")
    print(f"ID: {current_id}")
    print(f"Nombre: {current_name}")
    print("-----------------------------------------------------------")


def list_primitive_elements():
    """
    Simula listar todos los elementos, solo si está inicializado.
    """
    global is_primitive_selector_initialized # Necesario para leer el estado

    if not is_primitive_selector_initialized:
        print("Error: El selector primitivo no ha sido inicializado. Por favor, seleccione la opción 1 primero.")
        return

    print("\n--- Todos los Elementos en el Selector (Primitivo Brutal) ---")
    start_id = 1 # Punto de partida fijo para listar
    current_list_id = start_id
    count = 0
    total_elements = 8

    while count < total_elements:
        # Lógica para obtener los datos del elemento actual de la lista
        list_element_id = None
        list_element_name = None
        if current_list_id == 1: list_element_id = element1_id; list_element_name = element1_name
        elif current_list_id == 2: list_element_id = element2_id; list_element_name = element2_name
        elif current_list_id == 3: list_element_id = element3_id; list_element_name = element3_name
        elif current_list_id == 4: list_element_id = element4_id; list_element_name = element4_name
        elif current_list_id == 5: list_element_id = element5_id; list_element_name = element5_name
        elif current_list_id == 6: list_element_id = element6_id; list_element_name = element6_name
        elif current_list_id == 7: list_element_id = element7_id; list_element_name = element7_name
        elif current_list_id == 8: list_element_id = element8_id; list_element_name = element8_name

        print(f"- ID: {list_element_id}, Nombre: {list_element_name}")

        # Lógica para obtener el siguiente ID para el recorrido
        next_list_id = None
        if current_list_id == 1: next_list_id = element1_next_id
        elif current_list_id == 2: next_list_id = element2_next_id
        elif current_list_id == 3: next_list_id = element3_next_id
        elif current_list_id == 4: next_list_id = element4_next_id
        elif current_list_id == 5: next_list_id = element5_next_id
        elif current_list_id == 6: next_list_id = element6_next_id
        elif current_list_id == 7: next_list_id = element7_next_id
        elif current_list_id == 8: next_list_id = element8_next_id

        current_list_id = next_list_id
        count += 1
    print("-------------------------------------------------")

# --- Bucle Principal de la Aplicación de Consola Primitiva Extrema ---

def print_primitive_brutal_menu():
    """Muestra el menú de opciones para la versión primitiva brutal."""
    print("\n--- Menú del Selector Cíclico (Primitivo Brutal) ---")
    print("1. Inicializar Selector (Cargar 8 elementos fijos)")
    print("2. Mover Siguiente")
    print("3. Mover Anterior")
    print("4. Mostrar Elemento Seleccionado (Detalles Brutales)")
    print("5. Listar Todos los Elementos (Brutal)")
    print("6. Salir")
    print("----------------------------------------------------")

def main_primitive_brutal():
    """Función principal que ejecuta la aplicación de consola primitiva brutal."""
    print("Bienvenido al Selector Cíclico de Elementos (Versión Primitiva Brutal)!")

    # No inicializamos automáticamente aquí, esperando la opción 1 del usuario

    while True:
        print_primitive_brutal_menu()
        choice = input("Ingrese su opción: ")

        if choice == '1':
            # Si ya estaba inicializado, podemos simular una "reinicialización"
            # aunque en esta versión fija no cambia mucho más que el current_id
            if is_primitive_selector_initialized:
                 print("El selector primitivo ya ha sido inicializado. Reiniciando selección...")
            initialize_primitive_selector()
        elif choice == '2':
            move_primitive_next()
        elif choice == '3':
            move_primitive_previous()
        elif choice == '4':
            display_primitive_detailed_selection()
        elif choice == '5':
            list_primitive_elements()
        elif choice == '6':
            print("Saliendo del Selector Primitivo Brutal. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# --- Punto de Entrada del Ejecutable Primitivo Brutal ---
if __name__ == "__main__":
    main_primitive_brutal()