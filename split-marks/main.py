def run(marks: dict) -> tuple:
    failed = {}
    passed = {}
    for i in marks:
        if marks[i] < 5: failed[i.lower()] = marks[i]
        else : passed[i.upper()] = marks[i]
    
    return passed, failed


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
