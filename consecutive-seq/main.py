def consecutive_seq(valores, repeticiones):
    if not valores:                    # no queda nada: no hay ningún valor que cumpla
        return None
    n = _longitud_racha(valores)       # cuántas veces se repite seguido el primer valor
    if n == repeticiones:
        return valores[0]
    return consecutive_seq(valores[n:], repeticiones)   # seguimos tras la racha

def _longitud_racha(valores):
    """Longitud de la racha de valores iguales al inicio."""
    if len(valores) < 2 or valores[0] != valores[1]:
        return min(len(valores), 1)
    return 1 + _longitud_racha(valores[1:])

print(consecutive_seq((1, 74, 56, 56, 56, 332, 8, 8, 8), 3))  # 56
print(consecutive_seq((1, 2, 3), 2))                          # None


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(consecutive_seq)
