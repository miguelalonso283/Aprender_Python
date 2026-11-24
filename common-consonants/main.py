def run(text1: str, text2: str) -> str:
    vowels = 'aeiou'
    def consonants(t):
        return {c for c in t.lower() if c.isalpha() and c not in vowels}
    return ''.join(sorted(consonants(text1) & consonants(text2)))


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
