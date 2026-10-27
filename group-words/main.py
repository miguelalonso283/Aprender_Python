def run(words: list) -> dict:
    group_words = {}

    for word in words:
        letter = word[0]
        if letter not in group_words:
            group_words[letter] = []
        
        group_words[letter].append(word)    

    return group_words


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
