def merge(left,right):
    def loop(left,right,ss):
        if not (left == [] or right == []):
            if left[0] <= right[0]:
                ss.append(left[0])
                return [left[0]] + loop(left[1:], right, ss)
            else:
                ss.append(right[0])
                return [right[0]] + loop(left, right[1:],ss)
        else:
            return left + right
    return loop(left,right,[])
