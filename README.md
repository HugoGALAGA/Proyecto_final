# Índice de Temas del Proyecto

Bienvenido al índice de la documentación y el código fuente de este proyecto. Utiliza esta lista para navegar por los diferentes componentes y explicaciones.

*   **General del Proyecto:** Documentación que aplica a ambas partes del proyecto.
    *   [Caso de Uso del Proyecto](Caso_de_uso.md): Descripción de la aplicación "Selector Cíclico" y la justificación de por qué se eligió la CDLL.
    *   [Información de Licencia](LICENSE): Detalles sobre la licencia bajo la cual se distribuye el código.

*   **Parte 1: Implementación con Lista Doblemente Enlazada Circular (CDLL):**
    *   [Visión General de la Parte 1](CDLL_normal/Incisos/Explicacion.md): Explicación general sobre esta sección del proyecto.
    *   **Código Fuente:** Archivos Python que implementan la versión CDLL.
        *   [CDLLB.py](CDLL_normal/Incisos/CDLLB.py): Implementación base de la estructura CDLL y el Nodo.
        *   [operations.py](CDLL_normal/Incisos/operations.py): Funciones que definen las operaciones sobre la CDLL (mover, mostrar, listar).
        *   [main.py](CDLL_normal/Incisos/main.py): Punto de entrada y aplicación de consola para la versión CDLL.
    *   **Documentación Detallada:** Explicaciones individuales de los archivos de código de la Parte 1.
        *   [Explicación de CDLLB.py](CDLL_normal/Incisos/CDLLB.md)
        *   [Explicación de operations.py](CDLL_normal/Incisos/operations.md)
        *   [Explicación de main.py (Versión CDLL)](CDLL_normal/Incisos/main.md)

*   **Parte 2: Implementación Primitiva (Simulación sin Estructuras):**
    *   [Explicación Detallada y Código (Versión Primitiva)](CDLL_primitivo/Incisos/Prueba2.md): Documento que describe la lógica, funcionamiento y limitaciones de la implementación utilizando únicamente variables primitivas. (El código fuente está contenido en el mismo archivo `.py`).
    *   **Código Fuente:** Archivo Python que implementa la versión primitiva.
        *   [prueba_2.py](CDLL_primitivo/Incisos/prueba_2.py): Implementación completa y aplicación de consola para la versión primitiva extrema.

*(Nota sobre la estructura: La organización en subdirectorios `Incisos` y la posible duplicación de archivos como `Caso_de_uso.md`, `LICENSE` y `README.md` dentro de `CDLL_primitivo/Incisos` reflejan la estructura del repositorio observado. Los enlaces en este índice apuntan a las ubicaciones específicas de los archivos dentro de la estructura mostrada.)*

---
