def is_palindrome(texto):
    t = ''.join(texto.split()).lower()
    return t == t[::-1]


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_palindrome)
