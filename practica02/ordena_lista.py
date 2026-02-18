#Raul Sanchez Merino 
#raulsm

# Ejercicio: comprobar que su argumento es una lista, mostrando un error en otro caso.
mi_lista = ["aa", "z34", " " ,"hfshj","bb", "jJjj"]

def verificarlista(lista):
    # Verificar que el argumento sea una lista
    if not isinstance(lista, list):
        raise TypeError("El argumento debe ser una lista.")

    # Verificar que todos los elementos de la lista son cadenas
    if not all(isinstance(cadena, str) for cadena in lista):
        raise ValueError("La lista debe contener solo cadenas.")

    # Ordenar la lista de forma destructiva por longitud de cadenas
    lista.sort(key=len)

    # Devolver la lista ordenada
    return lista

try:
    # Llamada a la función para verificar y ordenar la lista
    resultado = verificarlista(mi_lista)

    # Imprimir la lista ordenada
    print("Lista ordenada por longitud de cadenas:", resultado)
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

