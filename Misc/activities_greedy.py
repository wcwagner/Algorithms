

def activity_selection(S, F):
    #assumed S,F are sorted on end time
    activities = []
    most_recent_end_time = -float("inf")

    for i in range(len(S)):
        if s[i] < most_recent_end_time:
            continue
        else:
            activities.append(i)
            most_recent_end_time = f[i]

        return activities


if __name__ == "__main__":
    S = [1,3,0,5,8,5]
    F = [2,4,6,7,9,9]

    print(activity_selection(S, F))

