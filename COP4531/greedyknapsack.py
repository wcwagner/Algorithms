

def greedy_knapsack(capacity, wts, vals):

    #calculate val/wt ratio and modify vals in place
    for i in range(len(vals)):
        vals[i] = float(vals[i] / wts[i])

    #sorts the two arrays, vals, and wts by the value in vals (IN NON-INCREASING)
    #ex wts = [10, 30, 20], and vals=[60, 120, 100] gives us
    #val_to_wt = [6, 5, 4] and wts = [10, 20, 30] <-- each wt corresponds to correct item i
    val_to_wt, wts = zip(*sorted(zip(vals, wts), reverse=True))

    total = 0
    # go through each item, add as much as possible until none left or capacity hti
    for i in range(len(wts)):
        # add as much as possible
        weight_added = wts[i] if capacity >= wts[i] else capacity
        total += val_to_wt[i] * weight_added

        capacity -= weight_added

        if capacity <= 0:
            break

    return total

if __name__ == "__main__":

    vals = [60, 120, 100]
    wts = [10, 30, 20]

    print(greedy_knapsack(50, wts, vals))




