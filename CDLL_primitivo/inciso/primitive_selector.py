# primitive_selector.py - Simulación del Selector con Variables Primitivas (Auto-ejecutable)

# --- Variables Primitivas que Representan los 8 Elementos Fijos ---
# Cada grupo de 4 variables representa un "nodo" simulado.
# Los *_next_id y *_prev_id son las "referencias encajadas" (simples IDs enteros).

# Elemento 1 (Patrick)
element1_id = 1
element1_name = "Patrick"
element1_next_id = 2  # Siguiente es Elemento 2
element1_prev_id = 8  # Anterior es Elemento 8 (circular)

# Elemento 2 (Spongebob)
element2_id = 2
element2_name = "Spongebob"
element2_next_id = 3  # Siguiente es Elemento 3
element2_prev_id = 1  # Anterior es Elemento 1

# Elemento 3 (Aang)
element3_id = 3
element3_name = "Aang"
element3_next_id = 4  # Siguiente es Elemento 4
element3_prev_id = 2  # Anterior es Elemento 2

# Elemento 4 (Korra)
element4_id = 4
element4_name = "Korra"
element4_next_id = 5  # Siguiente es Elemento 5
element4_prev_id = 3  # Anterior es Elemento 3

# Elemento 5 (Garfield)
element5_id = 5
element5_name = "Garfield"
element5_next_id = 6  # Siguiente es Elemento 6
element5_prev_id = 4  # Anterior es Elemento 4

# Elemento 6 (Reptar)
element6_id = 6
element6_name = "Reptar"
element6_next_id = 7  # Siguiente es Elemento 7
element6_prev_id = 5  # Anterior es Elemento 5

# Elemento 7 (Zim)
element7_id = 7
element7_name = "Zim"
element7_next_id = 8  # Siguiente es Elemento 8
element7_prev_id = 6  # Anterior es Elemento 6

# Elemento 8 (Jenny)
element8_id = 8
element8_name = "Jenny"
element8_next_id = 1  # Siguiente es Elemento 1 (circular)
element8_prev_id = 7  # Anterior es Elemento 7

# --- Variable para Rastrea el Elemento Actualmente Seleccionado ---
# Esta variable primitiva guarda el ID del elemento actual.
# Es la única forma "global" de saber dónde estamos sin una estructura de lista.
# Se inicializa con el ID del primer elemento.
current_primitive_element_id = element1_id

# --- Lógica para Obtener Datos y Enlaces basado en ID ---
# Estas funciones simulan la "desreferenciación" de los IDs
# usando lógica condicional extensa.

def _get_primitive_element_data(element_id: int) -> tuple[int, str] | None:
    """
    Función auxiliar para obtener el ID y nombre de un elemento
    dado su ID, usando solo lógica condicional.
    """
    if element_id == 1:
        return (element1_id, element1_name)
    elif element_id == 2:
        return (element2_id, element2_name)
    elif element_id == 3:
        return (element3_id, element3_name)
    elif element_id == 4:
        return (element4_id, element4_name)
    elif element_id == 5:
        return (element5_id, element5_name)
    elif element_id == 6:
        return (element6_id, element6_name)
    elif element_id == 7:
        return (element7_id, element7_name)
    elif element_id == 8:
        return (element8_id, element8_name)
    else:
        return None # ID no válido

def _get_primitive_next_id(element_id: int) -> int | None:
    """
    Función auxiliar para obtener el ID del siguiente elemento
    dado el ID actual, usando solo lógica condicional.
    """
    if element_id == 1: return element1_next_id
    elif element_id == 2: return element2_next_id
    elif element_id == 3: return element3_next_id
    elif element_id == 4: return element4_next_id
    elif element_id == 5: return element5_next_id
    elif element_id == 6: return element6_next_id
    elif element_id == 7: return element7_next_id
    elif element_id == 8: return element8_next_id
    else: return None

def _get_primitive_prev_id(element_id: int) -> int | None:
    """
    Función auxiliar para obtener el ID del anterior elemento
    dado el ID actual, usando solo lógica condicional.
    """
    if element_id == 1: return element1_prev_id
    elif element_id == 2: return element2_prev_id
    elif element_id == 3: return element3_prev_id
    elif element_id == 4: return element4_prev_id
    elif element_id == 5: return element5_prev_id
    elif element_id == 6: return element6_prev_id
    elif element_id == 7: return element7_prev_id
    elif element_id == 8: return element8_prev_id
    else: return None

# --- Operaciones Públicas para el Selector Primitivo ---
# (Estas funciones son llamadas por el bucle principal en este mismo archivo)

def initialize_primitive_selector():
    """
    (Simulado) Inicializa el selector primitivo.
    Solo asegura que la selección empiece en el primer elemento.
    """
    global current_primitive_element_id
    current_primitive_element_id = element1_id
    print("Selector primitivo inicializado con 8 elementos fijos.")
    display_primitive_simple_selection()
    print("-" * 20)


def move_primitive_next():
    """
    Mueve la selección al siguiente elemento usando IDs y lógica condicional.
    """
    global current_primitive_element_id
    next_id = _get_primitive_next_id(current_primitive_element_id)
    # Como siempre hay 8 elementos y los enlaces son correctos, next_id nunca será None
    current_primitive_element_id = next_id
    print("Movido al siguiente.")
    display_primitive_simple_selection()

def move_primitive_previous():
    """
    Mueve la selección al elemento anterior usando IDs y lógica condicional.
    """
    global current_primitive_element_id
    prev_id = _get_primitive_prev_id(current_primitive_element_id)
    # Como siempre hay 8 elementos y los enlaces son correctos, prev_id nunca será None
    current_primitive_element_id = prev_id
    print("Movido al anterior.")
    display_primitive_simple_selection()


def display_primitive_simple_selection():
    """
    Muestra una versión simple del elemento actualmente seleccionado.
    """
    current_data = _get_primitive_element_data(current_primitive_element_id)
    # Con 8 elementos fijos y IDs 1-8, current_data siempre será válido aquí
    id, nombre = current_data
    print(f"Elemento actual: {nombre} (ID: {id})")


def display_primitive_detailed_selection():
    """
    Muestra la información detallada del elemento actualmente seleccionado.
    """
    current_data = _get_primitive_element_data(current_primitive_element_id)
    # Con 8 elementos fijos y IDs 1-8, current_data siempre será válido aquí
    id, nombre = current_data
    print("\n--- Detalles del Elemento Seleccionado (Primitivo) ---")
    print(f"ID: {id}")
    print(f"Nombre: {nombre}")
    print("---------------------------------------------------")


def list_primitive_elements():
    """
    Simula listar todos los elementos recorriendo la estructura simulada
    con IDs y lógica condicional.
    """
    print("\n--- Todos los Elementos en el Selector (Primitivo) ---")
    start_id = 1
    current_list_id = start_id
    count = 0
    total_elements = 8

    while count < total_elements:
        data = _get_primitive_element_data(current_list_id)
        if data:
            id, nombre = data
            print(f"- ID: {id}, Nombre: {nombre}")
            current_list_id = _get_primitive_next_id(current_list_id)
            count += 1
        # No necesitamos else/error handling aquí si los enlaces están bien definidos
    print("-------------------------------------------------")

# --- Bucle Principal de la Aplicación de Consola Primitiva ---

def print_primitive_menu():
    """Muestra el menú de opciones para la versión primitiva."""
    print("\n--- Menú del Selector Cíclico (Primitivo) ---")
    print("1. Inicializar Selector (Cargar 8 elementos fijos)") # El nombre indica que son fijos
    print("2. Mover Siguiente")
    print("3. Mover Anterior")
    print("4. Mostrar Elemento Seleccionado (Detalles)")
    print("5. Listar Todos los Elementos")
    print("6. Salir")
    print("-----------------------------------------------")

def main_primitive():
    """Función principal que ejecuta la aplicación de consola primitiva."""
    print("Bienvenido al Selector Cíclico de Elementos (Versión Primitiva)!")

    # Puedes inicializar automáticamente al inicio
    # initialize_primitive_selector()
    # display_primitive_simple_selection()

    while True:
        print_primitive_menu()
        choice = input("Ingrese su opción: ")

        if choice == '1':
            # En la versión primitiva, inicializar solo reinicia la selección al primero
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
            print("Saliendo del Selector Primitivo. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# --- Punto de Entrada del Ejecutable Primitivo ---
if __name__ == "__main__":
    main_primitive()