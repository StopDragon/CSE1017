def merge(left,right):
    ss = []
    while not (left == [] or right == []):
        if left[0] <= right[0]:
            ss.append(left[0])
            left, right = left[1:], right
        else:
            ss.append(right[0])
            left, right = left, right[1:]
    return ss + left + right
