
# Estructura de Archivos del Proyecto

Este proyecto implementa un "Selector Cíclico de Elementos" en dos versiones distintas: una utilizando la estructura de datos Lista Doblemente Enlazada Circular (CDLL) y otra replicando la funcionalidad utilizando únicamente variables primitivas. La estructura de archivos está diseñada para separar estas dos partes y organizar la documentación asociada.

## Diagrama de Archivos

A continuación, se presenta una representación visual de la estructura de directorios y archivos del proyecto:

```text
.
├── CDLL_normal/
│   └── Incisos/
│       ├── CDLLB.md          # Documentación: Explicación detallada de CDLLB.py
│       ├── CDLLB.py          # Código: Implementación base de la CDLL y el Nodo
│       ├── main.md           # Documentación: Explicación detallada de main.py (CDLL version)
│       ├── main.py           # Código: Punto de entrada y UI de consola (CDLL version)
│       ├── operations.md     # Documentación: Explicación detallada de operations.py
│       ├── operations.py     # Código: Lógica de operaciones sobre la CDLL
│       └── Explicacion.md    # Documentación: Explicación general de la parte CDLL? (Podría ser la explicación del caso de uso o una descripción general de esta parte)
├── CDLL_primitivo/
│   └── Incisos/
│       ├── Prueba2.md        # Documentación: Explicación detallada de prueba_2.py (Primitive version)
│       ├── prueba_2.py       # Código: Implementación y UI de consola (Primitive version)
│       ├── Caso_de_uso.md    # Documentación: (Copia redundante?) Caso de uso del proyecto
│       ├── LICENSE         # Documentación: (Copia redundante?) Información de licencia
│       └── README.md       # Documentación: (Copia redundante?) README para esta subcarpeta
├── Caso_de_uso.md          # Documentación: Descripción general del caso de uso del proyecto
├── LICENSE                 # Documentación: Información de licencia del proyecto
└── README.md               # Documentación: Archivo principal del repositorio (este archivo)
