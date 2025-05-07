# main.py - Aplicación de Consola para el Selector Cíclico (Versión CDLL)
# Este es el ejecutable
from CDLLB import CircularDoubleLinkedList
from operations import (
    initialize_selector,
    move_selector_next,
    move_selector_previous,
    # display_current_selection, # Ya no importamos la versión simple para el menú principal
    display_detailed_selection, # Importamos la nueva función para detalles
    display_all_selector_elements,
    display_simple_selection # Importamos para mostrar después de inicializar
)

def print_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n--- Menú del Selector Cíclico (CDLL) ---")
    print("1. Inicializar Selector (Cargar 8 elementos)")
    print("2. Mover Siguiente")
    print("3. Mover Anterior")
    print("4. Mostrar Elemento Seleccionado (Detalles)") # Título ajustado
    print("5. Listar Todos los Elementos")
    print("6. Salir")
    print("------------------------------------------")

def main():
    """Función principal que ejecuta la aplicación de consola."""
    selector_cdll = CircularDoubleLinkedList()

    print("Bienvenido al Selector Cíclico de Elementos!")

    # Ya no inicializamos automáticamente aquí, esperando la opción 1 del usuario
    # initialize_selector(selector_cdll)
    # display_simple_selection(selector_cdll)

    while True:
        print_menu()
        choice = input("Ingrese su opción: ")

        if choice == '1':
            if not selector_cdll.is_empty():
                 print("El selector ya ha sido inicializado. Reiniciando...")
                 # Crear una nueva instancia limpia si ya existía
                 selector_cdll = CircularDoubleLinkedList() # Reinicializa la lista
            initialize_selector(selector_cdll)
            # La función initialize_selector ya llama a display_simple_selection
        elif choice == '2':
            move_selector_next(selector_cdll)
            # move_selector_next ya llama a display_simple_selection
        elif choice == '3':
            move_selector_previous(selector_cdll)
            # move_selector_previous ya llama a display_simple_selection
        elif choice == '4':
            # Aquí usamos la función que muestra detalles completos
            display_detailed_selection(selector_cdll)
        elif choice == '5':
            display_all_selector_elements(selector_cdll)
        elif choice == '6':
            print("Saliendo del Selector. ¡Adiós!")
            break # Sale del bucle while
        else:
            print("Opción no válida. Intente de nuevo.")



if __name__ == "__main__":
    main()