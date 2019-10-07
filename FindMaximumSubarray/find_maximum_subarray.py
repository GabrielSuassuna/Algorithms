import math

def find_max_crossing_subarray(array, low, mid, hight):
    max_left = 0
    max_right = 0
    left_sum = -math.inf
    sum_value = 0
    for i in range(mid, low, -1):
        sum_value += array[i]
        if sum_value > left_sum:
            left_sum = sum_value
            max_left = i
    right_sum = -math.inf
    sum_value = 0
    for j in range (mid+1, hight):
        sum_value += array[j]
        if sum_value > right_sum:
            right_sum = sum_value
            max_right = j
    return max_left, max_right, left_sum+right_sum

def find_maximum_subarray(array, low, hight):
    if hight == low:
        return low, hight, array[low]
    else:
        mid = math.floor((low+hight)/2)
        left_low, left_hight, left_sum = find_maximum_subarray(array, low, mid)
        right_low, right_hight, right_sum = find_maximum_subarray(array, mid+1, hight)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(array, low, mid, hight)
        
        if left_sum >= right_sum and left_sum>= cross_sum:
            return left_low, left_hight, left_sum
        elif right_sum >= left_sum and right_sum>= cross_sum:
            return right_low, right_hight, right_sum
        else:
            return cross_low, cross_high, cross_sum

a = [-1, -2, -3, -4, -5]
print(find_maximum_subarray(a, 0, 4))