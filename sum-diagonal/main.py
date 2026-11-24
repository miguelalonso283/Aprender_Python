def run(matrix: list) -> int | None:
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        return None
    return sum(matrix[i][i] for i in range(n))


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
