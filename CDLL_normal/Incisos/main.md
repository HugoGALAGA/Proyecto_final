# Explicación Detallada del Archivo `main.py` (Versión CDLL)

El archivo `main.py` es el **punto de entrada** y la **interfaz de usuario** principal para la versión del Selector Cíclico que utiliza la Lista Doblemente Enlazada Circular (CDLL). Su rol es interactuar directamente con el usuario a través de la consola y coordinar la ejecución de las operaciones definidas en `operations.py`.

## 1. Propósito del Archivo

El propósito fundamental de `main.py` es:

*   **Iniciar la aplicación:** Es el script que se ejecuta para poner en marcha el programa.
*   **Proporcionar una interfaz de usuario básica:** Muestra un menú de opciones y lee la entrada del usuario desde la consola.
*   **Orquestar la ejecución:** Llama a las funciones de `operations.py` (que a su vez operan sobre la CDLL) basándose en las elecciones del usuario.

`main.py` no contiene la implementación de la estructura de datos (`CDLLB.py`) ni la lógica detallada de las operaciones (`operations.py`). Su responsabilidad es la interacción con el usuario y la dirección del flujo del programa.

## 2. Estructura y Relación con Otros Archivos

*   `main.py` **importa** la clase `CircularDoubleLinkedList` desde `CDLLB.py` para poder crear una instancia de la lista que se utilizará durante la ejecución del programa.
*   `main.py` **importa** las funciones específicas de `operations.py` que corresponden a las acciones disponibles en el menú (inicializar, mover, mostrar, listar).
*   `main.py` **no es importado** por ningún otro archivo en esta estructura; es el script ejecutable principal.

## 3. Funciones y Lógica Implementada

El archivo `main.py` contiene la siguiente lógica y funciones:

*   **Importaciones:** Al inicio del archivo, se importan los componentes necesarios de `CDLLB.py` y `operations.py`.
*   **Instancia de la CDLL:** Se crea una única instancia de `CircularDoubleLinkedList` (`selector_cdll`). Esta instancia persistirá durante toda la ejecución del programa y mantendrá el estado actual del selector.
*   **`print_menu()`:**
    *   **Lógica:** Una función auxiliar simple cuya única tarea es imprimir en la consola las opciones disponibles para el usuario en un formato claro.
    *   **Funcionamiento:** Es llamada repetidamente dentro del bucle principal para mostrar el menú después de cada operación del usuario (excepto salir).
*   **`main()`:**
    *   **Lógica:** Esta es la función principal donde reside la lógica de la aplicación de consola.
        *   Imprime un mensaje de bienvenida.
        *   Entra en un bucle infinito (`while True`) que representa el ciclo de vida de la aplicación (mostrar menú -> obtener entrada -> realizar acción -> repetir).
        *   Dentro del bucle:
            *   Llama a `print_menu()`.
            *   Lee la opción ingresada por el usuario usando `input()`.
            *   Utiliza una serie de sentencias `if`/`elif` para evaluar la opción del usuario.
            *   Para cada opción válida (1 a 5), llama a la función correspondiente importada de `operations.py`, pasando la instancia `selector_cdll` como argumento.
            *   La opción '1' (`Inicializar Selector`) es un caso especial: si la lista ya tiene elementos, se simula una "reinicialización" creando una nueva instancia de la CDLL antes de llamar a `initialize_selector`. Esto previene añadir los elementos varias veces a la misma lista.
            *   La opción '6' (`Salir`) rompe el bucle `while True`, terminando la ejecución del programa.
            *   El bloque `else` maneja las entradas del usuario que no corresponden a ninguna opción válida, imprimiendo un mensaje de error.
        *   Incluye un mensaje de despedida al salir del bucle.
    *   **Funcionamiento:** Coordina la interacción con el usuario y la ejecución de las operaciones. No implementa la lógica de la CDLL, solo la utiliza a través de las funciones de `operations.py`.
    *   **Manejo de Errores:** Implementa manejo de errores a nivel de interfaz para entradas de menú inválidas. Se basa en las funciones de `operations.py` para el manejo de errores lógicos (ej. intentar mover en lista vacía), aunque en esta versión, la necesidad de inicializar primero reduce algunos de esos casos.

*   **Bloque `if __name__ == "__main__":`:**
    *   **Lógica:** Es un estándar en Python. Asegura que la función `main()` se llame solo cuando el script `main.py` es ejecutado directamente (no cuando es importado como un módulo en otro script).
    *   **Funcionamiento:** Es el verdadero punto de inicio de la ejecución del script.

## 4. Complejidad de las Operaciones en `main.py`

La complejidad de `main.py` se refiere principalmente a la lógica de su bucle principal por cada interacción del usuario.

*   `print_menu()`: Su complejidad es O(1) con respecto al tamaño de la lista CDLL, ya que solo imprime un número fijo de líneas de menú.
*   Lectura de `input()` y evaluación con `if/elif`: La lectura de entrada es una operación dependiente del usuario y del sistema. La evaluación de la opción mediante `if/elif` es O(1) con respecto al número de opciones del menú (un número constante).
*   Llamadas a funciones de `operations.py`: La llamada a una función es una operación O(1). La *complejidad de la operación ejecutada* por esa función (dentro de `operations.py` y `CDLLB.py`) varía (O(1) para mover/mostrar, O(N) para listar, O(N) para inicializar con N elementos), pero la lógica de `main.py` en sí misma (decidir qué función llamar) es constante por interacción.

Por lo tanto, la complejidad de **una sola iteración** del bucle principal en `main.py` (excluyendo la complejidad de la función de `operations.py` llamada) es **O(1)**. La complejidad total de la ejecución del programa depende del número de interacciones del usuario antes de salir.

## 5. Rol General en el Proyecto

`main.py` es la capa de presentación y control del Selector Cíclico (versión CDLL). Recopila la intención del usuario (qué operación quiere realizar) y delega la tarea a la capa de lógica (`operations.py`), que a su vez utiliza la estructura de datos (`CDLLB.py`) para manipular los datos subyacentes. Este diseño desacoplado facilita entender la responsabilidad de cada parte del código.
