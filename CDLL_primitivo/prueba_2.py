# primitive_selector.py - Simulación del Selector Primitivo EXTREMO y Obsoleto

# --- Variables Primitivas que Representan los 8 Elementos Fijos ---
# Cada grupo de 4 variables representa un "nodo" simulado.
# Los *_next_id y *_prev_id son las "referencias encajadas" (simples IDs enteros).

# Elemento 1 
element1_id = 1
element1_name = "A"
element1_next_id = 2
element1_prev_id = 8

# Elemento 2 
element2_id = 2
element2_name = "B"
element2_next_id = 3
element2_prev_id = 1

# Elemento 3 
element3_id = 3
element3_name = "C"
element3_next_id = 4
element3_prev_id = 2

# Elemento 4 
element4_id = 4
element4_name = "D"
element4_next_id = 5
element4_prev_id = 3

# Elemento 5 
element5_id = 5
element5_name = "E"
element5_next_id = 6
element5_prev_id = 4

# Elemento 6 
element6_id = 6
element6_name = "F"
element6_next_id = 7
element6_prev_id = 5

# Elemento 7 
element7_id = 7
element7_name = "G"
element7_next_id = 8
element7_prev_id = 6

# Elemento 8 
element8_id = 8
element8_name = "H"
element8_next_id = 1
element8_prev_id = 7

# --- Variable para Rastrea el Elemento Actualmente Seleccionado ---
# Inicializamos con un valor no válido (0) para indicar que no hay selección activa.
current_primitive_element_id = 0

# is_primitive_selector_initialized VARIABLE ELIMINADA para hacerlo más primitivo.
# Ahora el estado de inicialización se verifica viendo si current_primitive_element_id es 0.

# --- Operaciones Públicas para el Selector Primitivo ---

def initialize_primitive_selector():
    """
    Establece el punto de partida inicial del selector primitivo.
    """
    global current_primitive_element_id
    # No hay "carga", los elementos están fijos.
    # Simplemente establecemos el ID del primer elemento como el actual.
    current_primitive_element_id = element1_id # Establece al primer elemento (ID 1)

    print("Selector primitivo obsoleto inicializado (punto de partida establecido).")
    # No mostramos el elemento actual aquí, el usuario debe seleccionarlo con Opción 4.
    print("-" * 20)

def move_primitive_next():
    """
    Mueve la selección al siguiente elemento, solo si el selector está operativo.
    """
    global current_primitive_element_id

    # Verificar si el selector está operativo (si current_primitive_element_id es válido)
    if current_primitive_element_id == 0:
        print("Error: El selector primitivo obsoleto no está operativo. Por favor, inicialice (Opción 1).")
        return

    # Lógica para encontrar el siguiente ID (duplicada, brutal)
    next_id = 0 # Usamos 0 como valor temporal de no encontrado
    if current_primitive_element_id == 1:
        next_id = element1_next_id
    elif current_primitive_element_id == 2:
        next_id = element2_next_id
    elif current_primitive_element_id == 3:
        next_id = element3_next_id
    elif current_primitive_element_id == 4:
        next_id = element4_next_id
    elif current_primitive_element_id == 5:
        next_id = element5_next_id
    elif current_primitive_element_id == 6:
        next_id = element6_next_id
    elif current_primitive_element_id == 7:
        next_id = element7_next_id
    elif current_primitive_element_id == 8:
        next_id = element8_next_id
    # next_id siempre será válido (1-8) si current_primitive_element_id era 1-8

    current_primitive_element_id = next_id

    print("Movido al siguiente.")
    # No mostramos el elemento actual aquí. El usuario debe seleccionar la Opción 4.
    # display_primitive_simple_selection() # <-- Eliminado para más "obsolescencia"


def move_primitive_previous():
    """
    Mueve la selección al elemento anterior, solo si el selector está operativo.
    """
    global current_primitive_element_id

    # Verificar si el selector está operativo
    if current_primitive_element_id == 0:
        print("Error: El selector primitivo obsoleto no está operativo. Por favor, inicialice (Opción 1).")
        return

    # Lógica para encontrar el anterior ID (duplicada, brutal)
    prev_id = 0 # Usamos 0 como valor temporal de no encontrado
    if current_primitive_element_id == 1:
        prev_id = element1_prev_id
    elif current_primitive_element_id == 2:
        prev_id = element2_prev_id
    elif current_primitive_element_id == 3:
        prev_id = element3_prev_id
    elif current_primitive_element_id == 4:
        prev_id = element4_prev_id
    elif current_primitive_element_id == 5:
        prev_id = element5_prev_id
    elif current_primitive_element_id == 6:
        prev_id = element6_prev_id
    elif current_primitive_element_id == 7:
        prev_id = element7_prev_id
    elif current_primitive_element_id == 8:
        prev_id = element8_prev_id

    current_primitive_element_id = prev_id

    print("Movido al anterior.")
    # No mostramos el elemento actual aquí. El usuario debe seleccionar la Opción 4.
    # display_primitive_simple_selection() # <-- Eliminado para más "obsolescencia"


# display_primitive_simple_selection ELIMINADA completamente ya que no se llama internamente

def display_primitive_detailed_selection():
    """
    Muestra la información detallada del elemento actualmente seleccionado,
    accediendo a los datos directamente con lógica condicional,
    solo si el selector está operativo.
    """
    # Verificar si el selector está operativo
    if current_primitive_element_id == 0:
        print("Error: El selector primitivo obsoleto no está operativo. Por favor, inicialice (Opción 1).")
        return

    # Lógica para obtener los datos (duplicada, brutal)
    current_id_display = 0
    current_name_display = ""
    if current_primitive_element_id == 1:
        current_id_display = element1_id
        current_name_display = element1_name
    elif current_primitive_element_id == 2:
        current_id_display = element2_id
        current_name_display = element2_name
    elif current_primitive_element_id == 3:
        current_id_display = element3_id
        current_name_display = element3_name
    elif current_primitive_element_id == 4:
        current_id_display = element4_id
        current_name_display = element4_name
    elif current_primitive_element_id == 5:
        current_id_display = element5_id
        current_name_display = element5_name
    elif current_primitive_element_id == 6:
        current_id_display = element6_id
        current_name_display = element6_name
    elif current_primitive_element_id == 7:
        current_id_display = element7_id
        current_name_display = element7_name
    elif current_primitive_element_id == 8:
        current_id_display = element8_id
        current_name_display = element8_name
    # current_id_display y current_name_display siempre serán válidos si current_primitive_element_id es 1-8

    print("\n--- Detalles del Elemento Seleccionado (Primitivo Obsoleto) ---")
    print(f"ID: {current_id_display}")
    print(f"Nombre: {current_name_display}")
    print("-------------------------------------------------------------")


def list_primitive_elements():
    """
    Simula listar todos los elementos, solo si el selector está operativo.
    """
    # Verificar si el selector está operativo
    if current_primitive_element_id == 0:
        print("Error: El selector primitivo obsoleto no está operativo. Por favor, inicialice (Opción 1).")
        return

    print("\n--- Todos los Elementos en el Selector (Primitivo Obsoleto) ---")
    start_id = 1 # Punto de partida fijo para listar
    current_list_id = start_id
    count = 0
    total_elements = 8

    # Recorremos los 8 elementos
    while count < total_elements:
        # Lógica para obtener los datos del elemento actual de la lista (duplicada, brutal)
        list_element_id = 0
        list_element_name = ""
        if current_list_id == 1: list_element_id = element1_id; list_element_name = element1_name
        elif current_list_id == 2: list_element_id = element2_id; list_element_name = element2_name
        elif current_list_id == 3: list_element_id = element3_id; list_element_name = element3_name
        elif current_list_id == 4: list_element_id = element4_id; list_element_name = element4_name
        elif current_list_id == 5: list_element_id = element5_id; list_element_name = element5_name
        elif current_list_id == 6: list_element_id = element6_id; list_element_name = element6_name
        elif current_list_id == 7: list_element_id = element7_id; list_element_name = element7_name
        elif current_list_id == 8: list_element_id = element8_id; list_element_name = element8_name

        print(f"- ID: {list_element_id}, Nombre: {list_element_name}")

        # Lógica para obtener el siguiente ID para el recorrido (duplicada, brutal)
        next_list_id = 0
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

# --- Bucle Principal de la Aplicación de Consola Primitiva Obsoleta ---

def print_primitive_obsolete_menu():
    """Muestra el menú de opciones para la versión primitiva obsoleta."""
    print("\n--- Menú del Selector Cíclico (Primitivo Obsoleto) ---")
    print("1. Inicializar Selector (Establecer punto de partida)")
    print("2. Mover Siguiente")
    print("3. Mover Anterior")
    print("4. Mostrar Elemento Seleccionado (Detalles Obsoletos)")
    print("5. Listar Todos los Elementos (Obsoleto)")
    print("6. Salir")
    print("----------------------------------------------------")

def main_primitive_obsolete():
    """Función principal que ejecuta la aplicación de consola primitiva obsoleta."""
    print("Bienvenido al Selector Cíclico de Elementos (Versión Primitiva Obsoleta)!")
    print("El selector no está operativo hasta que se inicialice.")

    while True:
        print_primitive_obsolete_menu()
        choice = input("Ingrese su opción: ")

        if choice == '1':
            # Verificar si ya está "inicializado" (si current_primitive_element_id no es 0)
            if current_primitive_element_id != 0:
                 print("El selector primitivo obsoleto ya ha sido inicializado. Reiniciando punto de partida...")
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
            print("Saliendo del Selector Primitivo Obsoleto. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# --- Punto de Entrada del Ejecutable Primitivo Obsoleto ---
if __name__ == "__main__":
    main_primitive_obsolete()