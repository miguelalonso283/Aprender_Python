def rslice(text: str, size: int) -> list:
    if not text:
        return []
    return [text[:size]]+rslice(text[size:],size)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(rslice)
