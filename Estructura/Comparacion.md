## Estructura General del Proyecto y Comparación de Versiones

Este proyecto implementa la misma funcionalidad de "Selector Cíclico de Elementos" en dos versiones distintas para demostrar el contraste entre el uso de una estructura de datos especializada (CDLL) y la manipulación directa con solo variables primitivas.

Ambas versiones son **ejecutables independientes** localizados en directorios separados, y no tienen dependencias de código entre sí. Su relación es conceptual: **resuelven el mismo problema** bajo diferentes restricciones, lo que permite una **comparación directa** de la eficiencia y la conveniencia de cada enfoque.

### Diagrama Comparativo de Estructuras

El siguiente diagrama muestra la estructura de archivos y las dependencias *internas* para cada una de las dos versiones del proyecto:

```text
      +--------------------+                               +----------------------+
      |                    |                               |                      |
      |   CDLL_normal/     |                               |   CDLL_primitivo/    |
      | (Versión CDLL)     |                               |  (Versión Primitiva) |
      |                    |                               |                      |
      +--------------------+                               +----------------------+
               |                                                     |
      +--------+-----------+                       +-----------------------------+
      |Directorio Contenido|                       |      Directorio Contenido   |
      |   (/Incisos)       |                       |       (/Incisos)            |
      +--------+-----------+                       +-----------------------------+
               |                                                     |
      +--------+----------+                       +-----------------------------+
      | main.py (UI/Entry)|                       | primitive_selector.py       |
      |                   |                       | (Monolítico: Variables,     |
      +--------+----------+                       |  Lógica, UI - Todo junto)   |
               |                                  |                             |
      +--------+----------+                       +-----------------------------+
      | operations.py     |                      
      | (Logic)           |                       | No hay importaciones
      +--------+----------+                       | *externas* relevantes.
               |                                  |
      +--------+-----------+                      |
      | CDLLB.py           |----------------------+
      | (CDLL Base)        |
      +--------------------+

<----------------------- Resuelven el Mismo Problema para Comparación ----------------------->
