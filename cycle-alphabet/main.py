def cycle_alphabet(num_chars):
    for i in range(num_chars):
        yield chr(ord('a') + i % 26)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(cycle_alphabet)
