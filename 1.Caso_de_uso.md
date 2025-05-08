## Caso de Uso del Proyecto: Selector Cíclico de Elementos

**Descripción de la Aplicación:**

La aplicación de consola implementa un **Selector Cíclico de Elementos**. Su funcionalidad principal es permitir al usuario navegar a través de un conjunto predefinido y ordenado de elementos (conceptualizados como personajes o ítems seleccionables) utilizando comandos simples de "Siguiente" y "Anterior". La característica distintiva es el comportamiento **cíclico**: al intentar moverse "Siguiente" desde el último elemento de la secuencia, la selección pasa automáticamente al primer elemento; de manera análoga, al moverse "Anterior" desde el primer elemento, la selección pasa al último. La aplicación muestra en la consola el elemento actualmente seleccionado.

**Elección del Caso de Uso y su Integración con la CDLL:**

Este caso de uso fue elegido específicamente porque se alinea de manera **ideal y natural** con las propiedades inherentes de la **Lista Doblemente Enlazada Circular (CDLL)**, la estructura de datos asignada para esta parte del proyecto.

La integración de la CDLL en las mecánicas de la aplicación es fundamental y se basa en las siguientes correspondencias:

1.  **Representación de Elementos:** Cada elemento seleccionable (cada "personaje" o "ítem") en nuestro selector se representa como un **Nodo** dentro de la CDLL. Los datos asociados al elemento (su ID, nombre, etc.) se almacenan como los datos (`data`) del nodo.
2.  **Navegación Bi-direccional:** La operación de mover "Siguiente" en el selector se mapea directamente a seguir el puntero `next` del nodo actualmente seleccionado en la CDLL. De igual forma, la operación de mover "Anterior" se realiza siguiendo el puntero `prev`. La naturaleza *doblemente enlazada* de la lista permite que ambas operaciones de navegación sean eficientes.
3.  **Comportamiento Cíclico:** La propiedad *circular* de la lista es la clave para implementar el comportamiento de "envolver". En una CDLL, el puntero `next` del último nodo apunta al primer nodo (`head`), y el puntero `prev` del primer nodo (`head`) apunta al último nodo. Esto significa que, al seguir `next` desde el último nodo o `prev` desde el primer nodo, la navegación **automáticamente** salta al otro extremo de la lista sin requerir lógica condicional adicional en la aplicación para manejar los casos de los extremos.
4.  **Estado Actual:** La referencia al elemento actualmente seleccionado por el usuario se mantiene convenientemente mediante el puntero `current` (o una referencia similar) dentro de la clase `CircularDoubleLinkedList` que gestiona la lista.

En resumen, la CDLL no es solo una estructura de datos utilizada en el proyecto; es el **mecanismo subyacente** que, debido a sus características de doble enlace y circularidad, proporciona exactamente las funcionalidades de navegación requeridas por el Selector Cíclico de la manera más directa, elegante y eficiente (O(1) para las operaciones de movimiento y acceso al elemento actual). Esto la convierte en la elección perfecta para modelar este tipo de comportamiento cíclico.
