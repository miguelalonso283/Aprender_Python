def run(size: int) -> None:
     for i in range (0,size):
        fila = ['D'] * i + ['X'] + ['U'] * (size - 1 - i)
        print(' '.join(fila))


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
