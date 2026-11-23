def is_magic_square(matriz):
    n = len(matriz)
    if n == 0:                         # matriz vacía: se considera mágica
        return True

    objetivo = sum(matriz[0])

    filas = all(sum(fila) == objetivo for fila in matriz)
    columnas = all(sum(fila[j] for fila in matriz) == objetivo for j in range(n))
    diag_principal = sum(matriz[i][i] for i in range(n)) == objetivo
    diag_secundaria = sum(matriz[i][n - 1 - i] for i in range(n)) == objetivo

    return filas and columnas and diag_principal and diag_secundaria

print(is_magic_square([]))                                 # True
print(is_magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))  # True
print(is_magic_square([[1, 2], [3, 4]]))                   # False


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_magic_square)
