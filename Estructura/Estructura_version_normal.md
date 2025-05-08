## Estructura de Dependencias de Archivos (Parte 1: Versión CDLL)

Para la implementación del Selector Cíclico utilizando la Lista Doblemente Enlazada Circular (CDLL), el código está organizado en tres archivos principales (`CDLLB.py`, `operations.py`, `main.py`). La relación entre estos archivos se basa en cómo un archivo necesita importar y utilizar componentes (clases, funciones) definidos en otro.

Comprender estas dependencias es clave para entender el flujo de control y la separación de responsabilidades en esta parte del proyecto.

### Diagrama de Dependencias

El siguiente diagrama ilustra cómo los archivos se relacionan a través de las importaciones:

```text
+-----------+               +--------------+
|           | -- imports --> |              |
|  main.py  |                | operations.py|
| (UI/Entry)|                |   (Logic)    |
|           | -- imports --> |              |
+-----------+                +--------------+
      |                             |
      |          imports            |
      |-----------------------------|
                   |
                   v
               +--------------+
               |              |
               |   CDLLB.py   |
               | (CDLL Base)  |
               |              |
               +--------------+
