def add(lista):
    if not lista:                      # lista vacía
        return 0
    primero, resto = lista[0], lista[1:]
    if isinstance(primero, list):      # elemento anidado: sumamos recursivamente
        return add(primero) + add(resto)
    return primero + add(resto)

print(add([1, [2, 4], 5, [6, [7, 8]]]))  # 33
print(add([]))                           # 0


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(add)
