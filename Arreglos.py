def encontrar_comunes(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    
    comunes = list(set1 & set2)
    
    return comunes

arreglo_a = [3, 1, 7, 9, 2]
arreglo_b = [4, 2, 8, 1, 5]
print(encontrar_comunes(arreglo_a, arreglo_b)) 

