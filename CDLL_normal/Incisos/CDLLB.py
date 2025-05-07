# CDLLB.py - Circular Doubly Linked List Base
# Aqui esta la estructura base de la CDLL
class ElementData:
    """
    Clase simple para almacenar los datos de un elemento seleccionable.
    """
    def __init__(self, id, nombre):
        if not isinstance(id, int):
            raise TypeError("El ID debe ser un entero.")
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        self.id = id       # Identificador único (int)
        self.nombre = nombre # Nombre del elemento (str)

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}"

    def __repr__(self):
        return f"ElementData(id={self.id}, nombre='{self.nombre}')"


class Node:
    """
    Representa un nodo en la Lista Doblemente Enlazada Circular.
    """
    def __init__(self, data):
        if not isinstance(data, ElementData):
             raise TypeError("Los datos del nodo deben ser una instancia de ElementData.")
        self.data = data
        self.next = None # Referencia al siguiente nodo
        self.prev = None # Referencia al nodo anterior

    def __str__(self):
        # Para representación simple del nodo, útil para depuración
        return f"Nodo({self.data.nombre})"


class CircularDoubleLinkedList:
    """
    Implementa una Lista Doblemente Enlazada Circular.
    Permite la navegación en ambas direcciones y envuelve los extremos.
    """
    def __init__(self):
        self.head = None    # Referencia al primer nodo
        self.current = None # Referencia al nodo actualmente seleccionado (para el selector)
        self.size = 0       # Número de nodos en la lista

    def is_empty(self):
        """Verifica si la lista está vacía."""
        return self.head is None

    def append(self, data: ElementData):
        """
        Añade un nuevo nodo al final de la lista.
        La lista se mantiene circular.
        """
        new_node = Node(data)

        if self.is_empty():
            # Si la lista está vacía, el nuevo nodo es la cabeza y se apunta a sí mismo
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            self.current = new_node # Al añadir el primero, lo seleccionamos
        else:
            # Encuentra el último nodo (que es el nodo anterior a la cabeza)
            last_node = self.head.prev

            # Enlaza el nuevo nodo:
            new_node.next = self.head     # El siguiente del nuevo es la cabeza
            new_node.prev = last_node     # El anterior del nuevo es el viejo último

            # Actualiza los enlaces de los nodos existentes:
            last_node.next = new_node     # El siguiente del viejo último es el nuevo
            self.head.prev = new_node     # El anterior de la cabeza es el nuevo

        self.size += 1

    def move_next(self):
        """Mueve la selección al siguiente nodo."""
        if not self.is_empty():
            self.current = self.current.next
            return True
        return False # No se pudo mover (lista vacía)

    def move_previous(self):
        """Mueve la selección al nodo anterior."""
        if not self.is_empty():
            self.current = self.current.prev
            return True
        return False # No se pudo mover (lista vacía)

    def get_current_data(self) -> ElementData | None:
        """Retorna los datos del nodo actualmente seleccionado."""
        if not self.is_empty() and self.current:
            return self.current.data
        return None # Lista vacía o current no está definido

    def list_all_elements(self):
        """
        Genera los datos de todos los elementos en la lista,
        comenzando desde la cabeza.
        """
        if self.is_empty():
            return []

        elements_data = []
        # Empezamos desde la cabeza para listar en un orden consistente
        temp_node = self.head
        # Recorremos hasta que volvamos a la cabeza
        while True:
            elements_data.append(temp_node.data)
            temp_node = temp_node.next
            if temp_node == self.head:
                break # Salimos del ciclo al regresar a la cabeza

        return elements_data

