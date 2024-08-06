def encontrar_comunes(arr1, arr2):
    # Convertimos las listas a conjuntos para eliminar duplicados y para buscar intersección
    set1 = set(arr1)
    set2 = set(arr2)
    
    # Utilizamos la operación de intersección para encontrar los elementos comunes
    comunes = list(set1 & set2)
    
    return comunes

# Ejemplo de uso
arreglo_a = [3, 1, 7, 9, 2]
arreglo_b = [4, 2, 8, 1, 5]
print(encontrar_comunes(arreglo_a, arreglo_b))  # Output: [1, 2]
