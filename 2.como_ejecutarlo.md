## 🚀 Cómo Ejecutar el Proyecto

Este proyecto consta de dos aplicaciones de consola separadas, una para la implementación con CDLL y otra para la implementación primitiva. Sigue estos pasos para clonar el repositorio y ejecutar ambas versiones:

### Requisitos Previos

*   Tener [Python 3.x](https://www.python.org/downloads/) instalado en tu sistema.
*   Tener [Git](https://git-scm.com/downloads) instalado para clonar el repositorio (o puedes descargar los archivos manualmente).

### Pasos para Ejecutar

1.  **Clonar el Repositorio:** Abre tu terminal o línea de comandos y ejecuta el siguiente comando para descargar el proyecto:

    ```bash
    git clone <URL del repositorio>
    ```
    *(Reemplaza `<URL del repositorio>` con la URL real de tu repositorio, por ejemplo, `https://github.com/TuUsuario/NombreDeTuRepo.git`)*

2.  **Navegar al Directorio del Proyecto:** Ingresa al directorio raíz del proyecto que acabas de clonar:

    ```bash
    cd NombreDeTuRepo # O el nombre real del directorio clonado
    ```

3.  **Ejecutar la Versión con CDLL:**
    *   Esta versión utiliza la implementación estándar de la Lista Doblemente Enlazada Circular.
    *   Navega al directorio donde se encuentra el ejecutable de la Parte 1:
        ```bash
        cd CDLL_normal/Incisos
        ```
    *   Ejecuta el script principal:
        ```bash
        python main.py
        ```
    *   La aplicación de consola para la versión CDLL se iniciará y te mostrará un menú.

4.  **Ejecutar la Versión Primitiva:**
    *   Esta versión replica la funcionalidad usando únicamente variables primitivas y lógica condicional (la implementación "brutal").
    *   Desde el directorio raíz del proyecto, navega al directorio donde se encuentra el ejecutable de la Parte 2:
        ```bash
        cd CDLL_primitivo/Incisos
        ```
        *(O si sigues en `CDLL_normal/Incisos`, retrocede dos niveles y luego navega: `cd ../../CDLL_primitivo/Incisos`)*
    *   Ejecuta el script principal de la versión primitiva:
        ```bash
        python prueba_2.py
        ```
    *   La aplicación de consola para la versión primitiva se iniciará con su propio menú.

### Interacción

Una vez que cualquiera de las aplicaciones esté ejecutándose, se te presentará un menú con opciones numéricas (1, 2, 3, etc.). Ingresa el número de la opción deseada y presiona Enter. Sigue las indicaciones en la consola para interactuar con el selector.

Para salir de cualquiera de las aplicaciones, selecciona la opción correspondiente en el menú (generalmente la opción 6).

---
