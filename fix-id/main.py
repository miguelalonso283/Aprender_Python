def run(db: list) -> list:
    fixed_db = [{**r, 'id': i} for i, r in enumerate(db, start=1)]
    return fixed_db


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
