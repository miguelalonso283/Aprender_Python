def run(num_pillars: int, gap_pillars: float, pillar_width: float) -> float:
    inter_distance = (num_pillars-2)*pillar_width+(num_pillars-1)*gap_pillars*100
    return inter_distance


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
