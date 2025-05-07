# Documentación Parte 1: Selector Cíclico con Lista Doblemente Enlazada Circular (CDLL)

Este documento describe la primera fase del proyecto "Selector Cíclico de Elementos", donde se implementa la funcionalidad principal utilizando una Lista Doblemente Enlazada Circular (CDLL) como la estructura de datos central. Esta implementación sirve como la versión "estándar" o "normal" que demuestra el uso eficiente de la estructura asignada y que será contrastada con la implementación primitiva en la Parte 2.

## 1. Caso de Uso y Aplicación de la CDLL

El caso de uso implementado es un **Selector Cíclico de Elementos** operado a través de una interfaz de consola. La aplicación presenta una lista de elementos (como personajes) y permite al usuario navegar por ellos hacia adelante (Siguiente) y hacia atrás (Anterior). La característica cíclica implica que al ir "Siguiente" desde el último elemento, se regresa al primero, y al ir "Anterior" desde el primero, se regresa al último.

La **Lista Doblemente Enlazada Circular (CDLL)** es la estructura de datos ideal para este problema y se integra de la siguiente manera:

*   Cada **elemento seleccionable** (ej. un personaje) se almacena como los **datos** de un **Nodo** en la lista.
*   La **navegación "Siguiente" y "Anterior"** se realiza siguiendo los punteros `next` y `prev` de los Nodos.
*   La propiedad **circular** de la CDLL (donde el último nodo apunta al primero, y el primer nodo apunta al último) implementa intrínsecamente el comportamiento de "envolver" en los extremos, haciendo que la lógica de navegación sea simple y uniforme para todos los nodos.
*   La lista mantiene una referencia (`current`) al nodo actualmente seleccionado para facilitar las operaciones.

## 2. Estructura del Proyecto (Parte 1)

Esta primera parte del proyecto se organiza en tres archivos principales para separar la definición de la estructura de datos, la lógica de negocio/operaciones y la interfaz de usuario/ejecución principal:

*   **`CDLLB.py`**: Contiene la definición de la estructura de datos (Clase `Node` y Clase `CircularDoubleLinkedList`). Define cómo se representan individualmente los nodos y cómo se gestiona la lista en su conjunto.
*   **`operations.py`**: Contiene las funciones que implementan las operaciones lógicas del selector (inicializar, mover, mostrar, listar). Estas funciones **utilizan** una instancia de la clase `CircularDoubleLinkedList` para realizar sus tareas, actuando como una capa de "lógica de negocio".
*   **`main.py`**: Es el punto de entrada de la aplicación de consola. Contiene el bucle principal que muestra el menú al usuario, lee su entrada y llama a las funciones apropiadas definidas en `operations.py`. Es la capa de "interfaz de usuario".

## 3. Contenido de los Archivos

### `CDLLB.py`

Este archivo define las clases fundamentales:

*   **Clase `ElementData`**: Una clase auxiliar simple para encapsular los datos primitivos (`int id`, `str nombre`) de un elemento seleccionable. Aunque una clase podría considerarse una estructura, aquí actúa principalmente como un contenedor simple de primitivos para el nodo.
*   **Clase `Node`**: Representa un nodo individual en la lista. Contiene:
    *   `data`: Una instancia de `ElementData` con la información del elemento.
    *   `next`: Una referencia al siguiente nodo en la lista.
    *   `prev`: Una referencia al nodo anterior en la lista.
*   **Clase `CircularDoubleLinkedList`**: Gestiona la colección de nodos. Contiene:
    *   `head`: Referencia al primer nodo de la lista.
    *   `current`: Referencia al nodo actualmente seleccionado (clave para la navegación del selector).
    *   `size`: El número de nodos en la lista.
    *   Métodos para manipular la lista, como `append()` para añadir nodos, `move_next()` y `move_previous()` para la navegación, `get_current_data()` para obtener los datos del nodo actual, y `list_all_elements()` para recorrer la lista.

### `operations.py`

Este archivo contiene funciones que actúan sobre una instancia de `CircularDoubleLinkedList`. Implementan las operaciones del selector:

*   `initialize_selector(cdll)`: Crea una lista inicial de 8 elementos predefinidos (instancias de `ElementData`) y las añade a la `cdll` usando `cdll.append()`. Establece la selección inicial.
*   `move_selector_next(cdll)`: Llama a `cdll.move_next()` para avanzar la selección y luego llama a `display_simple_selection()` para mostrar el nuevo elemento actual de forma concisa.
*   `move_selector_previous(cdll)`: Llama a `cdll.move_previous()` para retroceder la selección y luego llama a `display_simple_selection()` para mostrar el nuevo elemento actual de forma concisa.
*   `display_simple_selection(cdll)`: Obtiene los datos del nodo `current` (`cdll.get_current_data()`) y los muestra en un formato simple (Nombre (ID)). Utilizada después de los movimientos.
*   `display_detailed_selection(cdll)`: Obtiene los datos del nodo `current` y los muestra en un formato más detallado. Utilizada para la opción específica del menú.
*   `display_all_selector_elements(cdll)`: Llama a `cdll.list_all_elements()` para obtener una lista de todos los datos de los elementos y los imprime, recorriendo la CDLL.

### `main.py`

Este archivo es el punto de entrada y orquesta la ejecución:

*   Importa las clases necesarias de `CDLLB.py` y las funciones de `operations.py`.
*   Crea una instancia de `CircularDoubleLinkedList` (`selector_cdll`).
*   Implementa la función `print_menu()` para mostrar las opciones al usuario.
*   La función `main()` contiene el bucle principal:
    *   Muestra el menú.
    *   Lee la entrada del usuario.
    *   Utiliza lógica condicional (`if/elif`) para llamar a la función correspondiente en `operations.py` basándose en la opción del usuario, pasando la instancia `selector_cdll`.
    *   Maneja la opción de "Salir".
    *   Incluye manejo básico de errores para entradas no válidas y evita operaciones si el selector no ha sido inicializado (simulando el comportamiento de una lista vacía).
*   El bloque `if __name__ == "__main__":` asegura que `main()` se ejecute solo cuando el script es llamado directamente.

## 4. Funcionamiento General

Al ejecutar `main.py`, el usuario interactúa con el menú de consola. Las opciones del menú (2 a 5) operan sobre la instancia de `CircularDoubleLinkedList` (`selector_cdll`) a través de las funciones definidas en `operations.py`. La inicialización (Opción 1) es necesaria antes de la mayoría de las operaciones de movimiento o visualización, garantizando que la CDLL contenga elementos y el puntero `current` sea válido.

Esta primera parte demuestra cómo una estructura de datos especializada como la CDLL resuelve de manera elegante y eficiente el problema de la navegación cíclica, sirviendo como la base funcional para la comparación posterior con la implementación puramente primitiva.
