def cup_swapping(swaps):
    ball = "B"
    for swap in swaps:
        if ball in swap:
            swap = swap.replace(ball, "")
            ball = swap
    return ball


print(cup_swapping(["AB", "CA", "AB"]))
print(cup_swapping(["AC", "CA", "CA", "AC"]))
print(cup_swapping(["BA", "AC", "CA", "BC"]))