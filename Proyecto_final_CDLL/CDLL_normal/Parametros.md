# Especificaciones - Parte 1: Implementación con Lista Doblemente Enlazada Circular (CDLL)

Este documento describe las especificaciones para la primera fase del proyecto "Selector Cíclico de Elementos", la cual será implementada utilizando una Lista Doblemente Enlazada Circular (CDLL) como estructura de datos principal.

## 1. Estructura de Datos Principal: Lista Doblemente Enlazada Circular (CDLL)

La base de esta implementación será una CDLL. Se definirán las siguientes componentes:

*   **Nodo (Node):**
    *   Representará un elemento individual en la lista (ej. un personaje).
    *   Contendrá una sección para almacenar los **datos del elemento**. Estos datos serán representados por **tipos primitivos** (ej. `str` para el nombre, `int` para un identificador único, etc.).
    *   Contendrá un **puntero/referencia `next`** que apunta al siguiente Nodo en la secuencia.
    *   Contendrá un **puntero/referencia `prev`** que apunta al Nodo anterior en la secuencia.

*   **Lista Doblemente Enlazada Circular (CircularDoubleLinkedList):**
    *   Gestionará la colección de Nodos.
    *   Mantendrá una referencia al **nodo "cabeza" (`head`)** o al **nodo actualmente seleccionado (`current`)** para facilitar la navegación. Si se usa un `current`, la naturaleza circular significa que cualquier nodo puede ser el punto de inicio del recorrido lógico.
    *   Opcionalmente, puede mantener un contador del número total de nodos (`size`).
    *   La naturaleza **circular** se asegura haciendo que el puntero `next` del último nodo apunte al primer nodo (`head`), y el puntero `prev` del primer nodo (`head`) apunte al último nodo.

## 2. Datos del Elemento

Cada nodo en la CDLL almacenará los datos de un elemento seleccionable. Estos datos se limitarán a **tipos primitivos** como se define en los requisitos generales del proyecto. Para un selector de elementos/personajes, los datos mínimos requeridos por nodo serán:

*   `id`: Un número entero (`int`) único para identificar el elemento.
*   `nombre`: El nombre del elemento/personaje (`str`).
*   *(Opcional)*: Podrían añadirse otros datos primitivos como `bool` para estado (ej. desbloqueado), `int` para nivel, etc., si el caso de uso lo requiere, pero `id` y `nombre` son suficientes para la funcionalidad principal.

## 3. Operaciones (Funcionalidades)

La aplicación de consola, en su versión con CDLL, ofrecerá al usuario las siguientes operaciones, las cuales se basan directamente en la manipulación de la lista:

*   **3.1. Inicializar Selector:**
    *   Crea la CDLL con un conjunto inicial de elementos predefinidos.
    *   Establece el nodo `current` al primer elemento o a un elemento por defecto.
    *   *(Nota: Si bien el anteproyecto menciona añadir/eliminar como opcional, la lista necesita ser populada inicialmente. Esta operación cubre esa necesidad).*

*   **3.2. Mover al Siguiente Elemento:**
    *   Cambia el nodo `current` al nodo al que apunta `current.next`.
    *   Esta operación es central a la navegación cíclica hacia adelante.
    *   Debe manejar el caso especial (natural en CDLL) de moverse del último elemento al primero.

*   **3.3. Mover al Elemento Anterior:**
    *   Cambia el nodo `current` al nodo al que apunta `current.prev`.
    *   Esta operación es central a la navegación cíclica hacia atrás.
    *   Debe manejar el caso especial (natural en CDLL) de moverse del primer elemento al último.

*   **3.4. Mostrar Elemento Seleccionado:**
    *   Accede a los datos del nodo `current` (su `id` y `nombre`).
    *   Imprime la información del elemento actualmente seleccionado en la consola.

*   **3.5. Listar Todos los Elementos:**
    *   Recorre la CDLL completa, empezando desde un punto conocido (ej. `head` o `current`).
    *   Imprime la información (`id`, `nombre`) de cada nodo visitado antes de regresar al nodo de inicio.
    *   Esta operación demuestra el contenido total de la lista.

*   **3.6. Salir:**
    *   Termina la ejecución de la aplicación.

*(Esta versión cumplirá con el requisito de un mínimo de 4 operaciones distintas para el usuario, incluyendo inicializar, mover (siguiente/anterior, que pueden contarse como dos o una combinada con dirección), mostrar y listar).*

## 4. Requerimientos Técnicos Adicionales

*   **Aplicación de Consola:** La interacción con el usuario (entrada de comandos/opciones, salida de información) se realizará a través de la consola.
*   **Manejo de Errores:** La aplicación debe ser robusta. Se implementará manejo de errores para prevenir caídas, por ejemplo:
    *   Intentar mover en una lista vacía (aunque `Inicializar` debería crear una lista no vacía).
    *   Entrada de usuario inválida (opciones de menú no reconocidas).
*   **Uso de la CDLL:** Todas las operaciones de navegación y acceso a elementos listadas (3.2 a 3.5) deben basarse directamente en los métodos y la estructura de la CDLL.

## 5. Alcance de la Parte 1

Esta fase se enfoca en la implementación estándar de la CDLL y su aplicación directa al caso de uso del selector cíclico. El número de elementos puede ser moderado (ej. 5 a 10+) para demostrar la escalabilidad comparativa con la versión primitiva. Esta implementación servirá como referencia funcional y base para la replicación en la Parte 2.

---
