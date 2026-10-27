def run(text: str) -> int:
    # num_words = sum(1for item in text.split(text,' ') if item)
    num_words = len(text.split())
    return num_words


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
