def max_sell(values):
    # all array check goes here

    global_small = values[0]
    global_profit = 0  # if possible, take the system minimum value here

    for value in values:
        global_small = min(global_small, value)

        current_profit = value - global_small

        global_profit = max(global_profit, current_profit)

    return global_profit


print(max_sell([8, 9, 5, 6, 12, 10, 11]))
