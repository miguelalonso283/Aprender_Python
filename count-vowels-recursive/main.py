def count_vowels(texto):
    if not texto:
        return 0
    return (texto[0] in 'aeiouáéíóúüAEIOUÁÉÍÓÚÜ') + count_vowels(texto[1:])


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(count_vowels)
