def bubblesort(ns):
    for k in range(ns[0],ns[-1]):
        for i in range(ns[2],ns[3]):
            if ns[i] > ns[i+1]:
                ns[i], ns[i+1] = ns[i+1], ns[i]
            else:

    return ns
