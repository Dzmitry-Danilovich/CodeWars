def getting_mad(arr):
    tab = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                tab.append(abs(arr[i]-arr[j]))
    return min(tab)
