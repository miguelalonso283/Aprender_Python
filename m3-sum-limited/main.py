def run(limit: int) -> None:
    suma = 0
    multiplo_actual = 0
    resultado = ''

    while suma < limit:
        resultado += str(multiplo_actual) + ' '
        suma += multiplo_actual
        multiplo_actual += 3

    print(resultado.strip())


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
