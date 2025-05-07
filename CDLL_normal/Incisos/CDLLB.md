# Explicación Detallada del Archivo `CDLLB.py`

El archivo `CDLLB.py` es el **corazón** de la Parte 1 del proyecto. Contiene la definición fundamental de la estructura de datos que se utilizara: la **Lista Doblemente Enlazada Circular (CDLL)**. Este archivo abstrae cómo se almacenan y enlazan los elementos, proporcionando las herramientas básicas para construir y navegar la lista.

## 1. Propósito del Archivo

El objetivo de `CDLLB.py` es encapsular la lógica de la CDLL. Define los bloques de construcción (los Nodos) y el mecanismo para gestionarlos como una colección circular y bi-direccional. Al separar la implementación de la estructura (`CDLLB.py`) de las operaciones de negocio (`operations.py`) y la interfaz de usuario (`main.py`), se logra un diseño modular y limpio, donde la complejidad de la estructura de datos se mantiene aislada.

## 2. Estructuras Definidas

El archivo define tres elementos principales:

### 2.1. Clase `ElementData`

*   **Propósito:** Esta clase no es parte de la estructura de la lista en sí, sino un **contenedor simple para los datos primitivos** que cada elemento de la lista representará. Se utiliza para agrupar el ID y el nombre del elemento de una manera organizada antes de ser almacenados dentro de un `Node`.
*   **Atributos:**
    *   `id` (`int`): Un identificador numérico único para el elemento.
    *   `nombre` (`str`): El nombre descriptivo del elemento.
*   **Lógica y Funcionamiento:** Su funcionamiento es mínimo; simplemente almacena y permite acceder a `id` y `nombre`. Incluye verificaciones de tipo básicas en su constructor (`__init__`) para asegurar que los datos son primitivos `int` y `str`. Los métodos `__str__` y `__repr__` facilitan la representación legible del objeto.
*   **Complejidad:** Las operaciones en esta clase (creación, acceso a atributos) son **O(1)**, ya que implican una cantidad constante de trabajo.

### 2.2. Clase `Node`

*   **Propósito:** Representa un **único eslabón** (o nodo) dentro de la cadena de la lista enlazada. Cada `Node` conoce sus datos y a sus vecinos (el anterior y el siguiente).
*   **Atributos:**
    *   `data` (`ElementData`): Una referencia al objeto `ElementData` que contiene la información real del elemento que este nodo representa.
    *   `next` (`Node` o `None`): Una referencia (puntero) al siguiente `Node` en la secuencia de la lista.
    *   `prev` (`Node` o `None`): Una referencia (puntero) al `Node` anterior en la secuencia de la lista.
*   **Lógica y Funcionamiento:** El constructor (`__init__`) toma el objeto `data` y inicializa los punteros `next` y `prev` a `None`. Estos punteros serán actualizados por la clase `CircularDoubleLinkedList` cuando el nodo sea añadido a la lista y enlazado con otros nodos. Incluye una verificación de tipo para `data`.
*   **Complejidad:** La creación de un nodo es **O(1)**. El acceso a sus atributos `data`, `next`, `prev` también es **O(1)**.

### 2.3. Clase `CircularDoubleLinkedList`

*   **Propósito:** Esta es la clase que **gestiona la colección completa de `Node`s**. Define la estructura de la lista en sí y proporciona los métodos para interactuar con ella (añadir nodos, navegar, etc.). Mantiene la lógica de la circularidad y los enlaces dobles.
*   **Atributos:**
    *   `head` (`Node` o `None`): Una referencia al primer nodo de la lista. En una lista circular, este nodo es especial porque su `prev` apunta al último nodo y su `next` apunta al segundo (si existen).
    *   `current` (`Node` o `None`): Una referencia al nodo actualmente seleccionado por el selector. Esta referencia cambia con las operaciones `move_next` y `move_previous`.
    *   `size` (`int`): El número actual de nodos en la lista.
*   **Lógica y Funcionamiento de Métodos Clave:**
    *   `__init__()`: Inicializa la lista vacía, estableciendo `head`, `current` a `None` y `size` a 0.
    *   `is_empty()`: Retorna `True` si la lista no tiene nodos (`head` es `None`), `False` en caso contrario.
    *   `append(data)`: Añade un nuevo nodo con los `data` proporcionados al **final** de la lista.
        *   Si la lista está vacía, el nuevo nodo se convierte en `head`, `current`, y sus punteros `next` y `prev` se auto-referencian a sí mismo.
        *   Si la lista no está vacía, el nuevo nodo se inserta entre el nodo que actualmente es el último (`self.head.prev`) y el `self.head`. Se actualizan los punteros del nuevo nodo, del antiguo último nodo y del `self.head` para mantener la doble conexión y la circularidad.
    *   `move_next()`: Actualiza el `current` nodo al nodo al que apunta `self.current.next`. La circularidad inherente de la lista maneja automáticamente el caso de moverse del último nodo (cuyo `next` apunta a `head`) al primer nodo (`head`).
    *   `move_previous()`: Actualiza el `current` nodo al nodo al que apunta `self.current.prev`. La circularidad maneja el caso de moverse del primer nodo (cuyo `prev` apunta al último nodo) al último.
    *   `get_current_data()`: Retorna el objeto `ElementData` almacenado en el nodo `current`. Retorna `None` si la lista está vacía o `current` no está definido.
    *   `list_all_elements()`: Recorre toda la lista comenzando desde `self.head` (o cualquier otro punto, pero `head` garantiza un orden consistente si la lista se construyó secuencialmente). Sigue los punteros `next` hasta que regresa al nodo de inicio (`self.head`), recolectando los datos de cada nodo visitado.

*   **Complejidad de Métodos Clave:** La eficiencia de las operaciones es una ventaja principal de la CDLL:
    *   `__init__()`: **O(1)**
    *   `is_empty()`: **O(1)**
    *   `append(data)` (al final usando `head.prev`): **O(1)**. En una lista doblemente enlazada *no circular* sin referencia al último nodo (`tail`), añadir al final sería O(N). La circularidad (y el acceso directo a `head.prev`) lo hace O(1).
    *   `move_next()`: **O(1)**. Solo implica actualizar una referencia.
    *   `move_previous()`: **O(1)**. Solo implica actualizar una referencia.
    *   `get_current_data()`: **O(1)**. Acceso directo a una referencia.
    *   `list_all_elements()`: **O(N)**, donde N es el número de nodos. Es necesario visitar cada nodo al menos una vez para listar sus datos.

## 3. Rol en el Proyecto General

`CDLLB.py` proporciona la infraestructura de datos para la primera versión de la aplicación. `operations.py` importa y utiliza la clase `CircularDoubleLinkedList` para implementar la lógica de alto nivel del selector (mover, mostrar, listar). `main.py` a su vez interactúa con `operations.py`. De esta forma, `CDLLB.py` actúa como la capa más fundamental que define *cómo se estructura la información enlazada y circularmente*, sin preocuparse por *qué* se hace con esa información a nivel de aplicación de consola.

La implementación en `CDLLB.py` demuestra cómo una estructura de datos bien diseñada puede proporcionar operaciones comunes (como añadir al final, moverse a siguiente/anterior) con una eficiencia de **O(1)**, lo cual es muy ventajoso para aplicaciones donde estas operaciones son frecuentes, como en el caso de nuestro selector cíclico.

