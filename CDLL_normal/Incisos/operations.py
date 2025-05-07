# operations.py - Funciones de Operación para el Selector CDLL
# Aqui estan las funciones que se aplicaran a la CDLL
from CDLLB import CircularDoubleLinkedList, ElementData

def initialize_selector(cdll: CircularDoubleLinkedList):
    """
    Inicializa el selector CDLL con un conjunto de 8 elementos predefinidos.
    """
    print("Inicializando selector con elementos...")
    # Conjunto de 8 elementos/personajes iniciales
    elements = [
        ElementData(1, "A"),
        ElementData(2, "B"),
        ElementData(3, "C"),
        ElementData(4, "D"),
        ElementData(5, "E"),
        ElementData(6, "F"), # Nuevo elemento
        ElementData(7, "G"),    # Nuevo elemento
        ElementData(8, "H")   # Nuevo elemento
    ]

    # Limpiar la lista si ya tenía elementos (útil si se llama varias veces)
    # Aunque para este proyecto simple no debería ser necesario
    # cdll.__init__()

    for element_data in elements:
        cdll.append(element_data)

    print(f"Selector inicializado con {cdll.size} elementos.")
    if not cdll.is_empty():
         # Mostrar el primer elemento seleccionado después de inicializar
         display_simple_selection(cdll)
    print("-" * 20)

def display_simple_selection(cdll: CircularDoubleLinkedList):
    """
    Muestra una versión simple de la información del elemento actualmente seleccionado.
    Usado después de mover para confirmación rápida.
    """
    current_data = cdll.get_current_data()
    if current_data:
        # Formato simple: Nombre (ID: X)
        print(f"Elemento actual: {current_data.nombre} (ID: {current_data.id})")
    else:
        print("El selector está vacío.")


def display_detailed_selection(cdll: CircularDoubleLinkedList):
    """
    Muestra la información completa del elemento actualmente seleccionado.
    Usado específicamente para la opción 4.
    """
    current_data = cdll.get_current_data()
    if current_data:
        print("\n--- Detalles del Elemento Seleccionado ---")
        print(f"ID: {current_data.id}")
        print(f"Nombre: {current_data.nombre}")
        # Aquí podrías añadir más detalles si ElementData tuviera más atributos
        print("-------------------------------------------")
    else:
        print("El selector está vacío.")


def move_selector_next(cdll: CircularDoubleLinkedList):
    """
    Intenta mover la selección al siguiente elemento y muestra confirmación simple.
    """
    if cdll.is_empty():
        print("El selector está vacío, no se puede mover.")
        return

    cdll.move_next()
    print("Movido al siguiente.")
    display_simple_selection(cdll) # Mostrar confirmación simple después de mover


def move_selector_previous(cdll: CircularDoubleLinkedList):
    """
    Intenta mover la selección al elemento anterior y muestra confirmación simple.
    """
    if cdll.is_empty():
        print("El selector está vacío, no se puede mover.")
        return

    cdll.move_previous()
    print("Movido al anterior.")
    display_simple_selection(cdll) # Mostrar confirmación simple después de mover


def display_all_selector_elements(cdll: CircularDoubleLinkedList):
    """
    Muestra la información de todos los elementos en el selector.
    """
    all_elements = cdll.list_all_elements()
    if all_elements:
        print("\n--- Todos los Elementos en el Selector ---")
        for element_data in all_elements:
            print(f"- ID: {element_data.id}, Nombre: {element_data.nombre}") # Formato de lista
        print("------------------------------------------")
    else:
        print("El selector está vacío.")
