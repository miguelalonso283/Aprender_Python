def extract_evens(valores):
    return [v for v in valores if v % 2 == 0]

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(extract_evens)
