def run(symbol: str) -> str:
    indice_coma= symbol.find(',')
    coeficiente = int(symbol[:indice_coma])
    exponente = int(symbol[indice_coma + 1:])
    nuevo_exponente = exponente+1
    integral = coeficiente/nuevo_exponente
    return str(int(integral))+"x^"+str(nuevo_exponente)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
