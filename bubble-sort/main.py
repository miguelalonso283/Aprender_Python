def bsort(lista):
    resultado = lista[:]               # copia: no modificamos la original
    n = len(resultado)
    hay_cambios = True

    while hay_cambios:                 # repetimos pasadas hasta que no haya intercambios
        hay_cambios = False
        for i in range(n - 1):
            if resultado[i] > resultado[i + 1]:
                resultado[i], resultado[i + 1] = resultado[i + 1], resultado[i]
                hay_cambios = True
        n -= 1                         # el último elemento de cada pasada ya está en su sitio

    return resultado

original = [5, 2, 9, 1, 5, 6]
print(bsort(original))   # [1, 2, 5, 5, 6, 9]
print(original)          # [5, 2, 9, 1, 5, 6] (sin cambios)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(bsort)
