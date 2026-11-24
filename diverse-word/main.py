def run(words: list) -> str:
    return max(words, key=lambda w: len(set(w.lower())))


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
